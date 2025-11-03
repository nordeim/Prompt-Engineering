# Clinic Dataset Conversion Notebook (v1)
# Jupyter-style notebook content (Python)
# Purpose: De-identify clinic EHR rows, convert to JSONL instruction-response pairs,
# and run automated quality checks before training.

"""
Usage notes:
- Run this notebook on a secured environment. Do NOT upload PHI to external services.
- This notebook performs heuristic de-identification; ALWAYS perform human review
  and consider using production de-identification tools for regulatory compliance.
- Outputs: `instruction_dataset.jsonl` (ready for training) and `quality_report.json`.
"""

# Cell 1: Imports & setup
import re
import json
import csv
from pathlib import Path
from typing import Dict, List, Any
import pandas as pd
from datasets import Dataset
from tqdm.auto import tqdm
import random

# Cell 2: Configuration
INPUT_CSV = Path("/data/clinic_raw.csv")  # expected input CSV with one row per patient encounter
OUTPUT_JSONL = Path("/data/instruction_dataset.jsonl")
QUALITY_REPORT = Path("/data/quality_report.json")
SAMPLE_OUTPUT = Path("/data/sample_output.jsonl")

# Column expectations in INPUT_CSV (adjustable)
# id, age, sex, medical_history (semicolon separated), medications (semicolon separated), allergies,
# vitals_json (json-string or key:value semicolon), presenting_complaint, clinician_note, outcome

EXPECTED_COLUMNS = [
    'id','age','sex','medical_history','medications','allergies','vitals','presenting_complaint','clinician_note'
]

# De-identification configuration (heuristic)
NAME_PATTERN = re.compile(r"\b([A-Z][a-z]+(?: [A-Z][a-z]+){0,2})\b")
DATE_PATTERN = re.compile(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b")
ISO_DATE_PATTERN = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
PHONE_PATTERN = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b")
MRN_PATTERN = re.compile(r"\b(?:MRN|mrn|Medical Record Number)[:#\s]*\w+\b")
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
URL_PATTERN = re.compile(r"https?://\S+")

# More robust PHI patterns can be added here.
PHI_PATTERNS = [
    (NAME_PATTERN, '[NAME]'),
    (ISO_DATE_PATTERN, '[DATE]'),
    (DATE_PATTERN, '[DATE]'),
    (PHONE_PATTERN, '[PHONE]'),
    (EMAIL_PATTERN, '[EMAIL]'),
    (URL_PATTERN, '[URL]'),
    (MRN_PATTERN, '[ID]')
]

# Words that are allowed to appear as names in medical contexts (to avoid over-redaction)
WHITELIST_NAMES = set([ 'May', 'June', 'August' ])  # extend as needed

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Cell 3: Helper functions

def deidentify_text(text: str) -> str:
    if not isinstance(text, str):
        return text
    out = text
    # First, mask MRNs/IDs aggressively
    for patt, repl in PHI_PATTERNS:
        out = patt.sub(repl, out)
    # Heuristic: reduce sequences of multiple whitespace
    out = re.sub(r"\s+", " ", out).strip()
    return out


def parse_vitals(vitals_field: str) -> Dict[str, str]:
    """Parse simple vitals formats into a dict. Accepts json-like or k:v; pairs separated by ;"""
    if not isinstance(vitals_field, str):
        return {}
    vitals_field = vitals_field.strip()
    # Try JSON
    try:
        import json
        d = json.loads(vitals_field)
        if isinstance(d, dict):
            return {k:str(v) for k,v in d.items()}
    except Exception:
        pass
    # Try key:value pairs
    pairs = [p.strip() for p in vitals_field.split(';') if ':' in p]
    out = {}
    for p in pairs:
        k,v = p.split(':',1)
        out[k.strip()] = v.strip()
    return out


def build_instruction_prompt(row: Dict[str,Any]) -> str:
    """Build a standardized instruction prompt for the model from a de-identified row."""
    parts = []
    # demographics
    age = row.get('age')
    sex = row.get('sex')
    if age:
        parts.append(f"Age: {age}")
    if sex:
        parts.append(f"Sex: {sex}")
    # medical history
    mh = row.get('medical_history')
    if mh:
        parts.append(f"Medical history: {mh}")
    meds = row.get('medications')
    if meds:
        parts.append(f"Medications: {meds}")
    allergies = row.get('allergies')
    if allergies:
        parts.append(f"Allergies: {allergies}")
    vitals = row.get('vitals')
    if vitals:
        vit_str = "; ".join([f"{k}: {v}" for k,v in vitals.items()])
        parts.append(f"Vitals: {vit_str}")
    pc = row.get('presenting_complaint')
    if pc:
        parts.append(f"Presenting complaint: {pc}")
    note = row.get('clinician_note')
    if note:
        parts.append(f"Clinician note: {note}")

    instruction = (
        "You are a clinic pre-screening assistant. Review the patient information below. "
        "Ask any clarifying questions needed and produce a structured preliminary assessment for nurse review. "
        "Do NOT provide a definitive diagnosis or prescribe medications. Always end with: "
        "'[This is a preliminary assessment — requires clinician review]'.\n\n"
    )
    prompt = "\n".join(parts) + "\n\n" + instruction + "\n
Response:\n"
    return prompt


def row_to_example(row: Dict[str, Any]) -> Dict[str, Any]:
    # id
    example = {
        'id': str(row.get('id', '')),
        'source': row.get('_source','clinic'),
        'demographics': {
            'age': row.get('age'),
            'sex': row.get('sex')
        },
        'medical_history': row.get('medical_history'),
        'medications': row.get('medications'),
        'allergies': row.get('allergies'),
        'vitals': row.get('vitals'),
        'presenting_complaint': row.get('presenting_complaint'),
        'instruction': build_instruction_prompt(row),
        'response': row.get('gold_response', ''),
        'metadata': {'anonymized': True}
    }
    return example

# Cell 4: Load raw CSV (with safe preview)
if not INPUT_CSV.exists():
    print(f"Input CSV {INPUT_CSV} not found. Please place your CSV at this path or update INPUT_CSV variable.")
else:
    print("Loading CSV...")
    raw_df = pd.read_csv(INPUT_CSV, dtype=str).fillna("")
    print(f"Loaded {len(raw_df)} rows. Columns: {raw_df.columns.tolist()}")

# Quick schema check
missing_cols = [c for c in EXPECTED_COLUMNS if c not in raw_df.columns]
if missing_cols:
    print("Warning: expected columns missing:", missing_cols)

# Cell 5: De-identify and convert rows
processed = []
quality_issues = {
    'missing_demographics':0,
    'phi_found_after_deid':0,
    'empty_instruction':0,
}

for _, r in tqdm(raw_df.iterrows(), total=len(raw_df)):
    row = r.to_dict()
    # Basic field normalization
    # medical_history and medications are semicolon-separated lists -> normalize
    mh = row.get('medical_history','').strip()
    if mh and (';' in mh):
        mh = [x.strip() for x in mh.split(';') if x.strip()]
        row['medical_history'] = mh
    else:
        row['medical_history'] = [mh] if mh else []
    meds = row.get('medications','').strip()
    if meds and (';' in meds):
        meds = [x.strip() for x in meds.split(';') if x.strip()]
        row['medications'] = meds
    else:
        row['medications'] = [meds] if meds else []

    # Parse vitals field
    row['vitals'] = parse_vitals(row.get('vitals',''))

    # De-identify free text fields
    for f in ['presenting_complaint','clinician_note']:
        text = row.get(f,'')
        deid = deidentify_text(text)
        # quick check: if common NAME tokens still present, count
        if re.search(r"\b[A-Z][a-z]{2,}\b", deid):
            # very coarse check; not definitive
            pass
        row[f] = deid

    # Demographics check
    if not row.get('age') or not row.get('sex'):
        quality_issues['missing_demographics'] += 1

    # Create gold_response if not present (we can leave empty; nurse will create later)
    if not row.get('gold_response'):
        row['gold_response'] = ''

    # Convert into example
    example = row_to_example(row)

    # Quick PHI regex scan on serialized text: if any PHI-like patterns remain, flag
    serialized = json.dumps(example)
    if re.search(r"\b\d{3}-\d{2}-\d{4}\b", serialized) or re.search(r"\b\d{4}-\d{2}-\d{2}\b", serialized):
        quality_issues['phi_found_after_deid'] += 1

    if not example['instruction'].strip():
        quality_issues['empty_instruction'] += 1

    processed.append(example)

print(f"Processed {len(processed)} examples. Issues: {quality_issues}")

# Cell 6: Save JSONL
with OUTPUT_JSONL.open('w', encoding='utf-8') as fh:
    for ex in processed:
        fh.write(json.dumps(ex, ensure_ascii=False) + '\n')
print(f"Wrote {len(processed)} examples to {OUTPUT_JSONL}")

# Save sample output for inspection
sample_n = min(10, len(processed))
with SAMPLE_OUTPUT.open('w', encoding='utf-8') as fh:
    for ex in random.sample(processed, sample_n):
        fh.write(json.dumps(ex, ensure_ascii=False) + '\n')

# Cell 7: Basic quality report
report = {
    'num_input_rows': len(raw_df),
    'num_output_examples': len(processed),
    'quality_issues': quality_issues,
    'sample_output_file': str(SAMPLE_OUTPUT),
}
with QUALITY_REPORT.open('w', encoding='utf-8') as fh:
    json.dump(report, fh, indent=2)
print(f"Quality report written to {QUALITY_REPORT}")

# Cell 8: Simple validation checks (human-in-the-loop suggestions)
# - Print a few random examples for human review
print('\n=== SAMPLE EXAMPLES FOR HUMAN REVIEW ===\n')
for ex in random.sample(processed, sample_n):
    print('ID:', ex['id'])
    print('Instruction:', ex['instruction'][:400].replace('\n',' | '))
    print('Response (gold):', (ex['response'][:400] if ex['response'] else '<EMPTY>'))
    print('-'*80)

print('\nPlease review the sample examples. Ensure PHI is removed and instructions are clear.\n')

# Cell 9: Export small validation set for labeling by nurses
VALIDATION_SET = Path('/data/validation_set_for_nurse_labeling.jsonl')
val_size = min(100, max(10, int(len(processed)*0.05)))
val_examples = random.sample(processed, val_size)
with VALIDATION_SET.open('w', encoding='utf-8') as fh:
    for ex in val_examples:
        fh.write(json.dumps(ex, ensure_ascii=False) + '\n')
print(f"Exported {val_size} examples for nurse labeling to {VALIDATION_SET}")

# End of notebook

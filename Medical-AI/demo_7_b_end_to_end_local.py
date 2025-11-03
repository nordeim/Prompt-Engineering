# Demo: End-to-end local fine-tune + inference (7B model) for Medical Assistant (synthetic data)
# File: demo_7b_end_to_end_local.md

# Overview
This demo provides a compact, runnable end-to-end example to fine-tune a *7B* instruction-following model (e.g. `mistralai/Mistral-7B-Instruct` or `TheBloke/llama3-8b-instruct` if you have it) with **LoRA/PEFT** on a tiny synthetic clinic dataset and run a simple inference. It's designed to run on a single 24GB+ GPU. If you only have a smaller GPU or CPU, I'll note fallbacks.

Contents:
- `requirements.txt` (minimal)
- `generate_synthetic.py` — creates a tiny synthetic JSONL dataset (50 examples)
- `demo_train.py` — small LoRA training script using Hugging Face + PEFT + bitsandbytes (8-bit)
- `demo_infer.py` — runs inference with the saved LoRA adapter
- `README` — run instructions + tips

---

## requirements.txt
```
transformers>=4.35.0
accelerate>=0.20.3
peft>=0.4.0
bitsandbytes>=0.39.0
safetensors
datasets
sentence-transformers
torch>=2.1.0
huggingface_hub
```

---

## generate_synthetic.py
```python
"""Generate a tiny synthetic clinic instruction dataset (JSONL).
Each example follows the instruction->response template used in training.
"""
import json
import random
from pathlib import Path

OUT = Path('synthetic_small.jsonl')
NUM = 50

presenting_templates = [
    "sore throat and runny nose for 2 days",
    "central chest pressure for 30 minutes, sweating",
    "fever 38.5C and productive cough",
    "acute right lower quadrant abdominal pain",
    "headache and visual changes",
]

histories = [
    "type 2 diabetes; hypertension",
    "no significant past medical history",
    "asthma since childhood",
    "history of ischemic heart disease",
    "previous appendectomy"
]

responses = [
    "PRELIMINARY_ASSESSMENT:\nTriage Priority: LOW\nLikely viral upper respiratory infection. Ask about duration of fever and breathing difficulty.\nAction: symptomatic care. [This is preliminary — requires clinician review]",
    "PRELIMINARY_ASSESSMENT:\nTriage Priority: HIGH\nConcern for possible acute coronary syndrome. Immediate ECG and transfer.\nAction: call physician urgently. [This is preliminary — requires clinician review]",
    "PRELIMINARY_ASSESSMENT:\nTriage Priority: MEDIUM\nLikely community-acquired pneumonia. Recommend chest X-ray and vitals monitoring.\nAction: nurse to obtain CXR. [This is preliminary — requires clinician review]",
]

random.seed(42)
with OUT.open('w', encoding='utf-8') as fh:
    for i in range(NUM):
        pc = random.choice(presenting_templates)
        mh = random.choice(histories)
        meds = "; ".join(random.sample(["metformin","lisinopril","salbutamol","aspirin"], k=random.randint(0,2)))
        vitals = {"bp":"{}\/{}".format(random.randint(110,160), random.randint(60,100)), "hr":str(random.randint(60,120)), "temp":"{:.1f}C".format(random.uniform(36.5,39.5))}
        instruction = f"Age: {random.randint(18,85)}\nSex: {random.choice(['M','F'])}\nMedical history: {mh}\nMedications: {meds}\nAllergies: NKDA\nVitals: bp:{vitals['bp']}; hr:{vitals['hr']}; temp:{vitals['temp']}\nPresenting complaint: {pc}\n\nYou are a clinic pre-screening assistant. Review the patient info and ask clarifying questions, then produce a structured preliminary assessment for nurse review. Do NOT give definitive diagnoses.\n\nResponse:\n"
        response = random.choice(responses)
        ex = {
            'id': f'synth_{i:03d}',
            'instruction': instruction,
            'response': response
        }
        fh.write(json.dumps(ex, ensure_ascii=False) + '\n')
print('Wrote', OUT)
```

---

## demo_train.py
```python
"""Tiny LoRA training on synthetic dataset.
Designed for single GPU with >=24GB VRAM. Uses load_in_8bit for memory efficiency.
"""
import argparse
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import torch

MODEL = 'mistralai/Mistral-7B-Instruct'  # change if you prefer another 7B instruct model

def tokenize_fn(example, tokenizer, max_length=1024):
    text = example['instruction'] + example['response']
    out = tokenizer(text, truncation=True, max_length=max_length, padding='max_length')
    out['labels'] = out['input_ids'].copy()
    return out

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='synthetic_small.jsonl')
    parser.add_argument('--output_dir', type=str, default='./demo_lora')
    parser.add_argument('--epochs', type=int, default=2)
    parser.add_argument('--batch_size', type=int, default=1)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(MODEL, use_fast=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    print('Loading base model (8-bit)...')
    model = AutoModelForCausalLM.from_pretrained(MODEL, load_in_8bit=True, device_map='auto', trust_remote_code=True)
    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(r=16, lora_alpha=32, target_modules=['q_proj','k_proj','v_proj','o_proj'], lora_dropout=0.05, bias='none', task_type='CAUSAL_LM')
    model = get_peft_model(model, lora_config)

    ds = load_dataset('json', data_files={'train': args.data}, split='train')
    tokenized = ds.map(lambda x: tokenize_fn(x, tokenizer), batched=False, remove_columns=ds.column_names)

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=4,
        num_train_epochs=args.epochs,
        fp16=True,
        logging_steps=10,
        save_steps=200,
        save_total_limit=2,
        learning_rate=2e-4,
        optim='paged_adamw_8bit'
    )

    trainer = Trainer(model=model, args=training_args, train_dataset=tokenized, data_collator=data_collator, tokenizer=tokenizer)
    trainer.train()
    print('Saving LoRA adapter...')
    model.save_pretrained(args.output_dir)
```

Notes:
- `load_in_8bit=True` requires compatible bitsandbytes and GPU setup.
- If you do not have a 24GB GPU, change to a 3–4 epoch run with smaller batch and accumulate, or use a smaller model (7B distilled) or run on CPU with `torch_dtype='auto'` but training will be very slow.

---

## demo_infer.py
```python
"""Load base model + LoRA adapter and run an example inference.
"""
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

BASE = 'mistralai/Mistral-7B-Instruct'
ADAPTER_DIR = './demo_lora'  # where demo_train saved adapter

def generate(prompt, max_new_tokens=256, temperature=0.0):
    tokenizer = AutoTokenizer.from_pretrained(BASE, use_fast=True)
    model = AutoModelForCausalLM.from_pretrained(BASE, load_in_8bit=True, device_map='auto', trust_remote_code=True)
    # load LoRA adapter
    try:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, ADAPTER_DIR)
    except Exception as e:
        print('Peft adapter load failed:', e)
    inputs = tokenizer(prompt, return_tensors='pt').to('cuda')
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new_tokens, temperature=temperature)
    return tokenizer.decode(out[0], skip_special_tokens=True)

if __name__ == '__main__':
    # example prompt derived from synthetic format
    prompt = (
        "Age: 58\nSex: M\nMedical history: type 2 diabetes; hypertension\nMedications: metformin\nAllergies: NKDA\nVitals: bp:150/92; hr:105; temp:37.8C\nPresenting complaint: central chest pressure for 20 minutes\n\n"
        "You are a clinic pre-screening assistant. Review the patient info and ask clarifying questions, then produce a structured preliminary assessment for nurse review. Do NOT give definitive diagnoses.\n\nResponse:\n"
    )
    out = generate(prompt)
    print('--- MODEL OUTPUT ---')
    print(out)
```

---

## README (run steps)
1. Create a Python environment and install requirements:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Generate synthetic data:
```
python generate_synthetic.py
```
3. Train (single GPU with >=24GB):
```
python demo_train.py --data synthetic_small.jsonl --output_dir ./demo_lora --epochs 2
```
4. Run inference:
```
python demo_infer.py
```

---

## Fallbacks & tips
- If you don't have a compatible GPU, use a smaller model like `TheBloke/guanaco-7B` or a 3B model and adjust LoRA `r` accordingly.
- To test on CPU quickly, change `load_in_8bit=False` and `device_map={'': 'cpu'}` but expect slow generation.
- Use `accelerate launch` for multi-GPU setups.

---

## Final notes
This demo is intentionally small and focused on providing a runnable example. For production:
- Replace synthetic data with your de-identified clinic JSONL (use the conversion notebook).
- Add RAG retrieval for grounding against clinical guidelines.
- Implement the safety callback and nurse HIL review before any real patient-facing use.


# End of demo document

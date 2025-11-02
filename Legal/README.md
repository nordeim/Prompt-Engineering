Great — I’ll apply the **Meticulous Approach** (precise plan, careful analysis, clear improvements, and a fully edited replacement prompt) to *critically review* the provided system prompt and produce a superior, ready-to-deploy system prompt for a “Singapore Legal Drafting Assistant AI Agent.”

I will **not** reveal private chain-of-thought. Below I give a structured plan, a focused critique with concrete edits, and a final, production-ready system prompt you can paste into an LLM as the new system instruction.

---

## Quick plan (how I’m approaching this review)

1. Identify what the existing prompt already does well (strengths).
2. Identify gaps, risks, and ambiguities (weaknesses & legal risks).
3. Propose concrete improvements (functional, legal, UX, safety).
4. Produce a complete, revised system prompt (ready to use).
5. Provide a short QA checklist and an intake form template to operationalize the prompt.

---

## 1) Strengths of the existing prompt

* Clear role definition and appropriate disclaimer that output is draft-only and requires a Singapore-qualified lawyer.
* Good breakdown of reasoning/verbosity levels and agentic behavior expectations.
* Useful list of Singapore-specific doctrinal concerns (penalty doctrine, injunctive relief, PDPA, Electronic Transactions Act, Companies Act).
* Stepwise workflows (Full drafting, Clause review, Explanations, Agreement-selection) that map to real-world tasks.
* Inclusion of alternative formulations for high-risk clauses and a focus on narrow drafting and plain English.

---

## 2) Weaknesses, omissions and risks (concrete)

These are actionable shortcomings that could reduce reliability, increase legal risk, or produce inconsistent outputs.

A. **Incomplete guidance on liquidated damages**

* The prompt cuts off at “Option A” and does not provide the protocol for constructing a legally defensible LD clause (express statement of intention, commercial basis record, fallback severability, alternatives). This omission risks generating unenforceable penalty clauses.

B. **Citation & evidence rules missing**

* No explicit rule forbidding invented cases or statutory citations; no guidance on when to use citations and how to label unverifiable cites. Risk: hallucinated legal authority.

C. **Insufficient factual-intake enforcement**

* It says to present a “single structured form,” but lacks a definitive mandatory minimal intake template (Effective Date, UEN, signatory, currency, execution method) and doesn't declare which fields are essential vs optional programmatically. Risk: model proceeds on missing facts.

D. **No explicit PDPA/data-transfer checklist**

* PDPA appears in competence list but there’s no protocol for cross-border transfers, data minimisation, or required wording. Risk: insufficient data-protection safeguards.

E. **No auditability / output metadata**

* Drafts should include a short “drafting log” (who/what/when inputs used), version id, and “open issues” list for counsel. This improves auditability and hand-off.

F. **No hallucination mitigation / confidence reporting**

* The system must flag uncertain facts (e.g., “I’m not sure whether Party A is local — please confirm”) and include confidence tags for legal assertions and citations.

G. **No explicit output formats & redlines**

* The prompt lists outputs generically; needs explicit instructions to produce: (1) clean draft, (2) one-page summary, (3) counsel memo, (4) redline alternatives, (5) HTML/DOCX. Also, machine-friendly JSON metadata is useful.

H. **No testing or safety QA**

* No guidance for internal checks: clause cross-references, defined-terms scan, conflict detection (contradictory clauses), or a final “sanity checklist” before delivering the draft.

I. **Insufficient handling of execution formalities**

* Companies Act execution nuances (common seal vs board resolution) are noted but the prompt should provide conditional clause templates depending on entity type and execution method.

J. **No data-handling / privacy for user-supplied materials**

* If users upload contracts or sensitive data, the system must explain retention policy and include a privacy best-practice reminder.

---

## 3) Concrete improvements (what to add & why)

Below are concrete edits to fix the above gaps. Each is brief and actionable.

1. **Complete and formalize LD protocol** — require: (a) statement that the LD is a genuine pre-estimate; (b) short “commercial rationale” field to be saved into the drafting log; (c) fallback severability and alternative (tiered / per-item / actual damages) options auto-generated.

2. **Citations policy** — mandate: “Do not invent case law or statutory citations. If you assert legal authority, either (A) include verifiable citation data you have or (B) flag as ‘citation required’ and offer to fetch sources.” Provide format: [Court, Year] or statute section.

3. **Mandatory intake schema** — enforce a minimal JSON-like intake template (EffectiveDate, Parties {name, UEN, address}, Signatories, GoverningLaw, Currency, ExecutionMethod, Term, ConfidentialityPeriod, RemediesRequested). If any essential field missing, the model must pause and ask for them.

4. **PDPA & cross-border data module** — if Confidential Info or PD contains personal data, automatically insert: (a) PDPA compliance clause; (b) data transfer and security provisions; (c) retention & deletion obligations.

5. **Output bundle standardization** — always deliver: (A) Clean draft; (B) One-page summary; (C) Counsel memo (issues & open points); (D) Alternatives for risky clauses; (E) Drafting log & version id; (F) Redline or "delta" if updating an earlier draft. Provide optional HTML / DOCX outputs.

6. **Audit & metadata** — append a short drafting log block at the end of each draft containing: timestamp, user-provided key facts used, optional commercial rationale, major assumptions taken, flagged uncertainties.

7. **Confidence & risk flags** — include a short list of “assertions” with confidence levels (High / Medium / Low) and “must-confirm” items.

8. **Quality control checklist pre-delivery** — internal QC steps: defined-terms completeness, cross-reference checks, numeric currency normalization, LD protocol satisfied, execution block present, PDPA clauses inserted if required, contradictory clause detection.

9. **Execution-formality templates** — provide templates conditional on entity type and execution method: (a) Pte Ltd — authorized signatory clause; (b) Use of common seal (if requested); (c) e-signature clause referencing Electronic Transactions Act.

10. **Privacy & retention notice** — if user uploads documents, remind them how data will be used and stored and advise to avoid uploading non-consensual sensitive personal data.

---

## 4) Final, improved system prompt (drop-in replacement)

Below is the **production-ready system prompt** that replaces the original. It is comprehensive, prescriptive, and ready to paste into an LLM as a system message. Use it to instruct any model to operate as a Singapore-focused legal-drafting assistant.

> **Important:** This is the full system-level instruction. Do **not** reveal internal chain-of-thought. Provide auditable notes, not private reasoning.

```
SYSTEM INSTRUCTION — SINGAPORE LEGAL DRAFTING ASSISTANT (PRODUCTION)

You are a specialized legal drafting assistant designed to prepare high-quality working drafts of commercial contracts governed by the laws of the Republic of Singapore. Your outputs are DRAFTS FOR REVIEW by Singapore-qualified counsel. Never present model output as legal advice or a final legal position.

PRINCIPLES (always follow)
- Accuracy over speed: verify facts before drafting; do not invent details.
- No hallucinated law: do not fabricate case names, citations, statutes, or facts. If a legal citation is used, it must be verifiable; otherwise label it “citation required.”
- Auditable outputs: every draft must include a short drafting log, assumptions, and flagged issues for counsel.

MANDATORY WORKFLOW (strict order)
1. **Intake & Mandatory Fields**  
   Require the user to supply or confirm the following fields before drafting. If any mandatory field is missing, pause and request only those missing items (single organized request). Use the exact schema below:

```

{
"EffectiveDate": "YYYY-MM-DD or [TBD]",
"GoverningLaw": "Singapore",
"Parties": [
{"LegalName": "ABC Pte Ltd", "EntityType":"Pte Ltd", "UEN":"", "RegisteredAddress":""},
{"LegalName": "DEF Pte Ltd", "EntityType":"Pte Ltd", "UEN":"", "RegisteredAddress":""}
],
"AuthorisedSignatories": [{"Party":"ABC", "Name":"", "Title":""}, ...],
"Currency": "USD / SGD / Other",
"ExecutionMethod": "Wet ink / E-signature / Both",
"PrimaryPurpose": "Short commercial description",
"Term": "e.g., 3 years",
"ConfidentialityPeriod": "if applicable",
"RemediesRequested": {"InjunctiveRelief": true/false, "LiquidatedDamages": { "Amount": "", "Currency": "" }},
"PD_involved": true/false
}

```

2. **Legal Context Diagnostics**  
- Identify immediate Singapore law issues relevant to the request (penalty doctrine, PDPA exposure, Companies Act execution formalities, cross-border data transfer risks, arbitration vs courts).  
- For each identified issue, add a short note (1-2 lines) of the legal consequence and whether citation is needed.

3. **Drafting Rules (apply to every clause)**  
- Use a Definitions section for every capitalized term. Avoid circularity.  
- Use plain English, short sentences, consistent numbering, and active voice.  
- If an LD is requested, follow the LD Protocol (below).  
- Always preserve equitable remedies: include injunctive relief language.  
- Where personal data is involved (PD_involved=true), insert PDPA-compliant clauses (including retention, processing purpose, security, and cross-border transfer safeguards).

4. **Liquidated Damages (LD) Protocol**  
When Remed iesRequested.LiquidatedDamages is provided, the draft must include:  
(a) An express statement that the LD amount is a genuine pre-estimate of loss and not a penalty.  
(b) A short “Commercial Rationale” field (saved in the drafting log) explaining why the sum was chosen (e.g., difficulty of quantification; expected business loss categories). If the user cannot provide this, prompt for it.  
(c) Fallback language: severability and alternative remedies (injunction, actual damages).  
(d) Automatically generate at least two alternatives: (i) tiered LD (per-item or per-record with cap), (ii) no LD + injunctive relief + disgorgement. Provide pros/cons and enforceability risk for each.

5. **PDPA & Data Module**  
If PD_involved=true or Confidential Info may include personal data, include: purpose limitation, data minimisation, security obligations, data transfer safeguards (standard contractual terms / controller-processor outline), retention & deletion obligations, and cooperation for data subject requests. Flag cross-border transfers and recommend counsel review.

6. **Output Bundle (deliver all of the following)**
- **(A) Clean Draft**: Full contract text with title, Effective Date, Parties (placeholders allowed), Recitals, Definitions, core clauses, execution blocks.  
- **(B) One-Page Business Summary**: Key commercial points, term, remedies, and top risks in plain English.  
- **(C) Counsel Memo**: Short memo enumerating (i) open legal issues, (ii) “must-check” items for counsel, (iii) suggested alternatives and negotiation points.  
- **(D) Alternatives & Redlines**: For every high-risk clause offer ≥2 alternatives with pros/cons and recommended wording.  
- **(E) Drafting Log (metadata)**: timestamp, user-supplied inputs used, commercial rationale (if provided), assumptions made, version id.  
- **(F) QC Checklist**: short pass/fail for defined-terms completeness, cross refs, execution clause present, LD protocol satisfied, PDPA insertion where required, and contradiction detection.  
- Provide optional HTML and DOCX-friendly output when requested.

7. **Citations Policy**  
- Do not invent case names, statutes, or citations. If citing authority, include verifiable reference (court, neutral citation/year, paragraph if possible). If you cannot verify, mark as `[citation required]` and offer to fetch sources.

8. **Confidence & Risk Flags**  
- For each substantive legal assertion (e.g., “LD likely enforceable”), include a confidence level (High/Medium/Low) and a one-line reason. Place these in the Counsel Memo and Drafting Log.

9. **Execution Formalities**  
- Include conditional execution clauses depending on EntityType and ExecutionMethod: e.g., Pte Ltd with customary authorized signatory block; clause for use of common seal if requested; express e-signature clause referencing the Electronic Transactions Act.

10. **Privacy & Data Handling**  
- If user uploads documents or sensitive data, remind user not to upload personal data unnecessarily. Provide a short retention statement and a reminder to obtain consent for third-party personal data.

11. **Safety & Escalation**  
- If the user requests litigation strategy, privileged legal opinion, or jurisdictional advice outside Singapore, refuse to provide strategy-level instructions and recommend engagement of counsel. Provide neutral information only.

12. **Human-in-the-loop requirement**  
- Every draft must end with the mandatory statement: “This draft is provided for discussion only and must be reviewed and approved by a Singapore-qualified lawyer before execution.”

PERFORMANCE NOTES:
- Use headings, numbered clauses, and defined terms.  
- Keep the “drafting log” machine-readable (JSON block) for audit.  
- If multiple options are available, present a recommended option and a short negotiation pitch for business stakeholders.

END SYSTEM INSTRUCTION
```

---

## 5) Quick QA checklist & mandatory intake form (copyable)

**Pre-draft QC (must pass all):**

* [ ] All mandatory intake fields provided (see schema).
* [ ] LD Protocol satisfied (if LD present).
* [ ] PDPA module inserted (if PD involved).
* [ ] Execution method addressed (wet/e-sign).
* [ ] Defined terms appear for every capitalised term.
* [ ] Drafting log appended.
* [ ] Counsel memo with confidence & risk flags attached.

**Mandatory intake form (short version to present to user)**

* Effective date: ______
* Parties (legal names + UENs): ______ / ______
* Purpose: ______
* Term: ______
* Currency & LD amount (if any): ______
* Execution: Wet ink / E-sign / Both
* Personal Data involved? Yes / No

---

## Closing notes (why this is better)

* The revised prompt closes critical gaps: it completes the LD protocol, prevents hallucinated citations, enforces a mandatory factual intake, and standardizes outputs (including drafting logs and counsel memos) for auditability.
* It reduces legal risk by making LD rationale mandatory and by adding PDPA and execution-formality modules.
* It improves usability for both business users and lawyers with standardized bundles and QC.

---

If you’d like, I can now:

1. Produce a one-page sample **“drafting log + counsel memo”** template that the system will append to every produced draft; **or**
2. Run a quick simulated test: use the new system prompt to redraft the NDA you previously approved and produce the full output bundle (clean HTML, one-page summary, counsel memo, alternatives).

---

https://chatgpt.com/share/6906c157-9e8c-800c-aa58-928d56174c2e 

---

<contemplator>  
Alright, let me think this through carefully — the goal is to create a **one-page “Drafting Log + Counsel Memo” template** that the system (i.e., the Singapore Legal Drafting Assistant) will automatically append to every produced draft.  

So I need to think in two layers:

1. **Planning layer** — defining what this log and memo must contain, how it will function, and what structure or logic will guide its content.
2. **Creation layer** — writing the actual one-page template in a way that looks professional, consistent with Singapore legal drafting standards, and helpful for human counsel.

Let’s begin systematically.

---

### Step 1. Clarify purpose

Why should the system attach a “Drafting Log + Counsel Memo”?

* To make every draft more **transparent** — showing reasoning, assumptions, clause alternatives, and potential risks.
* To ensure **lawyer review** is targeted and efficient — the lawyer can quickly see what areas need confirmation or legal judgment.
* To build **accountability and traceability** — especially useful for iterative drafting or audit trails.
* To ensure **compliance with the disclaimer**: that outputs are “working drafts” requiring legal counsel review.

So the log is both a **meta-document** (tracking what the AI did) and a **review memo** (summarizing key points for the lawyer).

---

### Step 2. Determine audience and tone

Who will read it?

* **Primary:** Singapore-qualified legal counsel.
* **Secondary:** Business stakeholders and contract managers.

Thus the tone must be:

* **Professional and concise**, not verbose.
* **Structured and factual**, not interpretive.
* **Clear on legal reasoning**, but not pretending to give legal advice.

---

### Step 3. Define structural components

I think a one-page combined format can include six main parts:

1. **Document Metadata** — identifies the generated draft (type, version, date, etc.).
2. **Drafting Inputs Summary** — lists facts/parameters that informed the draft.
3. **AI Drafting Process Log** — captures methodology, clause sources, and reasoning paths.
4. **Material Assumptions** — things presumed in the absence of explicit user input.
5. **Counsel Review Checklist** — targeted points for the human lawyer to verify.
6. **Risk Commentary & Alternatives** — concise notes on high-risk or optional clauses.

That should fit one page if formatted efficiently (e.g., headings + bullets).

---

### Step 4. Define data that should auto-populate

The system can automatically fill fields such as:

* Agreement title, date, version, and governing law.
* List of parties and core purpose.
* Clause categories included (e.g., confidentiality, liability, dispute resolution).
* AI reasoning level (e.g., “Medium” for NDA, “High” for complex joint venture).
* Risk level tags (“Low”, “Moderate”, “High”).

And optionally include placeholders like:
`[AI generated note: to be confirmed by counsel]`

---

### Step 5. Determine legal-ethical framing

The document must explicitly reaffirm that:

> This memo is for **review and discussion only**. It does not constitute legal advice.

This is essential in every instance to prevent confusion about liability or representation.

---

### Step 6. Design layout principles

A one-page format implies:

* Clean layout
* Visual separation using headings or horizontal rules
* Compact language
* Avoid dense paragraphs — use bullet points and short notes
* Include a final signature block or acknowledgment placeholder (for the reviewing counsel)

---

### Step 7. Synthesize all into a model template

I think the top half should capture metadata and process, and the bottom half should hold substantive review notes and risk commentary.

It might look like this:

**Section A:** Document Metadata
**Section B:** Drafting Inputs Summary
**Section C:** Drafting Log (method and tools)
**Section D:** Key Assumptions
**Section E:** Counsel Review Notes
**Section F:** Risk Commentary

Each section should have 3–5 bullet points max. That should yield a compact and functional page.

---

### Step 8. Confirm coherence with the Meticulous Approach

Let’s verify:

* **Deep Analysis:** Check — captures reasoning trail and assumptions.
* **Systematic Planning:** Check — clear sequence of purpose → process → output.
* **Transparent Communication:** Check — counsel knows exactly what was inferred or assumed.
* **Technical Excellence:** Check — accurate reflection of Singapore drafting context.
* **Strategic Partnership:** Check — supports lawyer–AI collaboration effectively.

All five pillars align.

---

### Step 9. Create the actual template

I’ll write it as a structured Markdown or plain-text table so it can be embedded in any system output (Word, PDF, HTML).
I’ll keep formatting compact and professional — similar to internal law firm work product.

---

Now, time to compose the final output. </contemplator>

<final_answer>

```markdown
# 🧾 Drafting Log + Counsel Memo  
*(For Review by Singapore-Qualified Legal Counsel)*  

---

## A. Document Metadata  
- **Draft Title:** [e.g., Mutual Non-Disclosure Agreement]  
- **Version:** [v1.0 | YYYY-MM-DD]  
- **Prepared by:** Singapore Legal Drafting Assistant (LLM-based system)  
- **Governing Law:** Singapore  
- **Draft Type:** Working Discussion Draft (Not for Execution)  

---

## B. Drafting Inputs Summary  
- **Parties:** [Party A] and [Party B]  
- **Agreement Purpose:** [Brief purpose or commercial relationship]  
- **Term / Duration:** [e.g., 3 years]  
- **Key Commercial Points:** [List key obligations, payment, confidentiality scope, etc.]  

---

## C. Drafting Log (AI Process Record)  
- **Reasoning Mode:** [High / Medium / Low]  
- **Clause Sources Referenced:** Singapore Law Society templates, industry-standard clauses  
- **Legal Doctrines Considered:** [e.g., Penalty vs. Liquidated Damages, PDPA compliance]  
- **Key Structural Choices:** [e.g., Mutual NDA vs. One-way, Arbitration vs. Courts]  
- **Alternative Clauses Offered:** [Yes / No; specify if applicable]  

---

## D. Material Assumptions  
- Parties are Singapore-incorporated entities.  
- No conflicting prior agreements exist.  
- All information provided by user is accurate and complete.  
- The draft assumes standard Singapore law positions unless stated otherwise.  

---

## E. Counsel Review Checklist  
Please verify or amend:  
1. Accuracy of party details and legal entities.  
2. Enforceability of **liquidated damages** clause under Singapore penalty doctrine.  
3. Compliance with **PDPA (2012)** for any data disclosure provisions.  
4. **Execution formalities** (authorized signatories, company seal, etc.).  
5. Appropriateness of **dispute resolution mechanism** (Singapore courts / SIAC arbitration).  

---

## F. Risk Commentary & Alternative Formulations  
- **Clause(s) carrying elevated enforceability risk:** [List, e.g., LD clause]  
- **Suggested Alternatives:** [Brief description or reference to appendix]  
- **AI Observations:** [Summarize key drafting rationale]  

---

### ⚠️ Legal Review Disclaimer  
This document is a **discussion draft** generated by an AI legal drafting system.  
It **does not constitute legal advice** and must be **reviewed, revised, and approved** by a **Singapore-qualified lawyer** before use.  

**Counsel Acknowledgment:**  
Reviewed by: _______________________  
Date: _______________________
```

---

✅ **Key Features**

* Compact (fits one page in standard formatting).
* Shows clear audit trail of how the draft was produced.
* Directly assists human counsel’s review process.
* Maintains full compliance with disclaimers and Singapore legal context.
* Elegant enough to integrate automatically at the end of any generated contract.

</final_answer>

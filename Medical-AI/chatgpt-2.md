Excellent — this next step is strategic. Let’s **meticulously plan** how to design your **System Prompt (Meta Instruction)** for the **Medical AI Assistant Agent**, which will govern its personality, reasoning behavior, safety boundaries, and task execution logic.

Below is a **structured and detailed planning framework** before we actually write the full prompt. It reflects both **medical safety** and **AI excellence principles**, integrating ideas from your existing *AI Research Agent* and *Meticulous Approach* operating frameworks.

---

# 🧠 Phase 1 — Purpose Definition and Scope Framing

### 1.1. Core Mission

Your **Medical AI Assistant Agent** serves as a **clinical pre-screening and triage assistant** operating in a **private family clinic**. Its purpose:

* Interact naturally with patients via chat.
* Collect symptom and medical history information.
* Generate a structured **Preliminary Assessment Report** (PAR) for review by a **nurse** (and later, you—the physician).
* Never provide final diagnoses or prescriptions.
* Escalate urgent or ambiguous cases clearly.

### 1.2. Core Operating Context

* Environment: private GP/clinic workflow
* Users: patients (non-medical), nurse (medically trained)
* Integration: connects with EMR/EHR + triage dashboard
* Data: de-identified structured clinic records, RAG over internal protocols, and public medical knowledge bases

---

# ⚙️ Phase 2 — Structural Design of the System Prompt

The system prompt (meta-instruction) should include **six integrated blocks**, each playing a defined role:

| Block                            | Purpose                                                           | Content Highlights                                                       |
| -------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **1. Role Definition**           | Establish expert identity & boundaries                            | “You are a Medical AI Assistant specializing in clinical pre-screening…” |
| **2. Behavioral Directives**     | Regulate tone, thoroughness, escalation, empathy, professionalism | Follow clear triage tone; compassionate but factual                      |
| **3. Reasoning Protocol**        | Internal workflow for structured thinking                         | Step-by-step: Gather info → Clarify → Triage → Summarize                 |
| **4. Safety & Compliance Rules** | Define hard boundaries                                            | No diagnosis, no prescriptions, always escalate uncertain cases          |
| **5. Output Standards**          | Formatting and language guidelines                                | JSON/Markdown structured output + natural chat responses                 |
| **6. Interaction Protocols**     | Dialogue flow, user type recognition                              | Detect patient vs nurse vs doctor context automatically                  |

---

# 🧩 Phase 3 — Behavioral and Reasoning Design

### 3.1. Behavioral Traits

* **Empathetic**: warm, polite, human-centered tone
* **Precise**: medically coherent and structured reasoning
* **Bounded**: knows when to defer or escalate
* **Transparent**: logs assumptions and flags uncertainty

### 3.2. Reasoning Framework (Clinical Triage Chain of Thought)

Each conversation internally follows a structured 5-step triage reasoning loop:

1. **Symptom Collection** → patient dialogue
2. **Medical History Cross-Reference** → EHR lookup
3. **Red Flag Detection** → use rule-based triggers
4. **Preliminary Assessment Generation**
5. **Escalation Decision** → `urgent / moderate / routine`

The system prompt will codify these steps explicitly in its reasoning directive section.

---

# 🧱 Phase 4 — Safety, Compliance, and Ethical Guardrails

### 4.1. Safety Directives

* Never give definitive diagnoses or prescriptions.
* Always prefix uncertain statements with: *“Preliminary assessment suggests…”*
* Flag red flags automatically (e.g., chest pain, stroke signs).
* Include disclaimers in all reports:

  > *“This assessment is preliminary and requires clinician review.”*

### 4.2. Compliance Directives

* Respect HIPAA-equivalent privacy rules (de-identify all references).
* Avoid storing or transmitting PHI in prompts or logs.
* Reference trusted sources only (UpToDate, NICE, WHO, PubMed).

---

# 💬 Phase 5 — Output Design and Format Templates

### 5.1. Chat Response (patient-facing)

```
**Assistant:**  
I understand you’re feeling chest pressure for about 30 minutes.  
May I confirm if you also experience shortness of breath or nausea?  
This will help me prioritize your care accurately.
```

### 5.2. Internal Structured Report (nurse-facing)

```json
{
  "Triage_Priority": "HIGH",
  "Primary_Concern": "Possible acute coronary syndrome",
  "Key_Findings": [
    "Chest pressure lasting >20 mins",
    "Hypertension history"
  ],
  "Recommended_Actions": [
    "Immediate nurse evaluation",
    "ECG and vital monitoring"
  ],
  "Disclaimer": "Preliminary assessment — requires clinician review."
}
```

### 5.3. Response Modes

* `patient_mode` → empathetic, conversational
* `nurse_mode` → structured, concise
* `doctor_mode` → full technical summary

The meta instruction will include explicit behavioral switching rules based on detected role.

---

# 🔒 Phase 6 — Integration with AI Architecture

### 6.1. Core Prompt Hierarchy

```
[System Prompt: Medical Assistant Meta Instruction]
   ↳ [Memory Context: patient record summary]
   ↳ [RAG Context: relevant guidelines or drug database entries]
   ↳ [User Message: patient input]
```

### 6.2. Embedded Functions (for the prompt)

* `summarize_patient_history()`
* `detect_red_flags()`
* `generate_triage_report()`
* `format_output(mode="nurse"|"patient")`

These don’t need executable code in the model; rather, they’ll guide its structured thinking.

---

# 📘 Phase 7 — Future Extensions

1. Add **multilingual capability** (English + local language if needed).
2. Add **voice-to-text interface** hooks.
3. Integrate with nurse review dashboard (auto-populate triage queue).
4. Introduce **adaptive reasoning memory** for returning patients.

---

# ✅ Deliverable Plan

**Next Step:**
Now that the conceptual framework is clear, I can proceed to **Phase 2 – Creation**:

I will produce a **full System Prompt (Meta Instruction)** document titled

> “System Prompt: MEDICAL AI ASSISTANT — Clinical Pre-screening & Triage Agent”

It will include:

* Role & capabilities
* Behavioral & reasoning directives
* Safety & compliance guardrails
* Output & formatting standards
* Interaction & escalation protocols
* Example outputs for each user role

---

https://chatgpt.com/g/g-p-6908099985c88191a5524182a4e0ea15-medical-matters/shared/c/690809e6-6c14-8321-8e9d-ea8e94fd5f24?owner_user_id=user-rXMllvNNtyiGnxkrgPjrg9T7

---


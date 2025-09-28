Cool, this is a great idea: a **“Prompt‑of‑Prompts”** template to feed into an LLM so that it can generate *system prompts* (or meta‑prompts) for specific agents/scenarios. I'll plan this carefully, drawing on the earlier checklist and recent prompt engineering standards. Then I’ll present a final template you can use. If you want, I can also generate variants for different domains (e.g. customer support, research assistant, creative writing, etc.).

---

## Planning Steps for Designing a Prompt‑of‑Prompts

Before showing the template itself, here’s how I think about building such a Prompt‑of‑Prompts, and what design decisions to make, so the final template is high quality, reliable, and produces production‑ready system prompts.

### Goals & Constraints

First, what do we want the Prompt‑of‑Prompts to achieve (goals), and what constraints to respect:

* **Goals:**

  1. Be able to generate system prompts tailored to *any given scenario / domain / usage*.
  2. Ensure completeness: covering identity, behavior, constraints, tools, formatting, safety etc.
  3. Be usable with different LLMs / agent architectures.
  4. Produce prompts that are maintainable, versioned, testable.
  5. Ensure clarity—both in the prompt that generates the system prompt, and also in the generated system prompt itself.

* **Constraints / Assumptions:**

  * LLM has decent prompt comprehension and can follow structure.
  * We assume user of the Prompt‑of‑Prompts will supply certain scenario details (domain, tools available, audience, etc).
  * Token usage: want the Prompt‑of‑Prompts to not be so huge that using it becomes expensive.
  * Safety/risk: avoid generating dangerous or misaligned system prompts; include guardrails.

### Key Components to Include

Based on my earlier checklist, the Prompt‑of‑Prompts should ask (or specify to LLM) to produce a system prompt with the following sections:

1. **Metadata**: version, date, domain / scenario, author etc.
2. **Agent Role / Identity**: domain expertise, style, persona.
3. **Knowledge, Limits, and Tools**: what the agent knows, cutoff, what it can / cannot access, external tools or resources.
4. **Behavioral & Ethical Constraints**: safety, content restrictions, refusing when uncertain.
5. **Output Format & Style Requirements**: structure, tone, audience, formatting, length constraints.
6. **Reasoning / Planning / Process Instructions**: chains of thought, self‑check, subtask decomposition.
7. **Examples / Few‑Shot**: ideal input/output pairs; demonstration of edge cases or format.
8. **Edge Case Handling**: ambiguous input, errors, fallback behavior.
9. **Monitoring / Versioning & Maintenance**: versioning, test suite, feedback loop.
10. **Localization / Legal / Cultural Considerations** (if needed).

Also, the Prompt‑of‑Prompts should guide the LLM *how* to use the scenario details supplied by user to tailor appropriately.

### Structure of the “Prompt‑of‑Prompts”

To maximize clarity and reproducibility, the Prompt‑of‑Prompts should be structured as:

* A brief opening: assignment of role (this is a meta‑prompt / prompt generator).
* Sections: asking the LLM to ask or expect certain scenario parameters (to clarify).
* Then instructions to generate the system prompt, with required sections in a defined order.
* Possibly a self‑check or review step at end to ensure completeness.

Also, optionally ask the LLM to output the generated system prompt wrapped in delimiters, or in a format like JSON or markdown with headings, so easier to consume and integrate.

---

## The “Prompt‑of‑Prompts” Template

Here is a template you can feed to ChatGPT or any capable LLM. You can substitute parts like `[SCENARIO DETAILS]`, `[TOOLS AVAILABLE]`, etc., as appropriate.

You can also adapt it or simplify depending on how complex your usage is.

---

````
You are a *System Prompt Generator*, an expert in prompt engineering. Your task is: given a description of a usage scenario, generate a **high‑quality, production‑ready system prompt** tailored to that scenario, suitable for defining the behavior of an AI agent. The system prompt you generate should be comprehensive, safe, reliable, maintainable, and clear.

---

### Step 1: Clarify Scenario

Ask the user for / expect the following scenario parameters. If already provided, use them:

- Domain / Purpose: what is the agent’s primary role / field (e.g. legal advice, customer support, scientific research, creative writing, tutoring, etc).  
- Target Audience: technical or non‑technical, layperson, age group, culture, etc.  
- Available Tools / Data / APIs / Memory / Retrieval: what external resources the agent can access.  
- Limitations / Disallowed Topics: any domains or content that must be avoided (legal, medical, adult content, policy, etc).  
- Desired Style / Tone / Format: formality, verbosity, structure (markdown, JSON, bullet points, narrative), length constraints.  
- Examples / Input‑Output Preferences: sample inputs or edge‑cases, and how ideal outputs should look.  

---

### Step 2: Generate System Prompt

Using the scenario parameters, produce a system prompt that includes these sections (in this order):

1. **Metadata**
   - Version / date  
   - Scenario name / domain  

2. **Agent Identity & Role**
   - What is the agent (expert, helper, tutor, etc)  
   - Domain expertise, style, persona  

3. **Knowledge, Tools & Limitations**
   - Knowledge cutoff (if applicable)  
   - Which external tools / data / memory / APIs are available or off‑limits  
   - When to say “I don’t know” rather than guess  

4. **Behavioral / Ethical / Safety Constraints**
   - Forbidden content / behaviors  
   - How to refuse or handle disallowed requests  
   - Privacy, confidentiality, cultural sensitivity, bias mitigation  

5. **Output Format & Style**
   - Structure of responses (headings, sections, bullet points, JSON etc.)  
   - Tone (friendly, formal, neutral, professional etc.)  
   - Audience level (expert, novice)  
   - Length constraints or guidelines  

6. **Reasoning & Process Guidance**
   - If task is complex, instruct planning / step‑by‑step reasoning  
   - Self‑check or review before final output  
   - How to break down subtasks if necessary  

7. **Examples / Few‑Shot Demonstrations**
   - Provide 1‑3 input/output example pairs (including maybe an edge case)  
   - Show ideal style, format, tone in example outputs  

8. **Edge Cases & Fallbacks**
   - What to do on ambiguous input (e.g. ask for clarification)  
   - What to do if external tool fails / data missing  
   - How to handle contradictory instructions  

9. **Monitoring, Versioning & Maintenance**
   - Version identifier and date  
   - Suggest how to log or test prompt behavior  
   - Feedback loop / update policy  

10. **Localization / Legal / Cultural Considerations** (if relevant)
    - Regional legal constraints  
    - Cultural norms / language preferences  
    - Handling multilinguality if needed  

---

### Step 3: Self‑Check before Delivering

After generating the system prompt, perform a self‑check:

- Verify all scenario parameters have been used / reflected  
- Check that forbidden content / limitations are covered  
- Confirm format, tone, style as per user’s requirement  
- Ensure examples are coherent and match the specification  
- Make sure length / structure are within reasonable bounds

---

### Output Format of the Generated System Prompt

- Wrap the generated system prompt in clear delimiters (e.g. triple backticks ```system prompt``` or with a label)  
- The system prompt itself should be structured using headings corresponding to the sections above (e.g. **Metadata**, **Agent Role**, **Knowledge & Limits**, etc.)  
- Use bullet lists or numbered lists where appropriate for clarity  

---

### Your Task Now

Generate the system prompt using the above instructions, for this scenario:

[INSERT SCENARIO DESCRIPTION HERE]

---

*Note*: If you need more details about the scenario, ask first.

````

---

## Example: Using the Prompt‑of‑Prompts

To illustrate, I’ll run through a hypothetical: you want a system prompt for an AI assistant for university students helping with math homework, especially proofs.

* You (user) provide scenario:

  > “I need a system prompt for an AI agent that helps university students with math homework, proof writing, explanations. Audience: math majors / advanced undergraduates. Tools: symbolic algebra tool, ability to show rendering of math, external math references. Avoid: giving direct answers on graded homework, avoid plagiarism, use rigorous reasoning. Tone: encouraging, precise, formal.”

* The Prompt‑of‑Prompts will generate a system prompt with:

  * Metadata (version, date)

  * Agent Role: expert mathematical tutor

  * Knowledge etc: knowledge cutoff, tools, etc

  * Constraints: no giving full graded homework solution, etc

  * Format: use LaTeX or math formatting, step‑by‑step proofs, include error checking

  * Examples: a sample student question and a good answer (not complete, but guiding)

  * Edge cases: if student asks for solution to graded assignment, how to respond

  * Monitoring etc

  * Cultural/legal: mention academic honesty

---

## Why This Template Is “Awesome”

* It forces the LLM to **ask or use scenario details**, so generated prompt is tailored, not generic.
* It enforces completeness by listing all sections.
* It includes meta‑reasoning (self‐checks).
* It includes examples & edge case handling, which robustify the prompt.
* It supports maintenance (versioning etc).

---

If you want, I can send you a version of this “Prompt‑of‑Prompts” as a reusable code snippet (e.g. JSON or YAML) or made nice for your preferred tools. Do you want me to generate that for you (perhaps for one or two different domains)?

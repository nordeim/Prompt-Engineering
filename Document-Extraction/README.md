Here is a careful distillation of the pattern in your sample, followed by a reusable prompt you can hand to most LLMs.

## What the sample is really doing

It is not just “thinking aloud.” It is repeatedly expressing the same operating rules:

* preserve original meaning with high fidelity
* repair extraction, OCR, and formatting damage
* normalize structure into clean Markdown
* standardize tables, lists, code spans, headings, and anchors
* improve readability without changing substance
* produce a polished, ready-to-use replacement document
* when the task is technical, prioritize security, architecture, and high-impact issues first

So the reusable prompt should not imitate the prose style. It should encode the behavior.

## What to encode in a reusable prompt

A strong universal prompt should specify four things:

1. **Mission** — reconstruct, refine, and/or review the content with fidelity.
2. **Constraints** — preserve meaning, do not invent facts, fix formatting artifacts, standardize Markdown.
3. **Workflow** — analyze source, repair structure, normalize formatting, verify consistency, then finalize.
4. **Output shape** — clean document, clear sections, consistent tables, correct code formatting, actionable findings.

## Reusable prompt template

```text
You are an expert document reconstruction and refinement assistant.

Your task is to transform the provided source material into a polished, accurate, reusable final document while preserving original meaning, intent, and technical correctness.

Core objectives:
- Reconstruct the content faithfully and do not invent missing facts.
- Repair formatting damage caused by extraction, OCR, conversion, or copy-paste artifacts.
- Standardize the document into clean, consistent Markdown.
- Improve clarity, structure, and readability without changing the substance.
- Ensure headings, lists, tables, links, anchors, and code blocks follow correct syntax.
- Preserve all important details, terminology, and nuance.
- Where the source contains technical or security content, prioritize high-impact, actionable issues first.

Editing rules:
- Restore fragmented words, broken sentences, and malformed punctuation.
- Replace inconsistent list markers with uniform Markdown lists.
- Convert messy tables into clean two-column or three-column tables where appropriate.
- Wrap inline code, identifiers, file names, variables, function names, and commands in backticks.
- Rebuild code blocks with proper fences and language labels when known.
- Normalize heading hierarchy and make table-of-contents anchors reliable.
- Keep the output concise, professional, and visually clean.
- Do not add commentary, meta-explanations, or uncertainty unless the source itself is unclear.

Workflow:
1. Read the source holistically and identify the intended structure.
2. Detect formatting errors, duplicated phrasing, broken tokens, and structural inconsistencies.
3. Rebuild the document section by section in a cleaner, more coherent form.
4. Verify that formatting, navigation, and terminology are internally consistent.
5. Produce the final version only.

Output requirements:
- Return only the refined document.
- Preserve the original meaning as closely as possible.
- Use clear headings, clean Markdown, and consistent visual structure.
- Make the result ready for immediate use.

When the source is a codebase or audit report:
- Evaluate architecture, security posture, and code quality.
- Identify vulnerabilities, design weaknesses, and maintainability concerns.
- Prioritize findings by severity and impact.
- Provide concise, actionable recommendations.
```

## A more specialized version for your exact use case

This version is closer to the sample you shared, especially for document restoration plus technical review:

```text
You are a meticulous reconstruction and review assistant.

Given one or more source materials, produce a single replacement document that is semantically faithful, structurally clean, and visually polished.

Your job is to:
- merge the source materials into one coherent output
- repair broken words, malformed punctuation, and formatting artifacts
- normalize Markdown headings, lists, tables, and code formatting
- restore table of contents links and heading anchors
- preserve the original meaning, nuance, and technical detail
- improve readability and navigation without introducing new claims

For technical or security-related material:
- assess architecture, data flow, access control, and system coherence
- identify security risks, code quality issues, and maintainability concerns
- focus first on high-impact findings affecting confidentiality, integrity, or availability
- present findings in a consistent, actionable format

Formatting standards:
- use standard Markdown syntax throughout
- wrap inline code and identifiers in backticks
- use clean tables for metadata and attribute-value pairs
- use consistent bullets and numbering
- ensure section titles are stable and anchor-friendly
- keep the output precise, professional, and ready for immediate use

Do not explain your process. Output only the final reconstructed document.
```

## Best practice for using it across GPT-5.x and Claude

To adapt it well across models, keep the prompt modular:

* **Role**: expert reconstruction and review assistant
* **Task**: rebuild source into final document
* **Constraints**: fidelity, no invention, formatting repair only
* **Style**: clean, professional, Markdown-first
* **Domain add-on**: security/codebase analysis when relevant
* **Output**: final document only

## One extra refinement

The original text has a lot of “I am…” self-talk. That usually works better as an **internal behavior spec**, but not as the final user-facing prompt. For reusable prompting, it is stronger to say:

* “repair”
* “normalize”
* “preserve”
* “prioritize”
* “verify”
* “reconstruct”

Those verbs tend to produce more reliable results than motivational prose.

# https://chatgpt.com/share/6a124e5e-754c-83ec-9037-181bd9e0921d 


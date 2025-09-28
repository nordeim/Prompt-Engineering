## Production‑Ready System Prompt Checklist

This is a detailed checklist broken into phases / categories. When designing a system prompt for an AI agent for production use, you can walk through this to ensure robustness, clarity, maintainability, safety, and good performance.

| Category                              | Check                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Why It Matters / Risk If Omitted                                                                                                                                                           |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Agent Identity & Role**             | • Define the agent’s role or persona precisely (e.g. data scientist, legal assistant, customer support, etc.). <br> • State domain(s) of expertise, if applicable. <br> • State style / tone: formal / informal / cheerful / serious / approachable, etc.                                                                                                                                                                                             | Role framing steers what kind of responses you get; missing role often leads to vague or misaligned output. Tone ensures consistency. Without this, users may get outputs that feel “off.” |
| **Knowledge & Capabilities**          | • Specify knowledge cutoff date. <br> • Specify which external tools / data sources / memory / APIs the agent *can* use. <br> • Specify which ones it **cannot** use (limits). <br> • If using retrieval or internet, say how to verify or cite sources. <br> • Clarify uncertainty: when it should respond “I don’t know” rather than guess.                                                                                                         | Helps avoid hallucinations, ensures agent only uses allowed resources. Limits reduce risk. Uncertainty handling avoids overconfidence.                                                     |
| **Behavior & Constraints / Safety**   | • List forbidden content or behaviors (e.g. hate speech, defamatory content, privacy violations, illegal advice, etc.). <br> • Specify refusal style / tone: How should the agent refuse or set boundaries (brief, polite, no moralizing etc). <br> • Ethical guidelines: e.g. bias, fairness, cultural sensitivity. <br> • Data privacy / confidentiality constraints. <br> • Safety: handling user misuse, adversarial inputs, etc.                 | Safety and ethics are non‑negotiable. Agents that violate policy or produce unsafe content can cause real damage. If constraints are vague, model might violate them or misinterpret.      |
| **Format, Style & Output Structure**  | • Define output format: JSON / markdown / bullet points / narrative / code blocks etc. <br> • Specify size / length constraints (max tokens, conciseness, verbosity). <br> • Style constraints: e.g. avoid certain words (“absolutely”, “always”), avoid starting with apologies, avoid over‑promising. <br> • Tone / language level: technical / layperson; formal vs conversational. <br> • Organizational structure: headings, sections, examples. | When outputs are consumed by downstream systems (UIs, APIs), consistent structure matters. Also helps human reading. Vague format leads to unpredictable output.                           |
| **Reasoning & Planning Instructions** | • For complex tasks, instruct step‑by‑step reasoning or “chain of thought”. <br> • If multiple subtasks, specify how to plan, break down, decide. <br> • If tool calls are needed, define when / how to call tools; specify “think before acting” when needed. <br> • Ask for verification or checking before final output (self‑check).                                                                                                              | Helps in correctness, avoids mistakes in complex tasks. Without planning instructions, agent may jump to conclusions or forget steps.                                                      |
| **Edge Cases / Exceptions**           | • Define what to do if user asks something outside scope / domain. <br> • Define how to handle ambiguous input: ask for clarification. <br> • Define fallback behavior when tools fail or data retrieval fails. <br> • Handling conflicting instructions from user vs system.                                                                                                                                                                         | Real‑world usage always hits edge / freak cases. If not handled, agent may produce bad / misleading output or crash.                                                                       |
| **Tool / API Integration**            | • List allowed tools, APIs, their input/output specification. <br> • Specify how to format calls, how to wrap results. <br> • Constraints on tool usage (e.g. one at a time; check tool before use). <br> • Permissions: what the agent is allowed vs forbidden to access.                                                                                                                                                                            | For agents with tools, unclear tool instructions lead to misuse (e.g. too many/unnecessary calls) or errors. Also security concerns.                                                       |
| **User Interaction Guidelines**       | • How to ask questions if the user is ambiguous. <br> • When/if to escalate to human or ask for approval. <br> • How to handle corrections, contradictions by user. <br> • Maintain context / memory guidelines if relevant.                                                                                                                                                                                                                          | Good UX; prevents misunderstandings; helps in continuous conversations.                                                                                                                    |
| **Versioning, Logging, Monitoring**   | • Include version or date metadata in the system prompt (internal). <br> • Maintain changelogs for changes. <br> • Define test suite of sample prompts and edge cases to validate behavior after changes. <br> • Monitor performance in production: error rates, user feedback, safety incidents. <br> • Possibly keep A/B comparisons for system prompt variants.                                                                                    | Without versioning, drift becomes hard to trace; hard to debug when behavior changes. Monitoring ensures prompt remains good over time.                                                    |
| **Localization, Culture, Legal**      | • If deployed in multiple locales: consider cultural sensitivity, language norms. <br> • Legal compliance: region‑specific data laws, disclaimers, disclaimers for medical/legal advice. <br> • Language/Bias issues: ensure style/phrasing do not reflect unintended bias.                                                                                                                                                                           | Because thing that’s safe/legal in one region might violate law or be insulting in another. Localization helps acceptance and reduces liability.                                           |
| **Performance / Cost Considerations** | • Keep the system prompt concise enough to avoid wasteful token usage, but detailed enough to constrain behavior. <br> • Consider token footprint (especially for long contexts). <br> • Response latency trade‑off when using many steps / reasonings. <br> • Evaluate model version trade‑offs (smaller vs larger) in context of prompt complexity.                                                                                                 | In production, cost & speed matter. Overly long system prompts may slow things, increase cost, or hit token limits.                                                                        |

---

### Workflow / Process Checklist

Beyond the content, here’s a process you should follow to ensure a robust system prompt is produced and maintained.

1. **Gather Requirements**

   * What is the agent’s domain, constraints, safety requirements, target users, deployment channels (API, UI, mobile, etc.).
   * Stakeholders: legal/compliance, UX, ethics, security.

2. **Draft Prompt** using template structure (with sections: role, knowledge & limit, constraints, format, tools, examples, etc.).

3. **Add Examples**

   * Best practice cases, typical input/output pairs.
   * Edge case examples, failure / refusal examples.

4. **Review by Experts**

   * Get domain experts / legal / safety reviewers to check prompt.
   * Check for ambiguity, missing constraints, unsafe content.

5. **Test & Validation**

   * Run synthetic tests: send a variety of prompts (normal, edge, adversarial) to see behavior.
   * Use test suite of sample user queries.
   * Run metrics: correctness, safety violations, output format adherence.

6. **Iterate & Refine**

   * Based on test failure, user feedback.
   * Modify system prompt; maybe adjust wording or constraints.

7. **Release & Version**

   * Tag version number, date.
   * Document what changed.
   * If possible, publish summary to users or stakeholders.

8. **Monitor in Production**

   * Collect logs (with user queries responses) to see drift / misbehavior.
   * User feedback loops.
   * Safety and legal compliance incidents.

9. **Maintenance**

   * Periodic reviews (quarterly or after major model updates).
   * Localization / domain adaptations.
   * Keep examples and test suite updated.

---

## Examples of Good System Prompts

Here are several examples (some inspired by public prompts) of high‑quality system prompts, adapted / generalized, that illustrate many of the checklist items. You can adapt or mix and match pieces.

---

### Example 1: Domain Expert Assistant (Data Scientist)

```
System Prompt Version: 1.0 — Data‑Scientist Assistant — [2025‑09‑28]

You are an expert data scientist with strong experience analyzing business datasets, statistical modeling, and interpreting results for non‑technical audiences. Your responses should be accurate, thorough, and transparent.

Knowledge & Tools:
- Knowledge cutoff: August 2025.
- You have access to tools: data_explorer (for summary stats & visualizations), external dataset retrieval if user supplies link, data_cleaner (for basic cleaning tasks).
- Do not access any private or sensitive user data unless provided by the user and ensure no leakage or misuse.

Behavior & Ethical Constraints:
- Always check for potential bias in data; point out limitations.
- If uncertain about a result or conclusion, indicate the uncertainty clearly (“I’m not certain”, “based on current data”, etc).
- Do not make claims beyond evidence.
- Do not provide legal or medical advice.

Output Format & Style:
- Use markdown with headings: **Summary**, **Key Findings**, **Limitations**, **Recommendations**.
- Provide visualizations via ASCII or external link placeholders if necessary but annotate clearly.
- Tone: professional but approachable; avoid jargon when speaking to non‑technical users.
- Be concise: summaries should be < 200 words when possible; detailed parts can be longer.

Reasoning & Process:
- For multi‑step analyses, outline your plan first (“Here is how I will approach this: …”).
- After analysis, perform a self‑check: did you follow format? Did you consider edge cases? Did you cite sources / tools?

Edge Cases:
- If user asks about a topic beyond your domain (e.g. medical diagnosis), refuse with safe language: “I’m sorry, but I can’t assist with that request; you may want to consult a qualified professional.”
- If user’s input is ambiguous or missing data, ask for clarification.

Logging & Versioning:
- This system prompt is version 1.0, updated 2025‑09‑28. Any changes must be documented.
- Monitor responses for aberrant behavior, safety incidents, or misuse.

```

---

### Example 2: Customer Support Agent for eCommerce

```
System Prompt Version: 2.3 — eCommerce Support Agent — [2025‑09‑28]

You are an eCommerce customer support assistant specialized in helping customers with orders, returns, product information, and troubleshooting site issues.

Knowledge & Capabilities:
- Knowledge cutoff: July 2025.
- Access to tools: order_lookup (given order ID), product_database, returns_tool, escalation to human support when required.
- No internal financial data; no access to users’ private credit card info etc.

Behavior & Constraints:
- Always polite, empathetic, and helpful.
- Do not argue with the user; always aim to resolve. If conflict arises, escalate.
- Do not leak internal policy beyond what is user‑facing; avoid legal jargon.
- Refuse requests outside scope (e.g. legal advice, technical medical advice).

Format & Output:
- Use bullet points for procedural instructions. <br> - When giving instructions (“to do X, do Y then Z”), number the steps. <br> - For simple answers, short paragraphs; if the answer has multiple parts, use subheadings. <br> - When possible, provide estimated timelines (“Your return will take approx. 5‑7 business days.”), or refer to policy if available.

Reasoning & Interaction:
- If user request is unclear (“which product?”, “which order?”), ask clarifying questions.
- Use the tools when needed: before telling them something about their order, verify via order_lookup.
- If tool fails or lookup fails, “I’m sorry, I couldn’t find your order—could you confirm the order ID?”

Edge Cases & Safety:
- If user is abusive, maintain professionalism; do not respond in kind. If necessary, escalate or safe‑refuse. <br> - If asked for disallowed content (hate speech, harassment guidance, etc.), refuse with a safe template.

Versioning:
- Version 2.3, date: 2025‑09‑28.
- Change log must capture what changed from previous version (tone, behavior, tool access etc).
```

---

### Example 3: General “Philosophical / Ethical / Information” Agent (e.g. journalistic / neutrality required)

```
System Prompt Version: 1.2 — Neutral Information & Analysis Agent — [2025‑09‑28]

You are a neutral, fact‑based analysis assistant. Your role is to help users understand complex issues across domains (politics, science, ethics, culture) with clarity, objectivity, and humility.

Knowledge & Capabilities:
- Knowledge cutoff: September 2025.
- Can access public information sources / fact databases if user or backend provides. Must cite sources when referring to specific studies / claims.

Behavior & Ethical Constraints:
- Avoid taking sides unless based on recognized facts; treat controversial topics with impartiality. <br> - When quoting opinions, clearly mark “this is a view / opinion” vs “this is fact.” <br> - Avoid framing that inflames (e.g. avoid overly emotional or sensational language). <br> - Acknowledge uncertainty, conflicting evidence.

Format & Output:
- Use structure: **Background** / **Current Debates** / **Evidence** / **Implications** / **Summary**. <br> - Use bullet lists for pros/cons; use citations. <br> - Tone: respectful, measured, clear. <br> - Use plain language; assume educated layperson audience.

Reasoning & Process:
- Lay out major arguments / perspectives. <br> - Identify sources of evidence; if conflicting, show both sides. <br> - Ask when necessary for clarification (e.g. what aspect or perspective the user cares about).

Edge Cases:
- If user wants propaganda, extremist content, or disallowed content, refuse. <br> - If user’s request is ambiguous (“what happened in recent science”), ask for topic or field. <br> - If data or evidence is lacking, say so rather than fabricating.

Versioning & Monitoring:
- Version 1.2 – internal date 2025‑09‑28. <br> - Regular review especially after major current‑events or research updates. <br> - Maintain logs of contentious responses for review.
```

---

### Example 4: Tool‑Using Agent Example (from public sources, adapted)

Adapted from Mastra example (cat expert) ([Mastra][1])

```
System Prompt Version: 1.0 — Cat‑Expert Assistant — [2025‑09‑28]

You are a helpful cat expert assistant. When discussing cats, you should always include an interesting cat fact.

Your main responsibilities:
1. Answer questions about cats (behavior, health, breeds, care).
2. Use the `catFact` tool to provide verified cat facts (from a trusted source) when relevant.
3. Incorporate cat facts naturally into your responses; don’t dump fact first then answer—blend in.

Constraints & Safety:
- Do not provide veterinary or medical advice beyond widely known care recommendations; for anything serious, instruct user to consult a vet.
- Do not promote irresponsible breeding or practices.

Format & Style:
- Use friendly, conversational tone.
- Include a cat fact at least once per response.
- Keep facts concise; use bullet points for lists or multi‑part answers. If image of breed: include breed name, temperament, care tips.

Edge Cases:
- If user asks something not about cats, gently redirect / refuse.
- If tool fails, still try to answer from general knowledge and warn “I could not access verified cat fact at this time.”

Versioning:
- Version 1.0, 2025‑09‑28.
```

---

## Some Real Public Prompt Insights

To illustrate what actual labs do, here are some insights & snippets from published system prompts:

* Anthropic publishes the default system prompts for Claude models, with release notes. For example, they instruct Claude not to open URLs, links, or videos. They also ensure the model “…avoid identifying or naming any humans in images.” ([TechCrunch][2])
* They include personality / behavior instructions: e.g. Claude is to appear intellectually curious, enjoy hearing what humans think on issues, engage in discussions on wide topics, provide careful thoughts and clear information, and never to begin responses with “certainly” or “absolutely.” ([TechCrunch][2])
* UiPath Agents: their docs say a good system prompt “clearly determine a plan for action, incorporate inputs in a well‑structured way, and give guidance on when to run tools, access enterprise context, or escalate to a human.” ([UiPath Documentation][3])

---

[1]: https://mastra.ai/en/examples/agents/system-prompt?utm_source=chatgpt.com "Example: Agents with a System Prompt | Agents | Mastra Docs"
[2]: https://techcrunch.com/2024/08/26/anthropic-publishes-the-system-prompt-that-makes-claude-tick/?utm_source=chatgpt.com "Anthropic publishes the 'system prompts' that make Claude tick | TechCrunch"
[3]: https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-prompts?utm_source=chatgpt.com "Agents - Prompts"

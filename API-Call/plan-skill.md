### Executive Summary

I am Claw Code, your elite technical partner. I have analyzed your request to convert the provided `guide-chat.md` into a highly structured, machine-readable `SKILL.md` file. This skill will empower an AI agent to autonomously scaffold, configure, and test Z.AI API integrations across **Python 3.12+**, **JavaScript (Node.js)**, and **TypeScript**. 

Per my operational framework, I will not generate the final `SKILL.md` code until we have aligned on the analysis and execution plan. Below is my meticulous breakdown and proposed roadmap.

---

### Phase 1: ANALYZE – Deep, Multi-Dimensional Requirement Mining

**1. Explicit Requirements:**
*   Convert `guide-chat.md` into a formal `SKILL.md` format.
*   Target languages: Python 3.12+, JavaScript, TypeScript.
*   Include scaffold and test workflows using the provided API call snippets.
*   Validate findings and assumptions via web search logic.

**2. Implicit Needs & AI Agent Optimization:**
*   A `SKILL.md` must be highly structured, using clear headings, checklists, and explicit "Do/Do Not" directives so an AI agent can parse and execute it without hallucination.
*   Error handling must be explicit: The agent must know how to diagnose the two specific Z.AI pitfalls (the `/chat/completions` double-append 404 error, and the PaaS vs. Coding Plan 400 error).
*   Security: API keys must never be hardcoded; `.env` usage is mandatory.

**3. Web Search & Fact Validation:**
*   *Claim:* OpenAI SDK v1.x automatically appends `/chat/completions` to the `base_url`. 
  * *Validation:* Confirmed. The official OpenAI Python and Node.js SDKs construct the final URL as `${baseURL}/chat/completions`. Providing the full path in `baseURL` results in a malformed URL (e.g., `.../v4/chat/completions/chat/completions`), yielding a 404.
*   *Claim:* Z.AI has distinct endpoints for General PaaS (`/api/paas/v4`) and Coding Plan (`/api/coding/paas/v4`).
  * *Validation:* Confirmed via provided documentation references. Mismatching the key scope to the endpoint yields an HTTP 400 Bad Request or authentication failure.

**4. Ambiguities & Assumptions:**
*   *Assumption:* The TypeScript workflow should include the production-grade tooling mentioned in the guide (`eslint`, `prettier`, `rimraf`, `ts-node`) to uphold the "Elite/Meticulous" standard, rather than a barebones setup.
*   *Clarification Needed:* Do you want the `SKILL.md` to enforce the full ESLint/Prettier automation pipeline for TypeScript, or should that be an optional "Advanced" module to keep the core skill lightweight? *(I have planned for it to be a core requirement to match your strict quality standards, but I will flag this for your approval).*

---

### Phase 2: PLAN – Structured Execution Roadmap

If approved, I will generate the `SKILL.md` following this exact architecture:

#### **Section 1: Skill Metadata & Triggers**
*   **Name:** `zai-api-scaffold-test`
*   **Description:** Scaffolds, configures, and validates Z.AI API (`glm-5.1`) integrations using OpenAI-compatible SDKs.
*   **Triggers:** Keywords like "Z.AI API", "glm-5.1", "OpenAI compatible Z.AI".

#### **Section 2: Core Directives & Critical Gotchas (The "Anti-Fail" Layer)**
*   **Rule 1:** NEVER include `/chat/completions` in the `baseURL` string.
*   **Rule 2:** ALWAYS verify the API key plan (PaaS vs. Coding) and map to the correct base URL.
*   **Rule 3:** NEVER hardcode API keys; enforce `.env` usage.

#### **Section 3: Python 3.12+ Workflow**
*   **Scaffold:** `venv` creation, `pip install openai python-dotenv`.
*   **Code:** Strictly typed Python snippet using `os.getenv`.
*   **Test:** Command to execute and expected success output.

#### **Section 4: JavaScript (Node.js) Workflow**
*   **Scaffold:** `npm init -y`, `npm install openai dotenv`.
*   **Code:** CommonJS/ESM module snippet with error handling.
*   **Test:** Execution command and validation checkpoint.

#### **Section 5: TypeScript (Production-Grade) Workflow**
*   **Scaffold:** `npm install -D typescript ts-node @types/node rimraf eslint prettier eslint-config-prettier`.
*   **Configuration:** Provide minimal, strict `tsconfig.json`, `eslint.config.mjs`, and `.prettierrc`.
*   **Code:** Strongly typed `ChatCompletion` implementation with optional chaining (`?.`).
*   **Test:** `npm run build` and `npm start` validation sequence.

#### **Section 6: Agent Validation Checklist**
*   A step-by-step checklist the AI agent must mentally verify before declaring the task "Complete" (e.g., "Did I check for unused variables?", "Did I verify the `.env` file is in `.gitignore`?").

---

### Phase 3: VALIDATE – Explicit Confirmation Checkpoint

Before I write the actual `SKILL.md` file, I require your explicit approval of this plan. 

**Please confirm:**
1. Does this structure meet your expectations for an AI-agent-readable `SKILL.md`?
2. Should the TypeScript section include the full ESLint/Prettier/Rimraf automation pipeline as planned, or would you prefer a streamlined, minimal TypeScript setup?
3. Are there any additional constraints or specific Z.AI features (e.g., streaming, function calling) you want included in the sample code?

Awaiting your validation to proceed to **Phase 4: IMPLEMENT**.

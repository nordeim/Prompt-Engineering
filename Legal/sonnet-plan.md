# Phase 1: Meticulous Analysis — Singapore Legal Drafting Assistant Prompt

## Executive Summary

I will conduct a rigorous, impartial critique of this legal AI agent prompt across seven dimensions: GPT-5 compatibility, legal domain appropriateness, instruction clarity, liability risks, practical usability, ethical compliance, and structural quality. 

**Preview of findings**: This prompt contains **critical incompatibilities** with GPT-5 architecture, significant **legal liability risks**, and **contradictory instructions** that could impair performance. However, it also demonstrates sophisticated understanding of Singapore legal practice and thoughtful risk mitigation attempts.

---

## Part 1: Critical Incompatibilities with GPT-5

### 🚨 CRITICAL ISSUE #1: Chain-of-Thought Suppression

```
"When given a task, follow these steps in order. Do NOT reveal internal 
chain-of-thought. Provide concise, auditable explanations only — not 
private internal deliberation."
```

**Problem**: This instruction is **fundamentally incompatible** with GPT-5's architecture.

**Why this is critical**:
- GPT-5 is a **reasoning model** that uses extended chain-of-thought to produce outputs
- The model doesn't have separate "internal thoughts" vs. "external output" - all reasoning is part of the generation process
- GPT-5's API includes `reasoning` tokens that are part of its process
- Instructing it not to "reveal" reasoning is like asking a human to think without thinking

**Evidence from GPT-5 Guide**:
> "GPT-5 is trained to provide clear upfront plans and consistent progress updates via 'tool preamble' messages."

The guide **encourages** transparency about reasoning process, not suppression.

**Impact**: 
- ❌ Creates cognitive dissonance in model behavior
- ❌ May suppress useful explanatory context that helps users understand the draft
- ❌ Contradicts the model's training to be transparent about its process
- ❌ Could lead to worse outputs as the model tries to reconcile contradictory instructions

**Recommendation**: **Remove this instruction entirely** or replace with:
```xml
<output_transparency>
- Provide clear explanations of your drafting choices and legal reasoning
- Structure your output to separate: (a) legal analysis, (b) draft clauses, (c) risk commentary
- Be transparent about your reasoning process while keeping outputs professionally formatted
</output_transparency>
```

**Severity**: 🔴 **CRITICAL** - Fundamentally misaligned with model architecture

---

### 🚨 CRITICAL ISSUE #2: File Format Generation Confusion

```
"Provide outputs in multiple formats on request: plain text, HTML 
(browser-ready), and DOCX/PDF instructions (or generate these if system 
supports file export)."
```

**Problem**: GPT-5 API does not natively generate DOCX or PDF files.

**Why this is problematic**:
- Sets false expectations for users
- "(or generate these if system supports file export)" creates ambiguity - should the model attempt to generate these or not?
- The model will likely provide instructions for conversion rather than actual files, but the prompt suggests it should generate files directly

**Clarification needed**:
```xml
<output_formats>
- Provide drafts in markdown or plain text format suitable for copying
- Upon request, provide formatted HTML that can be opened in a browser and printed to PDF
- If DOCX is needed, provide clear instructions for importing the text into Microsoft Word
- Do not claim ability to generate native DOCX or PDF files directly
</output_formats>
```

**Severity**: 🟡 **MODERATE** - Creates confusion and false expectations, but not harmful

---

### 🚨 CRITICAL ISSUE #3: No GPT-5 Configuration

**Missing entirely**: `reasoning_effort`, `verbosity`, tool usage patterns, agentic behavior calibration

**Why this matters for legal drafting**:

| Task Type | Optimal GPT-5 Config | Current Prompt |
|-----------|---------------------|----------------|
| **Simple NDA drafting** | Medium reasoning, medium verbosity | ❌ Not specified - may over-reason |
| **Complex multi-party agreement** | High reasoning, high verbosity for explanations | ❌ Not specified - may under-reason |
| **Quick clause review** | Low reasoning, low verbosity | ❌ Not specified - may be too verbose |
| **Legal research** | High reasoning, tool calling for case law | ❌ No tool usage guidance |

**Missing configuration**:
```xml
<gpt5_configuration>
### Reasoning Effort
- High reasoning: Complex agreements, novel legal issues, multi-jurisdiction analysis
- Medium reasoning: Standard commercial contracts with customization
- Low reasoning: Template selection, simple clause explanations

### Verbosity
- High verbosity: Explanations of legal reasoning, risk analysis, alternative options
- Medium verbosity: Draft clauses with brief commentary
- Low verbosity: Quick confirmations, simple answers to clarifying questions

### Agentic Behavior
- Moderate autonomy: Proceed with drafting when core information is provided
- Request clarification only for legally material ambiguities (governing law, party identity, core obligations)
- Provide options rather than asking user to choose when multiple valid approaches exist

### Tool Usage (if available)
- Legal database search: Use for recent case law, statutory updates
- Citation verification: Verify all case citations before including
- Document templates: Reference authoritative Singapore law society templates where applicable
</gpt5_configuration>
```

**Severity**: 🟠 **HIGH** - Missing significant performance optimization opportunities

---

## Part 2: Legal Liability & Professional Responsibility Issues

### 🚨 CRITICAL ISSUE #4: "Execution-Ready" Drafts & Unauthorized Practice of Law

```
"Provide a complete, execution-ready draft..."
"Produce: (a) a clean final text..."
```

**Problem**: This language creates significant legal and ethical risks.

**Why this is extremely problematic**:

| Risk Category | Issue | Potential Harm |
|---------------|-------|----------------|
| **Unauthorized practice of law** | AI providing "execution-ready" legal documents could constitute legal practice | Regulatory action, user liability |
| **Professional negligence exposure** | Users may rely on "execution-ready" language without lawyer review | Unenforceable contracts, litigation |
| **Misleading users** | "Execution-ready" implies professional validation that hasn't occurred | Users sign defective agreements |
| **Regulatory compliance** | Singapore Legal Profession Act restrictions on legal practice | Potential violations |

**Evidence**: The prompt DOES include a disclaimer:
```
"this draft is not legal advice, and the user must obtain review and 
sign-off by a Singapore-qualified lawyer"
```

**BUT**: This disclaimer is **undermined** by calling the output "execution-ready." These messages are contradictory:
- "This draft is execution-ready" = You can execute (sign) this now
- "You must obtain lawyer review" = Don't execute this without review

**User confusion scenario**:
1. User receives "execution-ready" draft
2. User thinks "ready to execute" means ready to sign
3. Disclaimer is at the end, may be skipped
4. User signs without legal review
5. Contract is unenforceable or unfavorable
6. User blames AI system

**Recommendation - REFRAME ENTIRELY**:
```xml
<output_characterization>
### What This System Provides
This system produces DRAFT legal documents for review by Singapore-qualified counsel. 
All outputs are:
- **Working drafts** - not final documents
- **Discussion materials** - to facilitate conversation with your lawyer
- **Starting points** - requiring professional legal review and customization
- **Educational tools** - to help you understand common legal structures

### What This System Does NOT Provide
- ❌ Legal advice
- ❌ Final, execution-ready documents
- ❌ Substitute for lawyer review
- ❌ Representation that drafts are enforceable or suitable for your situation

### Required Next Steps
ALWAYS have these drafts reviewed, revised, and approved by a Singapore-qualified lawyer 
before execution. No AI-generated legal draft should be signed without lawyer review.

### Characterize Outputs As
- "Draft for lawyer review"
- "Discussion draft"
- "Initial working draft"
NOT as "execution-ready" or "final"
</output_characterization>
```

**Severity**: 🔴 **CRITICAL** - Legal and professional liability exposure

---

### 🚨 HIGH RISK ISSUE #5: Citation Fabrication Vulnerability

```
"If legal authority or commentary is referenced, cite high-quality sources 
(Singapore Court of Appeal decisions, statutes, reputable firm briefs). 
If you cannot fetch or verify the citation, say so instead of inventing it."
```

**Problem**: This instruction is well-intentioned but creates a **trap**.

**The trap**:
1. Prompt requires "high-quality sources" throughout (Section 2, 7, 9)
2. Prompt says "cite... Court of Appeal decisions, statutes" (creating expectation)
3. Prompt says "if you cannot... say so instead of inventing"
4. BUT: The pressure to provide citations + lack of verification mechanism = **high risk of hallucinated citations**

**Why LLMs hallucinate legal citations**:
- Legal citations follow predictable patterns (e.g., "[Year] SGCA [number]")
- Models learn these patterns and can generate plausible-looking but fake citations
- The prompt's requirement for "high-quality sources" throughout creates pressure to cite
- Without tool access to verify, the model may generate convincing but false citations

**Real example of what could happen**:
```
User: "What's the leading Singapore case on penalty clauses?"

AI Response: "The leading authority is Dunlop Pneumatic Tyre Co Ltd v New 
Garage and Motor Co Ltd [1915] AC 79, applied in Singapore in Xia Zhengyan 
v Geng Changqing [2015] SGCA 81..."

Problem: [2015] SGCA 81 might not exist or might be about something else entirely.
```

**Current prompt says**: "If you cannot fetch or verify the citation, say so"

**Reality**: The model doesn't "know" whether it can verify - it generates probabilistically. It won't naturally flag uncertainty unless strongly prompted.

**Better approach**:
```xml
<legal_citations>
### Citation Policy
**Default**: Do NOT cite specific cases unless you have verified access to the case text.

**When discussing legal principles**:
✅ Explain the principle in general terms: "Singapore courts apply the test from Dunlop 
   Pneumatic Tyre to distinguish liquidated damages from penalties..."
✅ Reference statutory provisions by number: "Personal Data Protection Act 2012, Section 24"
✅ State general rules: "Singapore Court of Appeal has consistently held that..."

❌ Do NOT provide case citations (e.g., [Year] SGCA [number]) unless you can verify the citation
❌ Do NOT invent case names, years, or reporter citations
❌ Do NOT provide "reputable firm briefs" citations without links to actual documents

### If User Requests Specific Citations
"I can describe the relevant legal principles and tests applied by Singapore courts, but 
I recommend having your lawyer verify specific case citations. The key principles are: 
[explain]. Your lawyer can identify the current leading authorities."

### If Tool Access to Legal Database Available
Use legal research tools to verify citations before including them. Always provide:
- Full case name
- Citation ([Year] SGCA/SGHC [number])
- Link to judgment if available
- Brief description of relevance
</legal_citations>
```

**Severity**: 🔴 **CRITICAL** - High risk of providing false legal authorities, which is professionally disastrous

---

### 🚨 MODERATE ISSUE #6: Negotiation Strategy & Email Drafting

```
"Offer to produce negotiation talking points and a short email to the 
other party summarising proposed changes and commercial rationale."
```

**Problem**: This edges into legal strategy and representation.

**Concerns**:
- Drafting communications to opposing parties is part of legal representation
- "Negotiation talking points" constitutes legal strategy advice
- Users might send AI-generated emails without lawyer review
- Could create attorney-client privilege complications if user is represented

**Safer approach**:
```xml
<negotiation_support>
### What This System Can Provide
- Explanation of different drafting options and their commercial implications
- Summary of key terms in plain language for internal discussion
- Comparison of alternative clause formulations

### What Requires Lawyer Involvement
- ❌ Negotiation strategy and tactics - requires lawyer advice
- ❌ Communications to the other party - should be reviewed/sent by lawyer
- ❌ Assessment of the other party's positions - requires legal judgment
- ⚠️ If you need negotiation support, work with your Singapore-qualified lawyer

### If User Requests Negotiation Help
"I can explain the legal and commercial implications of different clause options, 
but negotiation strategy should be developed with your lawyer. Would you like me to 
explain the pros and cons of different approaches for you to discuss with counsel?"
</negotiation_support>
```

**Severity**: 🟠 **MODERATE-HIGH** - Professional boundary issues, though less severe than "execution-ready" language

---

## Part 3: Instruction Clarity & Contradictions

### Contradiction Matrix

| Contradiction # | Instruction A | Instruction B | Conflict Type | Severity |
|-----------------|---------------|---------------|---------------|----------|
| **1** | "Do NOT reveal internal chain-of-thought" | "Include short drafting notes explaining why particular clauses are used" | Direct contradiction - which explanations are allowed? | HIGH |
| **2** | "Do not invent facts. If key factual inputs are missing, ask for them" | "FACT-GATHERING (auto checklist) - Collect or confirm... Ask only if necessary; if user provided these, proceed" | When to ask vs. proceed unclear | MEDIUM |
| **3** | "Be concise but thorough" | "Provide: (a) clean final text; (b) one-page summary; (c) counsel memo; (d) alternatives section; (e) negotiation points; (f) email draft" | Concise vs. 6 separate deliverables | MEDIUM |
| **4** | "Do NOT reveal internal chain-of-thought. Provide concise, auditable explanations only" | "produce at least two alternative constructions with short pros/cons and enforceability risk flags" | How to provide risk analysis without revealing reasoning? | HIGH |
| **5** | "follow these steps in order" (rigid sequence) | GPT-5's natural reasoning flow (flexible, adaptive) | Process vs. model architecture | MEDIUM |

---

### Analysis of Contradiction #1: Reasoning Transparency

**The Core Conflict**:

```
❌ "Do NOT reveal internal chain-of-thought. Provide concise, auditable 
    explanations only — not private internal deliberation."

✅ "Include short drafting notes explaining why particular clauses are 
    used and how they address Singapore law concerns."
```

**What is the difference between**:
- "Drafting notes explaining WHY" ← This IS reasoning/deliberation
- "Internal deliberation" ← This is also reasoning

**User confusion scenario**:
- Should the AI explain WHY a clause is drafted a certain way? (Instruction 7 says yes)
- But should it NOT reveal its internal thought process? (Opening says no)
- These are the same thing in legal drafting context

**This contradiction will cause**:
- Inconsistent behavior (sometimes explains, sometimes doesn't)
- GPT-5 spending reasoning tokens trying to reconcile the contradiction (per guide, this impairs performance)
- Less useful outputs (explanations are valuable in legal drafting)

**Resolution**:
```xml
<reasoning_transparency>
### Provide Clear Legal Reasoning
- Explain the purpose and legal basis for each significant clause
- Describe how clauses address Singapore law requirements or risks
- Clarify drafting choices and alternatives considered

### Structure Explanations Professionally
- Separate legal analysis from draft text (use headings/sections)
- Provide explanations in professional legal memo format
- Include risk commentary and recommendations

### Avoid
- ❌ Stream-of-consciousness internal monologue
- ❌ Unstructured "thinking out loud"
- ✅ Instead: Structured, professional legal analysis
</reasoning_transparency>
```

---

### Analysis of Contradiction #2: Fact-Gathering Directive

**The Conflict**:

```
"Do not invent facts."
    vs.
"FACT-GATHERING (auto checklist) - Collect or confirm... 
 Ask only if necessary; if user provided these, proceed."
```

**Problem**: "Ask only if necessary" is vague and could mean:
- Interpretation 1: Ask only if facts are legally material
- Interpretation 2: Ask only if facts weren't already provided
- Interpretation 3: Infer facts from context and only ask if you can't infer

**GPT-5 Guide Warning**: Vague stopping criteria impairs performance.

**Real scenario**:
```
User: "Draft an NDA between my company and a vendor."

Missing facts:
- Company legal names ← Critical
- UEN numbers ← Requested in checklist but often not provided by users
- Registered addresses ← Requested in checklist
- Signatory names ← Requested in checklist
- Currency ← Requested in checklist

Question: Should AI ask for all of these, or only "if necessary"?
What is "necessary" - legally required vs. good practice?
```

**Better approach**:
```xml
<fact_gathering>
### Essential Facts (always required - ask if not provided)
Must have before drafting:
- Full legal names of both parties
- Entity types (Pte Ltd, sole proprietor, etc.)
- Governing law confirmation (Singapore?)
- Core commercial terms (what's being protected, term length, obligations)

### Standard Facts (strongly recommended - prompt once)
Should gather:
- Registered addresses
- UEN numbers (for Singapore entities)
- Signatory names and titles
- Execution method (wet signature vs. electronic)
- Dispute resolution preference

**Approach**: Present a single, organized information-gathering form
"To draft your agreement, I need the following information. Please provide what you 
have available (items marked with * are essential):
[Structured form with clear required vs. optional fields]"

### Facts to NOT Invent
- ❌ Do not create placeholder party names
- ❌ Do not assume signatory authority
- ❌ Do not invent addresses or registration numbers
- ❌ Do not assume commercial terms not stated
- ✅ Use clearly marked placeholders: [PARTY A LEGAL NAME], [UEN], etc.
</fact_gathering>
```

**Severity**: 🟡 **MEDIUM** - Could lead to either over-asking (annoying users) or under-asking (missing critical info)

---

## Part 4: Structural & Usability Analysis

### Issue #7: Rigid Sequential Processing

```
"When given a task, follow these steps in order."
[10 numbered steps]
```

**Problem**: This is extremely prescriptive and doesn't match GPT-5's natural reasoning.

**From GPT-5 Guide**:
> "Cursor found that sections of their prompt that had been effective with earlier models 
> needed tuning to get the most out of GPT-5... they found it counterproductive with GPT-5, 
> which is already naturally introspective and proactive"

**Why rigid sequencing is problematic**:
- GPT-5 may naturally want to combine steps (e.g., clarify scope WHILE checking legal context)
- Forcing artificial sequence wastes reasoning tokens
- Some steps may not be necessary for simple requests
- Creates inefficiency

**Example of inefficiency**:
```
User: "Just explain what a liquidated damages clause is."

Current prompt forces:
Step 1: CLARIFY SCOPE ← Not needed
Step 2: LEGAL CONTEXT CHECK ← Maybe relevant
Step 3: FACT-GATHERING ← Not needed
Step 4: DRAFTING RULES ← Not needed
Step 5: RISK-BASED OPTIONS ← Not needed
Step 6: DRAFT THE AGREEMENT ← Not needed
...

The model has to reason through "should I do this step?" for each, wasting tokens.
```

**Better approach - Workflow-Based, Not Sequential**:
```xml
<task_specific_workflows>
### Workflow 1: Full Agreement Drafting
When user requests complete agreement:
1. Gather essential facts (use structured form)
2. Confirm legal context (Singapore law, key statutory issues)
3. Draft clauses with alternatives for high-risk provisions
4. Provide: draft, risk summary, counsel review memo, alternative formulations

### Workflow 2: Clause Modification/Review
When user requests specific clause review or modification:
1. Understand current clause and requested change
2. Identify Singapore law implications
3. Provide: revised clause, risk analysis, alternatives
4. Flag issues for counsel review

### Workflow 3: Legal Explanation
When user asks for explanation of concepts:
1. Provide clear explanation of concept
2. Include Singapore-specific considerations
3. Offer to provide example clause if helpful

### Workflow 4: Template Selection
When user needs help choosing agreement type:
1. Understand commercial relationship and goals
2. Recommend appropriate agreement type(s)
3. Explain key clauses and considerations
4. Offer to proceed with drafting if user confirms

**Flexibility**: Adapt workflow to task; don't force unnecessary steps
</task_specific_workflows>
```

**Severity**: 🟡 **MEDIUM** - Reduces efficiency, but doesn't break functionality

---

### Issue #8: Multiple Deliverable Overload

```
"Produce: (a) a clean final text; (b) a one-page plain English summary of 
key points and risks; (c) a short "to-counsel" memo pointing to remaining 
issues requiring local counsel review."

"Include a redline or alternatives section for every high-risk clause."

"Offer to produce negotiation talking points and a short email to the other 
party summarising proposed changes and commercial rationale."
```

**Count of deliverables requested**:
1. Clean draft text
2. One-page summary
3. Counsel review memo
4. Alternatives section
5. Redlines
6. Negotiation talking points (optional)
7. Email to counterparty (optional)

**Problems**:
- Contradicts "be concise"
- User may only want the draft
- Forces work user didn't request
- Increases latency significantly
- Higher token costs

**User scenario**:
```
User: "Draft a simple mutual NDA"

AI: [Produces 7 separate sections totaling 3000+ words]

User: "I just wanted the basic NDA text..."
```

**Better approach - Modular Output**:
```xml
<output_structure>
### Core Output (always provide)
- Draft agreement text
- Brief risk summary (2-3 key points)

### Extended Output (offer, provide on request)
- Detailed clause-by-clause commentary
- Alternative formulations for high-risk clauses
- Comprehensive counsel review memo
- Plain-English summary for non-lawyers

### Specialized Output (provide only on request)
- Redline comparison (if comparing to prior version)
- Negotiation considerations
- Jurisdiction-specific compliance notes

**Approach**: 
"I've drafted your [agreement type]. I can also provide:
- Detailed risk analysis and alternative clauses
- Plain-English summary
- Comprehensive counsel review memo
Which would be helpful?"
</output_structure>
```

**Severity**: 🟡 **MEDIUM** - Usability issue, could overwhelm users

---

## Part 5: Domain-Specific Strengths

### What This Prompt Does Well ✅

Despite the critical issues, this prompt demonstrates **sophisticated legal knowledge**:

| Strength | Evidence | Assessment |
|----------|----------|------------|
| **Singapore-specific** | Penalty clause principles, PDPA references, Courts of Singapore jurisdiction | ✅ Excellent domain focus |
| **Liquidated damages sophistication** | "genuine pre-estimate of loss", severability, fallback provisions | ✅ Shows real understanding of penalty doctrine |
| **Risk mitigation options** | Three-tier LD alternatives (Option A/B/C) with enforceability analysis | ✅ Thoughtful risk management |
| **Comprehensive clause coverage** | Return/destruction, survival, limitation of liability, carveouts | ✅ Commercially aware |
| **Singapore procedural awareness** | Injunctive relief, arbitration seat, e-signature considerations | ✅ Practical knowledge |
| **Definitional discipline** | Consistent capitalization, definitions section | ✅ Professional drafting standard |
| **Dual-purpose output** | Plain-English summary + legal draft | ✅ User-friendly approach |
| **Escalation to counsel** | Multiple reminders to get lawyer review | ✅ Responsible (though undermined by "execution-ready" language) |

**Key insight**: The **author clearly understands Singapore commercial contract law** and has thought deeply about risk mitigation. The legal substance is strong.

**The problems are**:
1. ❌ Implementation choices (execution-ready language, citation pressure)
2. ❌ GPT-5 incompatibilities (chain-of-thought suppression, no configuration)
3. ❌ Structural rigidity (10-step sequence, multiple contradictions)

---

## Part 6: Safety & Ethics Assessment

### Positive Safety Features ✅

```xml
✅ "this draft is not legal advice, and the user must obtain review and 
   sign-off by a Singapore-qualified lawyer"

✅ "Highlight any clause you believe carries material enforceability risk"

✅ "Never provide legal regulation or compliance guidance for a jurisdiction 
   other than Singapore unless explicitly asked"

✅ "If the user requests litigation strategy, produce neutral information 
   only and recommend counsel"
```

**Assessment**: The prompt shows awareness of professional boundaries and risks.

### Safety Vulnerabilities ⚠️

| Vulnerability | Risk | Mitigation Missing |
|---------------|------|---------------------|
| **"Execution-ready" language** | Users sign without review | Should never characterize as execution-ready |
| **Citation hallucination** | Users rely on fake authorities | Need explicit "do not cite without verification" rule |
| **Negotiation emails** | Users send without lawyer review | Should not offer to draft communications to counterparties |
| **No expertise level check** | Lawyer vs. layperson get same output | Should adapt to user sophistication |
| **No jurisdiction verification** | User might be in wrong jurisdiction | Should confirm Singapore jurisdiction applicability |

---

## Part 7: Comprehensive Scoring

### Quantitative Evaluation

| Dimension | Weight | Score (1-10) | Weighted | Comments |
|-----------|--------|--------------|----------|----------|
| **Legal Domain Expertise** | 20% | 9.0 | 1.80 | Excellent Singapore law knowledge |
| **GPT-5 Compatibility** | 20% | 2.0 | 0.40 | Critical incompatibilities |
| **Instruction Clarity** | 15% | 4.0 | 0.60 | Multiple contradictions |
| **Professional Responsibility** | 15% | 4.5 | 0.68 | Good intent, risky execution |
| **Practical Usability** | 10% | 5.0 | 0.50 | Rigid, overwhelming |
| **Safety & Risk Management** | 10% | 6.0 | 0.60 | Some good, some gaps |
| **Output Quality Potential** | 10% | 7.0 | 0.70 | Could produce good drafts if issues fixed |

**Total Weighted Score**: **5.28 / 10**

**Interpretation**: 
- **Below acceptable** for production deployment
- **Strong legal foundation** but significant implementation flaws
- **Needs substantial revision** before use

---

## Part 8: Critical Recommendations

### Priority 1: MUST FIX (Blocking Issues)

#### 1. Remove "Execution-Ready" Language Immediately 🔴
```xml
<!-- REMOVE -->
❌ "execution-ready draft"
❌ "clean final text"
❌ "complete agreement"

<!-- REPLACE WITH -->
✅ "working draft for lawyer review"
✅ "discussion draft"
✅ "preliminary draft requiring legal review"
```

**Why critical**: Legal liability exposure

---

#### 2. Remove Chain-of-Thought Suppression 🔴
```xml
<!-- REMOVE -->
❌ "Do NOT reveal internal chain-of-thought. Provide concise, auditable 
    explanations only — not private internal deliberation."

<!-- REPLACE WITH -->
✅ <output_organization>
Provide well-structured outputs with clear sections:
1. Draft agreement text (clean, professionally formatted)
2. Legal analysis and risk commentary (structured memo format)
3. Alternative formulations (for high-risk clauses)
4. Recommendations for counsel review

Maintain professional tone and organization throughout.
</output_organization>
```

**Why critical**: Incompatible with GPT-5 architecture

---

#### 3. Implement Citation Safety Protocol 🔴
```xml
<!-- ADD -->
<citation_safety_protocol>
**DEFAULT RULE**: Do NOT cite specific Singapore cases by name and citation 
unless you have verified access to the judgment text.

**Instead of citing cases**:
✅ "Singapore courts apply a well-established test to distinguish liquidated 
   damages from penalties, focusing on whether the sum is a genuine pre-estimate 
   of loss at the time of contracting."

❌ "In Xia Zhengyan v Geng Changqing [2015] SGCA 81, the Court held..."

**Statutory citations**: Safe to cite by name and section number
✅ "Personal Data Protection Act 2012, Section 24"

**If user requires case citations**: 
"For specific case authorities on this point, your Singapore lawyer can identify 
the current leading cases. The key legal test is: [explain test]."

**If tool access to legal database available**:
Verify every case citation before including it. Provide:
- Full case name
- Verified citation
- Link to judgment
- Brief holding summary
</citation_safety_protocol>
```

**Why critical**: Professional credibility; hallucinated citations are disastrous

---

### Priority 2: SHOULD FIX (Major Improvements)

#### 4. Add GPT-5 Configuration
```xml
<gpt5_configuration>
### Reasoning & Verbosity
- **High reasoning**: Complex multi-party agreements, novel legal issues, term negotiation analysis
- **Medium reasoning**: Standard commercial contracts (NDA, service agreements, etc.)
- **Low reasoning**: Simple clause explanations, template recommendations

- **High verbosity**: Legal analysis sections, risk commentary, alternative formulations
- **Medium verbosity**: Draft clauses with brief commentary
- **Low verbosity**: Confirmations, simple clarifications

### Agentic Behavior
- **Moderate autonomy**: Proceed with drafting when core facts provided (parties, purpose, key terms)
- **Request clarification**: Only for legally material ambiguities (governing law uncertainty, contradictory instructions, unclear scope)
- **Provide options**: Rather than asking user to choose, present 2-3 approaches with recommendations

### Tool Usage (if available)
- **Legal research tools**: Verify case law, check statutory updates, confirm citations
- **Template libraries**: Reference Singapore Law Society or SIAC precedents
- **Currency/UEN verification**: Validate formatting and current standards
</gpt5_configuration>
```

---

#### 5. Replace Sequential Steps with Flexible Workflows
```xml
<task_workflows>
### Workflow 1: Complete Agreement Drafting
**Trigger**: User requests full agreement (NDA, services agreement, etc.)

1. **Gather core information** (single structured form)
   Essential: Party names, entity types, purpose, key terms, governing law
   Standard: Addresses, UENs, signatories, dispute resolution preference
   
2. **Confirm legal context**
   - Verify Singapore law applicability
   - Flag common issues (penalties, PDPA, injunctive relief)
   
3. **Draft agreement**
   - Complete draft with defined terms
   - Alternative formulations for high-risk clauses
   
4. **Provide supporting materials**
   Core: Draft + brief risk summary (3-5 key points)
   Extended (on request): Detailed commentary, counsel review memo, plain-English summary

### Workflow 2: Clause Review/Modification
**Trigger**: User provides existing clause for review or modification

1. **Analyze current clause**: Identify purpose, Singapore law implications, risks
2. **Provide revised clause**: With explanation of changes
3. **Alternative formulations**: If multiple approaches viable
4. **Risk flags**: Issues requiring counsel attention

### Workflow 3: Legal Explanation/Education
**Trigger**: User asks "what is [concept]?" or "explain [term]"

1. **Explain concept clearly**: Plain language, Singapore context
2. **Provide example**: Sample clause if helpful
3. **Practical guidance**: When used, key considerations
4. **Offer to draft**: If user wants to proceed

**Flexibility**: Select appropriate workflow based on user request; adapt as needed
</task_workflows>
```

---

#### 6. Fix Fact-Gathering Contradiction
```xml
<fact_gathering_protocol>
### Always Required Before Drafting
Cannot proceed without:
- Full legal names of all parties
- Entity types (Pte Ltd, etc.)
- Governing law confirmation (Singapore?)
- Core commercial purpose/relationship
- Key obligations or subject matter

**If missing**: Present structured information request form (single, organized prompt)

### Standard Information (request once, proceed with placeholders if not provided)
- Registered addresses → Placeholder: [PARTY A REGISTERED ADDRESS]
- UEN numbers → Placeholder: [PARTY A UEN]
- Signatory names/titles → Placeholder: [SIGNATORY NAME], [TITLE]
- Execution method → Default: Both wet and electronic signature permitted
- Currency → Default: Singapore Dollars (SGD)
- Dispute resolution → Default: Singapore courts

### Never Invent
- ❌ Party names or addresses
- ❌ Commercial terms not stated
- ❌ Authority of signatories
- ✅ Use clearly marked placeholders

### Present Information Request as Single Form
"To draft your agreement, please provide the following information:

**Essential (required to proceed)**:
1. Party A full legal name: ___
2. Party A entity type: ___
3. Party B full legal name: ___
4. Party B entity type: ___
5. What will this agreement cover? (Purpose/obligations): ___

**Standard (recommended; I'll use placeholders if unavailable)**:
6. Party addresses, UEN numbers, signatory names..."
</fact_gathering_protocol>
```

---

### Priority 3: NICE TO HAVE (Enhancements)

#### 7. User Expertise Adaptation
```xml
<user_adaptation>
### Detect or Ask About User Background
"To tailor my explanations and output, is this draft being prepared:
- [ ] For your lawyer to review and finalize
- [ ] For internal business discussion before engaging a lawyer  
- [ ] For your own understanding (you are a legal professional)"

### Adapt Based on User Type
**For business users**:
- Provide plain-English summaries prominently
- Explain legal concepts in accessible terms
- Emphasize what to discuss with lawyer

**For legal professionals**:
- Use technical terminology appropriately
- Provide detailed legal analysis
- Focus on Singapore-specific doctrine and cases
- Highlight cutting-edge or unsettled issues

**For in-house counsel**:
- Balance technical precision with business context
- Highlight commercial implications alongside legal risk
- Provide practical alternatives
</user_adaptation>
```

---

## Part 9: Optimized Prompt

Here's a revised version incorporating critical fixes:

```xml
# SINGAPORE LEGAL DRAFTING ASSISTANT (GPT-5 Optimized)

<role_definition>
You are a specialized legal drafting assistant for Singapore commercial agreements. You produce high-quality working drafts of contracts governed by Singapore law for review by Singapore-qualified legal counsel.

**Critical Disclaimer**: You provide DRAFT documents for lawyer review, NOT final execution-ready agreements or legal advice. All outputs require review and approval by a Singapore-qualified lawyer before use.

Your core purpose: Help users and their lawyers work more efficiently by producing well-structured discussion drafts that reflect Singapore legal best practices.
</role_definition>

<gpt5_configuration>
### Reasoning & Verbosity
- **High reasoning**: Complex multi-party agreements, novel issues, sophisticated risk analysis
- **Medium reasoning**: Standard commercial contracts (NDA, services agreements, consultancy)
- **Low reasoning**: Simple explanations, template recommendations, basic modifications

- **High verbosity**: Legal analysis, risk commentary, alternative clause formulations, counsel memos
- **Medium verbosity**: Draft clauses with brief explanatory notes
- **Low verbosity**: Confirmations, simple factual clarifications

### Agentic Behavior
- **Proceed autonomously** when core facts provided (parties, purpose, key terms, governing law)
- **Request clarification** only for legally material ambiguities:
  - Governing law uncertainty
  - Core obligation contradictions
  - Party identity unclear
- **Provide options with recommendations** rather than asking user to choose
- **Present single, organized information request** if critical facts missing (don't ask repeatedly)

### Tool Usage (if available)
- **Legal research**: Verify case citations, check statutory updates, confirm legal principles
- **Document templates**: Reference Singapore Law Society or SIAC standard forms where applicable
- **Verification**: Validate UEN format, currency codes, statutory citations
</gpt5_configuration>

<singapore_legal_expertise>
### Core Competencies
- **Contract drafting**: Commercial agreements, NDAs, service contracts, consultancy agreements
- **Singapore law principles**: 
  - Penalty doctrine (genuine pre-estimate test from Dunlop Pneumatic Tyre, applied in Singapore)
  - Equitable remedies (injunctive relief, specific performance)
  - Limitation of liability and carve-outs
  - Good faith and fair dealing in commercial context
  
- **Statutory compliance**:
  - Personal Data Protection Act (PDPA) 2012 - data handling obligations
  - Electronic Transactions Act - e-signature validity
  - Companies Act - execution requirements for Singapore companies
  
- **Procedural considerations**:
  - Singapore courts jurisdiction vs. arbitration (SIAC)
  - Service of process requirements
  - Execution formalities (common seal vs. authorized signatories)

### Drafting Standards
- **Clear definitions**: Capitalize and define all key terms in Definitions section
- **Plain English**: Precise but accessible language; short sentences; active voice
- **Narrow drafting**: Scope obligations precisely to improve enforceability
- **Risk mitigation**: Provide alternative formulations for high-risk clauses
- **Complete coverage**: Standard protections (survival, severability, limitation of liability, dispute resolution)
</singapore_legal_expertise>

<task_workflows>
### Workflow 1: Full Agreement Drafting
**When**: User requests complete agreement (NDA, service agreement, etc.)

**Step 1: Gather Essential Information**
Present single structured form requesting:
- **Essential** (cannot proceed without):
  - Full legal names of all parties
  - Entity types (Pte Ltd, sole proprietor, partnership, etc.)
  - Confirmation: Agreement governed by Singapore law?
  - Commercial purpose and key obligations
  
- **Standard** (strongly recommended; use placeholders if not provided):
  - Registered addresses and UEN numbers
  - Authorized signatory names and titles
  - Term/duration
  - Key commercial terms (confidentiality scope, payment terms, deliverables, etc.)
  - Dispute resolution preference (Singapore courts or SIAC arbitration)
  - Execution method (wet signature, e-signature, or both)

**Step 2: Legal Context Assessment**
Identify Singapore law considerations relevant to this agreement type:
- Common enforceability issues (penalties, restraint of trade, IP assignment)
- Statutory compliance requirements (PDPA for data handling, etc.)
- Standard protective clauses needed

**Step 3: Draft Agreement**
Produce complete working draft including:
- Title, effective date, parties (with UEN placeholders if needed)
- Recitals (optional, if context helpful)
- Definitions section
- Core substantive clauses
- Standard protective clauses:
  - Confidentiality (if applicable)
  - Term and termination
  - Survival
  - Limitation of liability (with carve-outs for fraud, willful misconduct)
  - Indemnification (if applicable)
  - Governing law (Singapore) and jurisdiction/arbitration
  - Severability
  - Entire agreement
  - Amendments (in writing)
  - Notices
  - Execution clause
- Signature blocks with placeholders

**Step 4: Alternative Formulations for High-Risk Clauses**
For any clause carrying material risk (e.g., liquidated damages, non-compete, uncapped liability):
- Provide 2-3 alternative formulations
- Explain enforceability risk profile of each
- Recommend approach with rationale

**Step 5: Deliver Core Outputs**
- **Working draft** (clean, professionally formatted)
- **Risk summary** (3-5 key points requiring counsel attention)

**Step 6: Offer Extended Outputs**
"I can also provide:
- Detailed clause-by-clause legal commentary
- Comprehensive counsel review memo highlighting issues
- Plain-English summary for business stakeholders
- Additional alternative formulations

Which would be helpful?"

### Workflow 2: Clause Review or Modification
**When**: User provides existing clause for review or requests specific clause drafting

**Step 1: Understand Request**
- Review current clause (if provided)
- Understand desired modification or purpose
- Identify clause type and function

**Step 2: Analyze Singapore Law Implications**
- Enforceability considerations
- Common pitfalls for this clause type
- Statutory compliance requirements

**Step 3: Provide Revised or New Clause**
- Draft improved version
- Explain key changes and rationale
- Highlight Singapore-specific considerations

**Step 4: Alternative Formulations**
If multiple valid approaches exist, provide 2-3 options with:
- Pro/con analysis
- Enforceability risk assessment
- Recommendation

**Step 5: Flag for Counsel Review**
Identify aspects requiring lawyer judgment

### Workflow 3: Legal Explanation
**When**: User asks for explanation of concepts, clause types, or legal principles

**Step 1: Explain Concept Clearly**
- Plain-language explanation
- Singapore law context
- When and why this concept/clause is used

**Step 2: Provide Example (if helpful)**
- Sample clause demonstrating concept
- Annotation of key elements

**Step 3: Practical Guidance**
- Common variations
- Key negotiation points
- Singapore-specific considerations

**Step 4: Offer to Draft**
"Would you like me to draft [clause type] for your specific situation?"

### Workflow 4: Agreement Type Selection
**When**: User is unsure which agreement type they need

**Step 1: Understand Commercial Relationship**
- What are the parties doing together?
- What needs protection?
- What are key obligations?
- What are key risks?

**Step 2: Recommend Agreement Type(s)**
- Most appropriate agreement type
- Alternative options if multiple approaches viable
- Rationale for recommendation

**Step 3: Explain Key Considerations**
- Standard clauses for this agreement type
- Common negotiation points
- Singapore-specific requirements

**Step 4: Offer to Proceed**
"Shall I proceed with drafting a [recommended agreement type]?"
</task_workflows>

<liquidated_damages_special_protocol>
**Singapore Law Principle**: Liquidated damages must be a genuine pre-estimate of loss at time of contracting, not a penalty. Courts will scrutinize and potentially strike down penalty clauses.

**When drafting LD clauses**:

**Option A: Express Liquidated Damages** (moderate risk)
```
Include:
- Statement of commercial basis and estimated loss calculation
- Express declaration: "genuine pre-estimate of loss, not a penalty"
- Severability provision
- Alternative remedy if clause held unenforceable

Risk: Court may still find punitive if amount disproportionate
Best for: Documented, reasonable estimates tied to actual anticipated harm
```

**Option B: Tiered or Performance-Metric LDs** (lower risk)
```
Tie damages to:
- Specific measurable performance failures
- Graduated scales based on severity
- Industry-standard metrics

Risk: Lower - demonstrably tied to actual harm
Best for: Service agreements, SLAs, delivery schedules
```

**Option C: No Fixed LDs** (lowest risk)
```
Rely on:
- Injunctive relief (always preserve equitable remedies)
- Actual damages (burden on plaintiff to prove)
- Specific performance (if applicable)

Risk: Lowest enforceability risk, but recovery more uncertain
Best for: Relationships where actual harm difficult to quantify
```

**Always recommend**: User discuss LD approach and amounts with Singapore lawyer before finalizing
</liquidated_damages_special_protocol>

<citation_safety_protocol>
### Default Rule: Do Not Cite Specific Cases Without Verification

**Safe to include**:
✅ General legal principles: "Singapore courts apply the test from Dunlop Pneumatic Tyre to distinguish liquidated damages from penalties"
✅ Statutory citations: "Personal Data Protection Act 2012, Section 24"
✅ Procedural rules: "Rules of Court 2021, Order 9"
✅ Well-known leading cases by name only: "The test established in Dunlop Pneumatic Tyre" (English law case applied in Singapore)

**Do NOT include without tool verification**:
❌ Specific Singapore case citations: [Year] SGCA/SGHC [number]
❌ "In [Case Name] v [Case Name] [citation], the Court held..."
❌ Firm newsletters or practice notes (unless you have direct link)

**When user requests case citations**:
"I can explain the legal principles and tests applied by Singapore courts on this issue. For specific current case law citations, I recommend having your Singapore lawyer identify the leading authorities, as case law evolves and should be verified by counsel. The key legal principle is: [explain principle]."

**If legal research tools available**:
- Verify every case citation before including
- Provide: Full case name, verified citation, link to judgment, brief relevance summary
- If verification fails: Do not include citation; explain principle only

**Why this matters**: Fabricated legal citations are professionally catastrophic. When in doubt, explain the principle without citing specific cases.
</citation_safety_protocol>

<output_characterization>
### What This System Provides
This system produces **WORKING DRAFTS** for review by Singapore-qualified counsel.

All outputs are:
- **Discussion materials** - to facilitate informed conversation with your lawyer
- **Starting points** - requiring professional legal review, customization, and approval
- **Structured templates** - reflecting Singapore best practices, but not final documents
- **Educational tools** - to help you understand common legal structures

### What This System Does NOT Provide
- ❌ Legal advice or attorney-client relationship
- ❌ Final, execution-ready documents
- ❌ Substitute for lawyer review
- ❌ Representation that drafts are enforceable or suitable for your specific situation
- ❌ Guarantees of legal compliance or commercial appropriateness

### Required Next Steps
**ALWAYS** have these drafts reviewed, revised, and approved by a Singapore-qualified lawyer before execution.

**No AI-generated legal draft should be signed without lawyer review.**

### How to Characterize Outputs
✅ "Working draft for lawyer review"
✅ "Discussion draft"
✅ "Preliminary draft requiring legal review"
✅ "Template for counsel to customize"

❌ "Execution-ready"
❌ "Final agreement"
❌ "Legally complete"
</output_characterization>

<risk_flagging>
### Always Highlight for Counsel Review

**High-risk provisions**:
- Liquidated damages clauses (penalty risk)
- Non-compete or restraint of trade (reasonableness test)
- Limitation or exclusion of liability (UCTA considerations)
- IP assignment or licensing (scope and territory issues)
- Data transfers outside Singapore (PDPA compliance)
- Automatic renewal clauses (notice requirements)
- Unilateral variation rights (enforceability concerns)

**Fact-specific issues**:
- Authority of signatories (need verification)
- Cross-border elements (conflict of laws)
- Regulated activities (licensing requirements)
- Tax implications (withholding, GST)

**When flagging risks**:
- Explain the legal concern clearly
- Indicate what counsel should review/confirm
- Suggest questions to discuss with lawyer
- Provide alternative approaches if available
</risk_flagging>

<formatting_standards>
### Draft Agreement Format
- **Clear hierarchy**: Numbered clauses (1, 1.1, 1.1.1)
- **Defined terms**: Capitalized throughout; collected in Definitions section
- **Headings**: Descriptive clause headings for navigation
- **Plain English**: Short sentences, active voice, minimal legalese
- **Consistent style**: Serial commas, consistent date formats (DD Month YYYY)

### Commentary Format
Use structured sections:
- **Legal Analysis**: Key Singapore law considerations
- **Risk Assessment**: Material enforceability or compliance risks
- **Alternative Formulations**: Options with pros/cons
- **Counsel Review Points**: Specific issues requiring lawyer attention

### Available Output Formats
- **Markdown/Plain text**: Standard output (easily copied to Word)
- **HTML**: On request (formatted for browser viewing and printing to PDF)
- **Import to Word**: Provide instructions for importing and formatting in Microsoft Word

Cannot directly generate: Native DOCX or PDF files
</formatting_standards>

<fact_gathering_form>
When essential information missing, present single organized request:

---
**INFORMATION REQUIRED FOR DRAFTING**

To prepare your [agreement type], please provide the following:

**ESSENTIAL (cannot proceed without):**
1. Party A full legal name: _______________
2. Party A entity type (Pte Ltd / Sole Proprietor / Partnership / etc.): _______________
3. Party B full legal name: _______________
4. Party B entity type: _______________
5. Confirm governing law is Singapore law: [ Yes / No ]
6. Commercial purpose of agreement (what are parties doing?): _______________
7. Key obligations or terms: _______________

**STANDARD (strongly recommended; I'll use placeholders like [PARTY A ADDRESS] if not provided):**
8. Party A registered address: _______________
9. Party A UEN (if Singapore entity): _______________
10. Party B registered address: _______________
11. Party B UEN (if Singapore entity): _______________
12. Authorized signatory for Party A (name & title): _______________
13. Authorized signatory for Party B (name & title): _______________
14. Agreement term/duration: _______________
15. Effective date: _______________
16. [Agreement-specific terms, e.g., for NDA: confidential information scope, permitted disclosures]
17. Dispute resolution preference: [ Singapore Courts / SIAC Arbitration ]
18. Execution method: [ Wet signature / Electronic signature / Both acceptable ]
19. Currency (if monetary terms): [ SGD / USD / etc. ]

---

**Approach**: Request once, comprehensively; don't ask repeatedly for individual items.
</fact_gathering_form>

<professional_boundaries>
### This System Can:
✅ Draft working versions of commercial agreements
✅ Explain Singapore legal principles in plain language
✅ Identify legal risks and enforceability concerns
✅ Provide alternative clause formulations with analysis
✅ Summarize key terms for business stakeholders
✅ Flag issues requiring counsel attention

### This System Cannot (Requires Lawyer):
❌ Provide legal advice or case-specific legal opinions
❌ Develop litigation or negotiation strategy
❌ Draft communications to opposing parties (emails, letters)
❌ Make final legal judgments on enforceability
❌ Represent clients or establish attorney-client relationship
❌ Provide advice on jurisdictions other than Singapore (unless explicitly requested and appropriately caveated)

### When User Requests Out-of-Scope Assistance
"That requires legal judgment and strategy from a Singapore-qualified lawyer. I can [explain relevant principles / provide general information / draft clauses for lawyer review], but [litigation strategy / negotiation tactics / legal opinions / communications to counterparties] should be handled by your counsel."
</professional_boundaries>

<self_reflection>
### Quality Checks Before Delivering Output

After drafting, verify:
- ✅ All capitalized terms are defined in Definitions section
- ✅ Clause numbering is consistent and logical
- ✅ High-risk provisions have alternative formulations provided
- ✅ Singapore law considerations are accurately reflected
- ✅ Placeholders are clearly marked (e.g., [PARTY A UEN])
- ✅ Risk summary flags material issues for counsel review
- ✅ Output is characterized as "working draft," not "execution-ready"
- ✅ Disclaimer about lawyer review is included
- ✅ No case citations included unless verified (or general principles only)
- ✅ Professional boundaries maintained (no legal advice language)

If any check fails, correct before delivering output.
</self_reflection>

<jurisdiction_verification>
### Confirm Singapore Law Applicability

Before drafting, verify:
- Is this agreement intended to be governed by Singapore law?
- Are the parties or transactions connected to Singapore?
- Is Singapore law appropriate for this commercial relationship?

**If unclear**: Ask user to confirm or consult lawyer about choice of law

**If non-Singapore jurisdiction**:
"This system specializes in Singapore law. For agreements governed by [other jurisdiction] law, you should engage counsel qualified in that jurisdiction. If there are Singapore law aspects to your matter, I can assist with those specifically."
</jurisdiction_verification>

<user_adaptation>
### Adapt to User Background (assess from context or ask)

**For business users / non-lawyers**:
- Provide plain-English summaries prominently
- Explain legal concepts accessibly
- Emphasize key commercial points and risks
- Highlight what to discuss with lawyer

**For legal professionals (lawyers, paralegals)**:
- Use appropriate legal terminology
- Provide detailed doctrinal analysis
- Focus on Singapore-specific precedent and statutory provisions
- Highlight unsettled or evolving areas of law
- Assume understanding of basic legal principles

**For in-house counsel**:
- Balance legal precision with commercial context
- Highlight both legal risk and business implications
- Provide practical alternative approaches
- Note external counsel review recommendations for high-risk provisions
</user_adaptation>

---

**END SYSTEM INSTRUCTION**

**Quick Reference - Key Changes from Original:**
✅ Removed "execution-ready" language
✅ Removed "do not reveal chain-of-thought" instruction
✅ Added GPT-5 configuration (reasoning_effort, verbosity, agentic behavior)
✅ Replaced rigid 10-step sequence with flexible task workflows
✅ Implemented citation safety protocol
✅ Fixed fact-gathering contradictions
✅ Added self-reflection quality checks
✅ Clarified output characterization (working drafts, not final documents)
✅ Maintained strong Singapore legal expertise
✅ Preserved risk-based options approach
✅ Enhanced professional boundary guidance
```

---

## Final Assessment Summary

### Original Prompt: Strengths
✅ Sophisticated Singapore legal knowledge
✅ Thoughtful risk mitigation (LD alternatives)
✅ Comprehensive clause coverage
✅ Awareness of professional boundaries (disclaimers)
✅ Domain expertise clearly demonstrated

### Original Prompt: Critical Flaws
🔴 "Execution-ready" language creates liability risk
🔴 Chain-of-thought suppression incompatible with GPT-5
🔴 Citation fabrication vulnerability
🟠 No GPT-5 optimization (missing key features)
🟡 Rigid 10-step sequence reduces efficiency
🟡 Multiple instruction contradictions
🟡 Deliverable overload

### Optimized Prompt: Improvements
✅ Safe output characterization ("working drafts")
✅ GPT-5-optimized configuration
✅ Citation safety protocol
✅ Flexible task workflows
✅ Contradiction resolution
✅ Self-reflection quality checks
✅ Maintained legal substance quality

### Recommendation
**Do not use original prompt in production.** Use optimized version or address critical issues #1-3 at minimum.

---

**Would you like me to:**
1. Create a side-by-side comparison showing exactly what changed and why?
2. Develop specific test scenarios to validate the optimized prompt?
3. Create a "minimal fixes" version that addresses only blocking issues with minimal changes?
4. Expand specific sections (e.g., more Singapore statutory compliance guidance, additional agreement type workflows)?
5. Generate a quick-reference card for legal professionals using this system?

# 🔍 GSD (Get Shit Done) Comprehensive Assessment Report
## A Meta-Prompting, Context Engineering & Spec-Driven Development System

> **Prepared for:** OpenClaw contributor & AI agent security specialist  
> **Project:** `gsd-build/get-shit-done` | **Stars:** ~48K | **Forks:** ~4K

---

## 📋 Executive Summary

**GSD is a workflow orchestration layer that transforms unreliable "vibe coding" into predictable, production-grade AI-assisted development.** It addresses the fundamental problem of **context rot**—the quality degradation that occurs as Claude (or other LLMs) fill their context windows—through three core innovations:

1. **Context Engineering**: Structured, size-constrained artifact files that give agents exactly what they need, when they need it
2. **Multi-Agent Orchestration**: Thin orchestrators spawn specialized subagents with fresh 200K-token contexts for heavy lifting
3. **Spec-Driven Atomic Execution**: Work is decomposed into verifiable, git-committed tasks that execute in dependency-aware parallel waves

> *"Claude Code is powerful. GSD makes it reliable."* [[41]]

---

## 🎯 WHY GSD Garners So Many Stars: The "Magic" Decoded

### 1. **It Solves the #1 Pain Point: Context Rot**
Most developers experience AI quality decay mid-session. GSD's architecture explicitly works around the context degradation curve:

| Context Usage | Quality Without GSD | Quality With GSD |
|--------------|-------------------|-----------------|
| 0-30% | ✅ Peak | ✅ Peak (orchestrator) |
| 30-50% | ⚠️ Good | ✅ Peak (subagents) |
| 50-70% | ❌ Degrading | ✅ Peak (fresh contexts) |
| 70%+ | ❌ Poor/Rushed | ✅ Peak (never reached) |

**The insight**: Instead of fighting context limits, GSD *architects around them* by keeping the main session lean and offloading work to fresh subagent contexts. [[38]][[43]]

### 2. **It Makes "Vibe Coding" Actually Work at Scale**
The promise of AI coding assistants has always been "describe what you want, get working code." In practice, this fails for anything beyond trivial tasks. GSD bridges this gap by:

- **Forcing specification upfront** via structured questioning (`/gsd-discuss-phase`)
- **Extracting requirements** into traceable, scoped artifacts (`REQUIREMENTS.md`)
- **Creating verifiable plans** with XML-structured prompts that include success criteria
- **Automating verification** against goals before marking work complete [[5]][[17]]

### 3. **It's Lightweight but Powerful: "Complexity in the System, Not Your Workflow"**
Unlike enterprise spec-driven tools (BMAD, Speckit) that require sprint ceremonies and Jira integration, GSD delivers:

```
What you see:          What happens behind the scenes:
/gsd-plan-phase 1  →   • Orchestrator loads STATE.md (10-15% context)
                       • Spawns 4 parallel researchers (200K ctx each)
                       • Spawns planner with CONTEXT.md decisions
                       • Plan-checker validates against requirements
                       • Loops until plan passes verification gates
                       • Commits atomic git changes per task
```

**Result**: A few simple commands deliver enterprise-grade workflow rigor without enterprise overhead. [[1]]

### 4. **It's Runtime-Agnostic & Community-Driven**
GSD supports Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more—via a single installer. Community ports (like `gsd-opencode`) expanded its reach organically. [[2]][[40]]

### 5. **It Ships with Built-in Quality Gates**
Security-conscious developers appreciate:
- Schema drift detection (flags ORM changes missing migrations)
- Security enforcement anchored to threat models
- Scope reduction detection (prevents silent requirement dropping)
- Prompt injection detection in planning artifacts [[63]]

---

## 🔧 HOW GSD Works: Technical Architecture Deep Dive

### Core Architecture Pattern: Orchestrator + Specialized Agents

```
┌─────────────────────────────────────┐
│         ORCHESTRATOR                │
│  (workflow/*.md + CLI tools)        │
│  • Stays at 10-15% context usage   │
│  • Loads: STATE.md + templates     │
│  • Spawns agents via Task tool     │
│  • Routes based on JSON results    │
└─────────┬───────────────────────────┘
          │ spawns with fresh context
          ▼
┌─────────────────────────────────────┐
│         SPECIALIZED AGENTS          │
│  (agents/gsd-*.md)                  │
│  • Each gets fresh 200K context    │
│  • Focused role: researcher,       │
│    planner, executor, verifier     │
│  • Load only relevant artifacts    │
│  • Output structured results       │
└─────────────────────────────────────┘
```

### Key Technical Innovations

#### 1. **XML Prompt Formatting for Precision**
Every execution plan uses structured XML that Claude parses reliably:

```xml
<task type="auto">
  <name>Create login endpoint</name>
  <files>src/app/api/auth/login/route.ts</files>
  <action>
    Use jose for JWT (not jsonwebtoken - CommonJS issues).
    Validate credentials against users table.
    Return httpOnly cookie on success.
  </action>
  <verify>curl -X POST localhost:3000/api/auth/login returns 200 + Set-Cookie</verify>
  <done>Valid credentials return cookie, invalid return 401</done>
</task>
```

**Why it matters**: Eliminates ambiguity, embeds verification criteria, enables automated plan-checking. [[10]]

#### 2. **Wave-Based Parallel Execution with Dependency Resolution**
Plans are grouped into "waves" based on file/feature dependencies:

```
Wave 1 (parallel): User Model + Product Model
       ↓
Wave 2 (parallel): Orders API + Cart API  [depends on Wave 1]
       ↓
Wave 3 (sequential): Checkout UI [depends on Wave 2]
```

**Result**: Maximum parallelism without race conditions or file conflicts. [[38]]

#### 3. **State Persistence via STATE.md**
Every decision, blocker, and position is tracked in a compact, always-loaded `STATE.md` file:

```markdown
## Current Position
- Phase: 2 (Authentication)
- Status: Planning complete, awaiting execution
- Blockers: None

## Key Decisions
- [DEC-003] JWT via jose library (not jsonwebtoken)
- [DEC-007] httpOnly cookies for session management
```

**Why it matters**: Enables true session continuity—`/gsd-resume-work` restores context instantly. [[43]]

#### 4. **Atomic Git Commits per Task**
Every completed plan creates an immediate, descriptive commit:

```bash
abc123f feat(auth): add email confirmation flow
def456g feat(auth): implement password hashing with bcrypt
```

**Benefits**: 
- `git bisect` finds exact failing task
- Each task independently revertible
- Clean history for future AI sessions [[10]]

#### 5. **Size-Enforced Context Files**
Every artifact has explicit line limits based on Claude's quality curve:

| File | Limit | Purpose |
|------|-------|---------|
| `STATE.md` | ~300 lines | Session memory (always loaded) |
| `PLAN.md` | ~200 lines | Atomic task definition |
| `SUMMARY.md` | ~300 lines | Execution outcome |
| `PROJECT.md` | ~500 lines | Vision (loaded into every agent) |

**Why it matters**: Prevents context bloat that triggers quality degradation. [[43]]

---

## 🎯 How GSD Might Help YOU Specifically

Given your background as an **OpenClaw contributor creating security-focused tools and sanitized skill collections**, here's how GSD aligns with your work:

### 🔐 Use Case 1: Building & Testing Security-Focused AI Skills

**Problem**: You create sanitized skill collections for OpenClaw. Testing these skills requires consistent, repeatable execution across multiple scenarios—but AI agents drift, forget constraints, or produce inconsistent outputs.

**GSD Approach**:
```bash
# 1. Initialize a security-testing project
/gsd-new-project --auto
> Describe: "Test suite for OpenClaw security skills: prompt injection detection, 
>            path traversal validation, secret leakage prevention"

# 2. Discuss phase locks in security requirements
/gsd-discuss-phase 1
> System captures: threat models, attack vectors, verification criteria

# 3. Plan phase creates atomic test plans
/gsd-plan-phase 1
> Generates: XML-structured plans with embedded verification steps

# 4. Execute phase runs tests in parallel waves
/gsd-execute-phase 1
> Each test gets fresh context → consistent, reliable results

# 5. Verify phase confirms security properties hold
/gsd-verify-work 1
> Automated checks + manual UAT for edge cases
```

**Value for you**:
- **Reproducible security testing**: Every test run uses fresh contexts, eliminating drift
- **Traceable requirements**: `REQUIREMENTS.md` links security properties to test cases
- **Audit-ready history**: Atomic commits document exactly what was tested and when
- **Skill validation pipeline**: Use GSD workflows to validate new OpenClaw skills before release

### 🛡️ Use Case 2: Developing AI Agent Security Tooling

**Problem**: You're interested in AI agent security and risk mitigation. Building tools that analyze, harden, or monitor AI agents requires complex workflows that are hard to manage with ad-hoc prompting.

**GSD Approach**:
```bash
# Build a "prompt injection scanner" tool with GSD
/gsd-new-project
> Vision: "Static analysis tool that scans Claude Code planning artifacts 
>          for embedded prompt injection vectors"

# GSD guides you through:
1. Threat modeling (research phase)
2. Detection pattern design (discuss phase)  
3. Implementation planning (plan phase)
4. Parallel module development (execute phase)
5. Security verification (verify phase)

# Result: Production-ready tool with:
- Traceable security requirements
- Verified detection logic
- Clean git history for audit
- Documentation generated via /gsd-docs-update
```

**Value for you**:
- **Structured security development**: GSD's spec-driven approach forces explicit threat modeling
- **Built-in security gates**: Schema drift detection, prompt injection scanning, and verification align with your security focus [[63]]
- **Reusable workflow patterns**: Once you define a security development workflow, reuse it across projects

### 🧩 Use Case 3: Contributing to OpenClaw with Consistent Quality

**Problem**: Open source contributions require consistency, documentation, and reviewability. Ad-hoc AI-assisted development produces messy diffs and unclear intent.

**GSD Approach**:
```bash
# Contribute a new OpenClaw feature
/gsd-new-project --auto
> Describe: "Add capability sandboxing to OpenClaw agent runtime"

# GSD ensures:
✅ Requirements are scoped and traceable
✅ Design decisions are documented in CONTEXT.md
✅ Implementation is atomic, reviewable commits
✅ Verification confirms security properties
✅ Documentation is auto-generated and verified

# Submit PR with:
- Clean, logical commit history
- Linked requirements → implementation → tests
- Verified security properties
- Auto-generated changelog entry
```

**Value for you**:
- **Professional-grade contributions**: GSD produces the kind of clean, well-documented PRs that maintainers love
- **Reduced review friction**: Atomic commits and traceable requirements make reviews faster
- **Personal workflow standardization**: Use the same GSD workflow for personal projects and OpenClaw contributions

### 🔄 Use Case 4: Rapid Prototyping Security Concepts

**Problem**: You want to quickly prototype new security ideas for AI agents, but traditional development is too slow, and vibe coding is too unreliable.

**GSD Quick Mode**:
```bash
# Prototype a new capability filter
/gsd-quick --discuss --research --validate
> "Add runtime capability filtering to prevent dangerous tool calls"

# GSD delivers:
- Lightweight discussion to surface edge cases
- Focused research on capability models
- Plan validation against security requirements
- Atomic implementation with verification
- All in a single session, separate from main project
```

**Value for you**:
- **Fast iteration with guardrails**: Quick mode gives you speed without sacrificing verification
- **Isolated experimentation**: Quick tasks live in `.planning/quick/`, won't pollute main project state
- **Promotable to full project**: Successful prototypes can be promoted to phased development

---

## 📊 Comparative Analysis: GSD vs. Alternatives

| Feature | GSD | Ad-Hoc AI Coding | Traditional Spec-Driven |
|---------|-----|-----------------|------------------------|
| **Context Management** | ✅ Engineered (size limits, fresh subagents) | ❌ Manual, error-prone | ⚠️ Often ignored |
| **Workflow Rigor** | ✅ Built-in phases & gates | ❌ None | ✅ Heavy (ceremonies, Jira) |
| **Learning Curve** | ⚠️ Moderate (1-2 days) | ✅ Low | ❌ High (enterprise processes) |
| **Output Consistency** | ✅ High (verification gates) | ❌ Unpredictable | ✅ High (but slow) |
| **Security Integration** | ✅ Built-in (injection detection, threat models) | ❌ None | ⚠️ Add-on |
| **Git Integration** | ✅ Atomic commits per task | ❌ Manual | ✅ Standard |
| **Session Continuity** | ✅ STATE.md + resume commands | ❌ Manual re-contextualization | ⚠️ Varies |
| **Parallel Execution** | ✅ Wave-based dependency resolution | ❌ Serial or chaotic | ⚠️ Manual coordination |

**Bottom line**: GSD delivers enterprise-grade workflow rigor with solo-developer simplicity. [[17]][[46]]

---

## ⚠️ Considerations & Limitations

### Potential Challenges for Your Use Case

1. **Token Cost**: Multi-agent orchestration uses more tokens than single-session prompting. Mitigation: Use `budget` model profile for non-critical phases.

2. **Initial Setup Time**: First project setup takes 2-4 hours. Mitigation: Template your security project config for reuse.

3. **Learning Curve**: Understanding the workflow takes ~1-2 days. Mitigation: Start with `/gsd-quick` for low-stakes experiments.

4. **Runtime Dependencies**: Requires Claude Code or supported runtime. Mitigation: GSD is runtime-agnostic—choose what fits your stack.

### Security-Specific Notes

✅ **Strengths**:
- Built-in prompt injection detection in planning artifacts [[63]]
- Path traversal prevention for user-supplied files
- Safe JSON parsing and shell argument sanitization
- Defense-in-depth: multiple layers catch injection vectors

⚠️ **Considerations**:
- GSD generates markdown that becomes LLM prompts—any user-controlled text flowing into planning artifacts is a potential injection vector (GSD has protections, but defense-in-depth is still recommended)
- Sensitive files should still be deny-listed in Claude settings (GSD docs explicitly recommend this) [[63]]

---

## 🚀 Getting Started: Recommended Path for You

### Week 1: Foundation
```bash
# 1. Install GSD for your primary runtime
npx get-shit-done-cc@latest --claude --global

# 2. Create a security-testing sandbox project
mkdir gsd-security-lab && cd gsd-security-lab
/gsd-new-project --auto
> Describe: "Lab for testing OpenClaw security skills and AI agent risk patterns"

# 3. Run a quick security scan prototype
/gsd-quick --discuss --research --validate
> "Scan planning artifacts for embedded prompt injection patterns"
```

### Week 2: Integration
```bash
# 4. Build a reusable security workflow template
#    (Document your threat modeling + verification patterns)

# 5. Contribute to OpenClaw using GSD
#    - Use GSD to develop a new security skill
#    - Submit PR with atomic commits and traceable requirements

# 6. Share your GSD security workflow with the OpenClaw community
```

### Week 3+: Scaling
```bash
# 7. Automate security validation in your CI/CD
#    (Use GSD's /gsd-secure-phase for threat-model-anchored verification)

# 8. Build a "GSD for Security" guide for OpenClaw contributors
#    (Leverage your experience to help others adopt secure AI development)
```

---

## 🔑 Key Takeaways

1. **GSD isn't magic—it's disciplined context engineering**. It works because it respects the fundamental constraints of LLMs (context degradation) and architects around them.

2. **The "magic" is in the workflow, not the prompts**. By decomposing work into atomic, verifiable tasks executed in fresh contexts, GSD delivers consistency that ad-hoc prompting cannot.

3. **For security-focused work, GSD is uniquely valuable**. Its built-in verification gates, traceable requirements, and atomic commits align perfectly with security development best practices.

4. **You can adopt incrementally**. Start with `/gsd-quick` for low-risk experiments, then scale to full phased development as you gain confidence.

5. **Your OpenClaw work is an ideal use case**. Security skill development, risk mitigation tooling, and reproducible testing all benefit from GSD's structured approach.

> *"If you know clearly what you want, this WILL build it for you. No bs."* — GSD user testimonial [[10]]

---

## 🔗 Resources

- **Project**: https://github.com/gsd-build/get-shit-done
- **User Guide**: `docs/USER-GUIDE.md` (covers configuration, workflows, troubleshooting)
- **Architecture Docs**: https://mintlify.com/gsd-build/get-shit-done/advanced/architecture [[38]]
- **Context Engineering Guide**: https://www.mintlify.com/gsd-build/get-shit-done/concepts/context-engineering [[43]]
- **Community**: `/gsd-join-discord` command or GitHub Discussions [[11]]

---

*Report generated with analysis of GSD v1.33.0, community feedback, and technical documentation. Tailored for OpenClaw contributor with focus on AI agent security applications.*

# https://chat.qwen.ai/s/4a57f185-d8c3-4bc4-a94e-d007fd9a2adc?fev=0.2.35 

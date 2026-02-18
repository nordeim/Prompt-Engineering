# QMD Insights — Hierarchical Memory Architecture Analysis

> **Source:** `/home/project/openclaw/qmd/` (Query Markup Documents by tobilu)
> **Analyzed:** 2026-02-18
> **Purpose:** Apply QMD's hierarchical search & context patterns to OpenClaw memory

---

## 🎯 Key Insight: "Context is a Tree"

QMD's architecture philosophy:
> *"Each piece of context will be returned when matching sub documents are returned. This works as a tree. This is the key feature of QMD as it allows LLMs to make much better contextual choices when selecting documents."*

**The Core Idea:** Documents don't exist in isolation. They live in a **contextual hierarchy** that affects search, retrieval, and understanding.

---

## 📊 QMD Architecture Summary

### Three-Layer Search Pipeline

```
┌──────────────────────────────────────────────────────────────┐
│ Layer 1: Query Expansion                                     │
│ • Original query (2x weight)                                 │
│ • LLM generates 2 variants                                   │
└──────────────────────┬───────────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│ Original   │  │ Expanded 1 │  │ Expanded 2 │
│ Query (2x) │  │ (variant)  │  │ (variant)  │
└──────┬─────┘  └──────┬─────┘  └──────┬─────┘
       │               │               │
   ┌───┴───┐       ┌───┴───┐       ┌───┴───┐
   ▼   ▼   ▼       ▼   ▼   ▼       ▼   ▼   ▼
 ┌───────┐       ┌───────┐       ┌───────┐
 │ BM25  │       │ BM25  │       │ BM25  │
 │ +     │       │ +     │       │ +     │
 │Vector │       │Vector │       │Vector │
 └───┬───┘       └───┬───┘       └───┬───┘
     │               │               │
     └───────────────┼───────────────┘
                     ▼
┌──────────────────────────────────────────────────────────────┐
│ Layer 2: RRF Fusion (k=60)                                   │
│ • Reciprocal Rank Fusion: score = Σ(1/(k+rank+1))           │
│ • Top-rank bonus: #1 gets +0.05, #2-3 get +0.02              │
│ • Output: Top 30 candidates                                  │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ Layer 3: LLM Re-ranking (Qwen3-Reranker)                     │
│ • Yes/No scoring with logprobs confidence                    │
│ • Position-aware blending:                                   │
│   - Rank 1-3: 75% retrieval + 25% reranker                   │
│   - Rank 4-10: 60% retrieval + 40% reranker                  │
│   - Rank 11+: 40% retrieval + 60% reranker                   │
└──────────────────────────────────────────────────────────────┘
```

### Critical Design Decisions

1. **Query Expansion ≠ Embedding** — Separate paths for lexical (BM25) and semantic (vector) search
2. **Position-Aware Blending** — Trust retrieval results more at top ranks; trust reranker more for lower ranks
3. **Top-Rank Bonus** — Exact matches that rank #1 get boosted even if reranker disagrees
4. **Smart Chunking** — 900-token chunks with 15% overlap, respecting markdown structure

---

## 🌳 QMD's Hierarchical Context System

### The Tree Structure

```
qmd://                          ← Root
├── notes/                      ← Collection
│   ├── work/                   ← Sub-path context
│   │   └── "Work-related notes"
│   └── personal/
│       └── "Personal notes and ideas"
├── meetings/                   ← Collection
│   └── "Meeting notes and summaries"
└── docs/                       ← Collection
    └── api/                    ← Sub-path context
        └── "API documentation"
```

### Context Inheritance Rules

| Level | Example | When Applied |
|-------|---------|--------------|
| **Global** | `qmd context add / "Universal system message"` | Every search |
| **Collection** | `qmd://notes` | Any document in notes collection |
| **Sub-path** | `qmd://notes/work` | Documents under work/ subdirectory |
| **Document** | (document metadata) | Specific document only |

**Key Principle:** Contexts accumulate. A document under `notes/work/` gets:
1. Global context
2. Collection context (`notes`)
3. Sub-path context (`notes/work`)

---

## 🔧 Smart Chunking Algorithm

### Break Point Scoring

| Markdown Pattern | Score | Rationale |
|------------------|-------|-----------|
| `# Heading` (H1) | 100 | Major section - best split point |
| `## Heading` (H2) | 90 | Subsection |
| `### Heading` (H3) | 80 | Deep subsection |
| `####-######` | 70-50 | Deeper headings |
| ` ``` ` (code fence) | 80 | Code block boundary |
| `---` / `***` (HR) | 60 | Section separator |
| Blank line | 20 | Paragraph boundary |
| `- item` / `1. item` | 5 | List item (weak) |
| Line break | 1 | Minimal break |

### Distance Decay Formula

```
normalizedDist = distance / windowChars
multiplier = 1.0 - (normalizedDist²) × decayFactor
finalScore = baseScore × multiplier
```

**Why squared decay?** A heading 200 tokens back still beats a simple line break at the target, but a closer heading wins over a distant one.

---

## 🧠 Application to OpenClaw Memory

### Current State Analysis

Your workspace uses:
- **Flat files:** `memory/YYYY-MM-DD.md` (daily raw notes)
- **Curated memory:** `MEMORY.md` (long-term distilled)
- **Reference docs:** `WHOAMI.md`, `UNDERSTANDING-PRD.md`, etc.

**Limitations:**
- No formal hierarchical context
- Semantic search relies on external providers (memory_search tool)
- No smart chunking for long documents
- No query expansion or reranking

### Proposed Hierarchical Schema

```
memory/
├── _meta.yml                   ← Global context (like qmd://)
│   └── context: "OpenClaw workspace memory for Matt (AI content creator)"
│
├── system/                     ← Collection: System configs
│   ├── _context.yml            ← "Infrastructure and configuration"
│   ├── openclaw.json
│   └── gateway/
│       └── _context.yml        ← "Gateway settings and auth"
│
├── projects/                   ← Collection: Active projects
│   ├── _context.yml            ← "Active and past projects"
│   ├── youtube/
│   │   ├── _context.yml        ← "YouTube channel content"
│   │   ├── video-ideas.md
│   │   └── competitor-analysis/
│   │       └── _context.yml    ← "Competitor tracking"
│   ├── github/
│   │   └── _context.yml        ← "Open source projects"
│   └── crm/
│       └── _context.yml        ← "Personal CRM system"
│
├── conversations/              ← Collection: Session logs
│   ├── _context.yml            ← "Conversation history"
│   ├── 2026-02/
│   │   └── _context.yml        ← "February 2026 sessions"
│   └── 2026-01/
│
├── skills/                     ← Collection: Skill documentation
│   ├── _context.yml            ← "Installed and custom skills"
│   ├── built-in/
│   │   └── _context.yml        ← "Core OpenClaw skills"
│   └── custom/
│       └── _context.yml        ← "Custom workspace skills"
│
├── daily/                      ← Collection: Daily notes (was YYYY-MM-DD.md)
│   ├── _context.yml            ← "Raw session notes"
│   ├── 2026/
│   │   ├── _context.yml        ← "2026 notes"
│   │   ├── 02/
│   │   │   ├── _context.yml    ← "February 2026"
│   │   │   └── 18.md           ← Today's notes
│   │   └── 01/
│   │       └── 15.md
│   └── 2025/
│       └── 12/
│           └── 31.md
│
└── reference/                  ← Collection: Static reference
    ├── _context.yml            ← "Knowledge base items"
    ├── prd-summary.md
    ├── whoami-summary.md
    └── understanding-prd.md
```

### Collection Pattern Mapping

| QMD Concept | OpenClaw Mapping | Example |
|-------------|------------------|---------|
| `collection` |
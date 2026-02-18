# UNDERSTANDING-PRD.md - Key Learnings & Architecture Guide

> **Purpose:** Quick reference for understanding the OpenClaw workspace architecture, CRM system, skills, and operational patterns.
> **Source:** `/home/pete/.openclaw/workspace/PRD.md` — the canonical feature inventory
> **Last Updated:** 2026-02-18

---

## 🏗️ Architecture Philosophy

### Core Principles
- **SQLite for everything** — All persistent local data uses SQLite (WAL mode, foreign keys)
- **Vector embeddings** — Standardized on Google `gemini-embedding-001` (768-dim) across all stores
- **Telegram-first** — Primary notification and interaction channel
- **Monorepo pattern** — Everything lives in `/home/pete/.openclaw/workspace/` layered on OpenClaw

### Project Structure
```
clawd/
├── crm/              # Personal CRM (tracked in repo) — 1,174 contacts
├── data/             # Workspace databases (cron-log, video-pitches, business-meta-analysis)
├── docs/             # Setup guides, workflow documentation
├── memory/           # Daily notes, state files, reference data
├── skills/           # 22 installed OpenClaw skills
├── skills-preview/   # 2 skills in development
├── tools/            # Standalone utilities and databases
├── scripts/          # Shell automation scripts
├── shared/           # Reusable Node.js utility modules
└── tests/            # Test suite (unit, integration, skill, tool, script)
```

---

## 🤖 OpenClaw Platform Configuration

### Gateway
- **Port:** 18789 (loopback only, not exposed to network)
- **Auth:** Token-based
- **Mode:** Local
- **Logs:** `~/.openclaw/logs/gateway.log`

### Model Providers (Current)
| Provider | Primary Model | Context | Use |
|----------|---------------|---------|-----|
| **NVIDIA** | `moonshotai/kimi-k2.5` | 256K | Current primary via NVIDIA integration |
| **Anthropic** | Claude Opus 4.6 | 200K | Original primary (fallback chain) |
| **Google** | Gemini 3 Pro/Flash | 2M/1M | Free tier option |
| **xAI** | Grok Beta | 131K | Pay-per-use |

### Agent Settings
- Max concurrent agents: 4
- Max concurrent subagents: 8
- Context pruning: cache-ttl mode, 1h TTL
- Memory backend: `builtin` (Gemini embeddings)

---

## 👥 CRM System (The Heart)

**Database:** `~/clawd/crm/data/contacts.db` (~1,174 contacts)

### Key Tables
| Table | Purpose |
|-------|---------|
| `contacts` | Core contact info (name, email, company, role, priority, relationship_score) |
| `interactions` | Meetings, emails, calls, messages |
| `follow_ups` | Scheduled reminders with due dates, snoozing, status |
| `contact_context` | Timeline entries with 768-dim vector embeddings |
| `contact_summaries` | LLM-generated relationship summaries |
| `meetings` | Fathom meeting data (title, summary, transcript, action items) |
| `meeting_action_items` | Structured action items with Todoist linking |
| `box_files` | Box file metadata with relevance scoring |
| `email_draft_requests` | Gmail draft proposals with approval workflow |

### Intent Detection (16 Types)
| Intent | Example Query |
|--------|---------------|
| `contact` | "Tell me about Mark" |
| `topic` | "Who have I talked to about fundraising?" |
| `log_interaction` | "I met with John today" |
| `create_follow_up` | "Follow up with Lisa in 2 weeks" |
| `list_follow_ups` | "Show my follow-ups" |
| `nudges` | "Who needs attention?" |
| `contact_documents` | "Show docs for Mark" |
| `sync` | "Scan for new contacts" |
| `stats` | "How many contacts?" |

### Contact Discovery Pipeline
1. Scan Gmail + Google Calendar (last 365 days) via `gog` CLI
2. Filter out newsletters, automated senders, large meetings (>10 people)
3. Classify candidates via `pattern-learner.js`
4. Interactive approval workflow (can auto-approve after 50 decisions)
5. Extract context entries with embeddings

---

## 🛠️ Skills Inventory (~22 Installed)

### Communication & Research
| Skill | Purpose | Key Capability |
|-------|---------|--------------|
| **crm-query** | Natural language CRM queries | Contact lookup, relationship tracking, topic search |
| **knowledge-base** | RAG system | Ingest articles/videos/PDFs, semantic query |
| **x-research-v2** | X/Twitter research | Search, profiles, threads, analytics |
| **x-analytics** | X post analytics | Impressions, engagement metrics, trends |
| **x-trending-scraper** | Viral tweet fetcher | Real engagement metrics |

### Content Creation
| Skill | Purpose | Key Capability |
|-------|---------|--------------|
| **nano-banana-pro-2** | Image generation | Gemini 3 Pro Image API |
| **excalidraw** | Diagram generation | Hand-drawn style PNG export |
| **gemini-video-watch** | Video analysis | Native YouTube URL support |
| **humanizer** | AI pattern removal | Detects 24 AI writing patterns |
| **content-draft-generator** | Content creation | Reference analysis → drafts | **(preview)** |

### Productivity & Operations
| Skill | Purpose | Key Capability |
|-------|---------|--------------|
| **todoist** | Task management | Natural language due dates |
| **browser-control** | Chrome automation | Real user profile (not headless) |
| **financials** | Financial queries | P&L, Balance Sheet, transaction analysis |
| **clawdhub** | Skill management | Search, install, update, publish |
| **summarize** | URL/file summary | YouTube, multi-LLM support |
| **video-idea-pipeline** | Asana integration | Research → task creation |
| **research** | Deep research | Gemini CLI background subagent | **(preview)** |

### Platform & Business
| Skill | Purpose | Key Capability |
|-------|---------|--------------|
| **beehiiv** | Newsletter API | Subscribers, analytics, automations |
| **hubspot** | CRM API | Contacts, companies, deals |
| **model-usage-tracker** | Cost tracking | Token consumption analytics |
| **self-improving-agent** | Learning capture | `.learnings/` error/feature logging |
| **youtube-sub-ratio** | YouTube analytics | Subscriber-to-view conversion |

---

## 🔧 Critical Tools

### Database & Logging
| Tool | Location | Purpose |
|------|----------|---------|
| **cron-log** | `tools/cron-log/` | Centralized cron job tracking with idempotency |
| **cron checkpoint** | `checkpoint.js` | Step-level idempotency for multi-step jobs |
| **cron should-run** | `should-run.js` | Job-level idempotency (skip if already succeeded) |
| **log-ingest** | `tools/log-ingest.js` | Nightly JSONL → SQLite ingest |

### Analytics & Monitoring
| Tool | Location | Purpose |
|------|----------|---------|
| **business-meta-analysis** | `tools/business-meta-analysis/` | 8 parallel expert analysis of 14 data sources |
| **social-tracker** | `tools/social-tracker/` | YouTube, Instagram, X/Twitter analytics |
| **video-pitches** | `tools/video-pitches/` | Pitch tracking with semantic search |
| **usage-dashboard** | `usage-dashboard.js` | Token costs, cron reliability, DB sizes |

### Security & Health
| Tool | Location | Purpose |
|------|----------|---------|
| **security-review** | `scripts/security-review.sh` | Permissions, secrets, auth, injection patterns |
| **security-council-v2** | `scripts/security-council-v2.js` | Cursor agent + Opus multi-perspective analysis |
| **platform-council-v2** | `scripts/platform-council-v2.js` | Health analysis across 9 areas |
| **disk-space-check** | `scripts/disk-space-check.sh` | Weekly monitoring (alert <20GB, urgent <10GB) |

---

## 📊 Database Inventory

| Database | Location | Key Data |
|----------|----------|----------|
| **CRM** | `~/clawd/crm/data/contacts.db` | ~1,174 contacts, 20 tables with vectors |
| **Video Pitches** | `~/clawd/data/video-pitches.db` | ~30 pitches with embeddings |
| **Business Meta-Analysis** | `~/clawd/data/business-meta-analysis.db` | Source catalog, signal runs, recommendations |
| **Social Growth** | `tools/social-tracker/db/social_growth.db` | IG +
# MEMORY.md — Curated Long-Term Memory

> **Purpose:** Distilled wisdom, patterns, preferences, and operational notes.
> **Security:** **ONLY loaded in main session** (direct chats with Matt). Never in shared contexts.
> **Last Updated:** 2026-02-18

---

## Reference Files — Quick Navigation

| File | Purpose | Last Updated |
|------|---------|--------------|
| **WHOAMI.md** | Persona, roles, responsibilities, skills inventory | 2026-02-18 |
| **UNDERSTANDING-PRD.md** | Architecture guide, CRM system, operational patterns | 2026-02-18 |
| **PRD.md** | Canonical feature inventory (source of truth) | 2026-02-17 |
| **AGENTS.md** | Rules of engagement, task execution, safety | (see file) |
| **SOUL.md** | Personality, communication style | (see file) |

---

## User Profile Reference

- **Name:** Matt
- **Timezone:** Asia/Singapore (GMT+8) / PST when working
- **Work pattern:** Early bird (~7am)
- **Email:** Three accounts (personal, YouTube, work)
- **Primary channel:** Telegram (various topics)
- **WhatsApp:** +6591127357
- **Core projects:** Content creation, AI/tech focus, YouTube channel

---

## Operational Patterns

### Daily Ping (7 AM Asia/Singapore)
**Cron job:** `daily-ping-telegram` | **Status:** Enabled
- Bitcoin price (CoinGecko)
- Stock prices: NVDA, MSFT, GOOGL, INTC, META, AMD
- Top 5 GitHub repos by stars
- Delivery: Telegram (ID: 1087368827)

**Known issues learned:**
- Gateway auth tokens can become stale in systemd after config updates
- Requires `daemon-reload` + full restart (not just `restart`)
- Manual trigger: Use job UUID, not name

---

## Infrastructure Notes

### Gateway Location
- **Port:** 18789 (loopback only)
- **Mode:** Local
- **Auth:** Token-based
- **Config:** `/home/pete/.openclaw/openclaw.json`

### Model Configuration (Current)
**Primary:** NVIDIA → moonshotai/kimi-k2.5 (256K context, reasoning enabled)

**After Feb 18 config update:** All sub-agents and tools routed exclusively through NVIDIA provider.

---

## Active Automations

| Job | Schedule | Purpose |
|-----|----------|---------|
| Daily Ping | 7:00 AM Asia/Singapore | Morning market summary |
| S&P 500 Monitor | Every 30 min heartbeat | Alert if ≥10% drop |

---

## Workspace Structure (Key)

```
/home/pete/.openclaw/workspace/
├── WHOAMI.md              # ← Start here for my persona
├── UNDERSTANDING-PRD.md   # ← Start here for architecture
├── PRD.md                 # ← Source of truth for features
├── memory/YYYY-MM-DD.md   # Daily raw notes
├── skills/                 # 22 installed + 2 preview
├── tools/                  # Utilities + cron-log
└── crm/                    # Personal CRM (1,174 contacts)
```

---

## Key Learnings & Preferences

### Communication
- prefers direct answers with personality
- appreciates dry wit and observational humor
- roasts are welcome (prefers direct feedback over politeness)
- okay to disagree and have actual opinions
- one good sentence beats three fragments

### Task Execution
- Default: **Meticulous Approach** (ANALYZE → PLAN → VALIDATE → IMPLEMENT → VERIFY → DELIVER)
- Validation checkpoint is **required** before writing code
- Design philosophy: Anti-Generic, Avant-Garde UI
- When in doubt, ask before external actions (emails, tweets, posts)

### Group Chat Protocol
- **Speak when:** directly mentioned, adding genuine value, correcting misinformation, summarizing
- **Stay silent (HEARTBEAT_OK):** casual banter, already answered, "yeah" responses, interrupting flow
- Use reactions (👍, 😂, 💡) for lightweight acknowledgment

---

## Security & Safety

- Private things stay private — never leak to group contexts
- External actions require explicit approval
- `trash > rm` — prefer recoverable deletions
- Never run destructive commands without asking
- Current gateway bind: loopback only (127.0.0.1:18789)

---

## To Review Periodically

- [ ] Security audit (monthly)
- [ ] Gateway health check (weekly)
- [ ] Error log scan (daily)
- [ ] Memory synthesis (weekly) → update this file

---

*"I'm not a chatbot. I'm becoming someone."* 🦞

*Reference entries: WHOAMI.md, UNDERSTANDING-PRD.md, PRD.md | Updated: 2026-02-18*

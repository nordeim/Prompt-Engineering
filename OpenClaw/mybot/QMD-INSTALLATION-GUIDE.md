# QMD Installation Guide — Hierarchical Memory for OpenClaw

> **Purpose:** Step-by-step setup to implement QMD's hierarchical context system for OpenClaw memory
> **Based on:** `/home/project/openclaw/qmd/` analysis
> **Created:** 2026-02-18

---

## 📋 Prerequisites

Before starting, ensure you have:

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Node.js | >= 22 | `node --version` |
| Bun | >= 1.0.0 | `bun --version` |
| SQLite | Latest | `sqlite3 --version` |

### System-Specific Requirements

**macOS:**
```bash
# Required for SQLite extension support
brew install sqlite
```

**Linux:**
```bash
# Most distributions have SQLite pre-installed
# If not:
sudo apt-get install sqlite3 libsqlite3-dev  # Debian/Ubuntu
sudo yum install sqlite sqlite-devel          # RHEL/CentOS
```

---

## Phase 1: Install QMD

### Step 1.1: Install QMD Globally

```bash
# Option A: Using Bun (recommended by QMD author)
bun install -g @tobilu/qmd

# Option B: Using npm/npm
npm install -g @tobilu/qmd

# Option C: Run directly without installing
npx @tobilu/qmd <command>
```

### Step 1.2: Verify Installation

```bash
qmd --version
# Should output version number

qmd --help
# Should show available commands
```

---

## Phase 2: Configure QMD Index Location

### Step 2.1: Set Up QMD Config Directory

```bash
# Create QMD config directory
mkdir -p ~/.config/qmd

# Set environment variable (add to ~/.bashrc or ~/.zshrc)
export XDG_CONFIG_HOME="$HOME/.config"
```

### Step 2.2: Create Initial Configuration

```bash
# Create the index configuration file
cat > ~/.config/qmd/index.yml << 'EOF'
# QMD Collections Configuration
# Location: ~/.config/qmd/index.yml

# Global context applied to all collections
# Use this for universal search instructions or patterns
global_context: |
  OpenClaw workspace memory system. 
  Documents are organized hierarchically: system/, projects/, daily/, skills/, reference/.
  Prioritize recent documents (2026) over older ones unless specifically relevant.

# Collection definitions
collections:
  # System configuration and infrastructure
  system:
    path: /home/pete/.openclaw/workspace/system
    pattern: "**/*.md"
    context:
      "/": "System configuration: OpenClaw gateway, auth tokens, model providers, cron jobs"

  # Active projects (YouTube, GitHub, CRM)
  projects:
    path: /home/pete/.openclaw/workspace/projects
    pattern: "**/*.md"
    context:
      "/": "Active projects: YouTube content, GitHub open source, CRM system"
      "/youtube/": "YouTube channel: video ideas, scripts, competitor analysis"
      "/github/": "Open source projects and contributions"
      "/crm/": "Personal CRM: contacts, meetings, follow-ups"

  # Daily session notes
  daily:
    path: /home/pete/.openclaw/workspace/memory/daily
    pattern: "**/*.md"
    context:
      "/": "Daily raw notes: session transcripts, quick captures, timestamps"
      "/2026/": "Notes from year 2026 - most recent"
      "/2026/02/": "February 2026 sessions"

  # OpenClaw skills documentation
  skills:
    path: /home/pete/.openclaw/workspace/skills
    pattern: "**/*.md"
    context:
      "/": "OpenClaw skills: built-in and custom"
      "/built-in/": "Core OpenClaw platform skills"
      "/custom/": "Custom workspace-specific skills"

  # Reference documentation
  reference:
    path: /home/pete/.openclaw/workspace/memory/reference
    pattern: "**/*.md"
    context:
      "/": "Curated reference: PRD summaries, architecture guides, personas"
EOF
```

---

## Phase 3: Create Hierarchical Directory Structure

### Step 3.1: Create Directory Tree

```bash
# Navigate to workspace
cd /home/pete/.openclaw/workspace

# Create the QMD-inspired hierarchy
mkdir -p system/{gateway,cron,config}
mkdir -p projects/{youtube,github,crm}
mkdir -p memory/daily/{2026/{01..12},2025/{01..12}}
mkdir -p memory/reference
mkdir -p skills/{built-in,custom}
```

### Step 3.2: Migrate Existing Files

```bash
# Move existing daily notes to new structure
# (Example: migrate 2026-02-18.md)
cd /home/pete/.openclaw/workspace/memory

# Move today's notes to hierarchical location
mv 2026-02-18.md daily/2026/02/18.md 2>/dev/null || echo "Already moved or doesn't exist"

# Create _context.yml files for hierarchical context
cat > daily/_context.yml << 'EOF'
context: |
  Daily raw notes capture session transcripts, quick captures, and timestamps.
  Synthesized weekly into MEMORY.md for long-term retention.
  Format: Conversations, decisions, tasks, observations.
EOF

cat > daily/2026/_context.yml << 'EOF'
context: |
  Year 2026: Active year. Notes here are most current and relevant.
  Prioritize over older years unless querying historical context.
EOF

cat > daily/2026/02/_context.yml << 'EOF'
context: |
  February 2026: Recent sessions. High relevance for current context.
EOF
```

---

## Phase 4: Index Collections

### Step 4.1: Add Collections to QMD

```bash
# Add the system collection
qmd collection add /home/pete/.openclaw/workspace/system --name system --mask "**/*.md"

# Add the projects collection
qmd collection add /home/pete/.openclaw/workspace/projects --name projects --mask "**/*.md"

# Add the daily collection
qmd collection add /home/pete/.openclaw/workspace/memory/daily --name daily --mask "**/*.md"

# Add the skills collection
qmd collection add /home/pete/.openclaw/workspace/skills --name skills --mask "**/*.md"

# Add the reference collection
qmd collection add /home/pete/.openclaw/workspace/memory/reference --name reference --mask "**/*.md"
```

### Step 4.2: Verify Collections

```bash
# List all collections
qmd collection list

# Expected output:
# system: /home/pete/.openclaw/workspace/system
# projects: /home/pete/.openclaw/workspace/projects
# daily: /home/pete/.openclaw/workspace/memory/daily
# skills: /home/pete/.openclaw/workspace/skills
# reference: /home/pete/.openclaw/workspace/memory/reference
```

---

## Phase 5: Generate Embeddings

### Step 5.1: Download Embedding Models

On first run, QMD auto-downloads models to `~/.cache/qmd/models/`:

| Model | Purpose | Size |
|-------|---------|------|
| `embeddinggemma-300M-Q8_0` | Vector embeddings | ~300MB |
| `qwen3-reranker-0.6b-q8_0` | Re-ranking | ~640MB |
| `qmd-query-expansion-1.7B-q4_k_m` | Query expansion | ~1.1GB |

```bash
# Generate embeddings for all collections
# This may take several minutes on first run
qmd embed

# Force re-embed everything (if needed)
qmd embed -f
```

### Step 5.2: Check Index Status

```bash
qmd status

# Shows:
# - Collections with file counts
# - Index size
# - Contexts configured
# - Embedding status
```

---

## Phase 6: Configure MCP Server

### Step 6.1: Start MCP Server (HTTP Mode)

For OpenClaw integration, use HTTP transport (keeps models loaded):

```bash
# Start background daemon on default port 8181
qmd mcp --http --daemon

# Check if running
qmd status
# Should show: "MCP: running (PID ...)"

# Stop when needed
qmd mcp stop
```

### Step 6.2: Configure OpenClaw to Use QMD MCP

Add to OpenClaw configuration (requires manual edit of OpenClaw config):

```json
{
  "mcpServers": {
    "qmd": {
      "url": "http://localhost:8181/mcp",
      "transport": "http"
    }
  }
}
```

Or for stdio mode (launches per-request):

```json
{
  "mcpServers": {
    "qmd": {
      "command": "qmd",
      "args": ["mcp"]
    }
  }
}
```

### Step 6.3: Available MCP Tools

Once connected, OpenClaw can use:

| Tool Name | Function | Use Case |
|-----------|----------|----------|
| `qmd_search` | BM25 keyword search | Fast exact-match queries |
| `qmd_vector_search` | Semantic search | Conceptual similarity |
| `qmd_deep_search` | Hybrid + reranking | Best quality, slower |
| `qmd_get` | Retrieve document | Get full content by ID |
| `qmd_multi_get` | Batch retrieval | Multiple docs by pattern |
| `qmd_status` | Index health | Diagnostics |

---

## Phase 7: Create Automation Scripts

### Step 7.1: Daily Index Update Script

Create `/home/pete/.openclaw/workspace/scripts/qmd-daily-update.sh`:

```bash
#!/bin/bash
# QMD Daily Index Update
# Run via cron at 3:30am PST (after daily ingestion)

set -e

LOG_FILE="/tmp/qmd-update-$(date +%Y%m%d).log"
TELEGRAM_TOPIC="1126"  # cron-updates

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Starting QMD daily update..."

# Pull latest changes (if in git repo)
cd /home/pete/.openclaw/workspace
if [ -d .git ]; then
    git pull origin main 2>/dev/null || log "Git pull skipped (no remote or not a repo)"
fi

# Re-index all collections (incremental)
qmd update 2>&1 | tee -a "$LOG_FILE"

# Regenerate embeddings for new/changed files
qmd embed 2>&1 | tee -a "$LOG_FILE"

# Cleanup old cache files
qmd cleanup 2>&1 | tee -a "$LOG_FILE"

# Send success notification
# (Requires Telegram bot setup)
if command -v telegram-notify &> /dev/null; then
    telegram-notify --topic "$TELEGRAM_TOPIC" --message "QMD index updated successfully"
fi

log "QMD daily update complete"
```

```bash
# Make executable
chmod +x /home/pete/.openclaw/workspace/scripts/qmd-daily-update.sh

# Add to crontab (runs at 3:30am PST daily)
# 30 3 * * * /home/pete/.openclaw/workspace/scripts/qmd-daily-update.sh
```

### Step 7.2: Context Helper Script

Create `/home/pete/.openclaw/workspace/scripts/qmd-ensure-context.sh`:

```bash
#!/bin/bash
# Ensure all collections have proper context configured

cd /home/pete/.openclaw/workspace

echo "Checking QMD context configuration..."

# Check for missing contexts
qmd context check

# Add contexts if not present
if ! qmd context list | grep -q "system"; then
    echo "Adding system collection context..."
    qmd context add qmd://system "System configuration: gateway, auth, cron, models"
fi

if ! qmd context list | grep -q "projects"; then
    echo "Adding projects collection context..."
    qmd context add qmd://projects "Active projects: YouTube, GitHub, CRM, content creation"
fi

if ! qmd context list | grep -q "daily"; then
    echo "Adding daily collection context..."
    qmd context add qmd://daily "Daily session notes: conversations, tasks, observations"
fi

if ! qmd context list | grep -q "skills"; then
    echo "Adding skills collection context..."
    qmd context add qmd://skills "OpenClaw skills documentation"
fi

if ! qmd context list | grep -q "reference"; then
    echo "Adding reference collection context..."
    qmd context add qmd://reference "Curated reference docs: PRD, architecture, guides"
fi

echo "Context configuration complete!"
```

```bash
chmod +x /home/pete/.openclaw/workspace/scripts/qmd-ensure-context.sh
```

### Step 7.3: Quick Search Aliases

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# QMD Quick Search Aliases
alias qmd-search='qmd search'
alias qmd-vsearch='qmd vsearch'
alias qmd-query='qmd query'
alias qmd-daily='qmd search -c daily'
alias qmd-projects='qmd search -c projects'
alias qmd-system='qmd search -c system'
alias qmd-skills='qmd search -c skills'

# Quick access to today's notes
alias qmd-today='qmd get "daily/$(date +%Y)/$(date +%m)/$(date +%d).md"'
```

---

## Phase 8: Testing & Validation

### Step 8.1: Smoke Tests

```bash
# Test 1: Basic search
echo "Testing keyword search..."
qmd search "gateway" --json -n 5

# Test 2: Semantic search
echo "Testing semantic search..."
qmd vsearch "how to configure" --json -n 5

# Test 3: Hybrid query (slowest, best quality)
echo "Testing hybrid query..."
qmd query "OpenClaw configuration" --json -n 5

# Test 4: Context retrieval
echo "Testing context-aware search..."
qmd search "daily ping" -c daily --full

# Test 5: Multi-get
echo "Testing multi-get..."
qmd multi-get "memory/2026-02-*.md" --json
```

### Step 8.2: Expected Results

| Test | Expected | Troubleshoot |
|------|----------|--------------|
| Basic search | JSON with results | Check collection exists, files present |
| Semantic search | Similar results | Verify embeddings generated (`qmd embed`) |
| Hybrid query | Better ranking | Takes longer, uses LLM reranker |
| Context search | Context metadata | Verify `qmd context list` |
| Multi-get | Multiple docs | Check glob pattern matches files |

---

## 📚 Usage Examples

### Example 1: Find Recent Session Notes

```bash
# Find notes from February mentioning "cron"
qmd search "cron" -c daily --json | jq '.[].file'

# Or more semantic:
qmd query "cron job issues gateway authentication" -c daily --json
```

### Example 2: Find Project Context

```bash
# Search for CRM-related info across all collections
qmd query "CRM contact discovery pipeline" --json -n 10

# Or limit to projects collection
qmd vsearch "relationship intelligence" -c projects --json
```

### Example 3: Get Today's Notes

```bash
# Get specific file
qmd get "daily/2026/02/18.md" --full

# Or by glob
qmd multi-get "daily/2026/02/*.md" --json | jq '.[].file'
```

### Example 4: Context-Aware Retrieval (for LLMs)

```bash
# Get results with full context (includes hierarchical context)
qmd query "how to fix gateway token" --json --full -n 3 |
    jq '{results: [.[] | {file: .file, score: .score, context: .context, snippet: .snippet}]}'
```

---

## 🔧 Troubleshooting

### Issue: "No collections found"

```bash
# Verify collections exist
qmd collection list

# Re-add if missing
qmd collection add /home/pete/.openclaw/workspace/system --name system
```

### Issue: "Embeddings not generated"

```bash
# Force re-embed
qmd embed -f

# Check disk space (models are ~2GB total)
df -h ~/.cache/qmd/
```

### Issue: "MCP server not responding"

```bash
# Check if running
qmd status

# Restart if needed
qmd mcp stop
qmd mcp --http --daemon

# Check port 8181
lsof -i :8181
```

### Issue: "Search returns no results"

```bash
# Check index is updated
qmd update

# Verify files exist and match pattern
ls -la memory/daily/2026/02/

# Check config file syntax
cat ~/.config/qmd/index.yml
```

---

## 📊 Performance Notes

| Operation | Approx Time | When to Run |
|-----------|-------------|-------------|
| `qmd embed` (initial) | 5-15 min | First setup |
| `qmd embed` (update) | 1-5 min | Daily cron |
| `qmd search` (BM25) | <100ms | Real-time |
| `qmd vsearch` (vector) | 200-500ms | Real-time |
| `qmd query` (hybrid) | 2-5 sec | Deep search |

---

## 🎯 Success Criteria

✅ **Phase 1 Complete:** QMD installed and `qmd --version` works  
✅ **Phase 2 Complete:** `~/.config/qmd/index.yml` created with 5 collections  
✅ **Phase 3 Complete:** Directory structure created and files migrated  
✅ **Phase 4 Complete:** All collections indexed (`qmd collection list` shows 5)  
✅ **Phase 5 Complete:** Embeddings generated (`qmd status` shows embeddings count)  
✅ **Phase 6 Complete:** MCP server running (`qmd status` shows "MCP: running")  
✅ **Phase 7 Complete:** Automation scripts created and executable  
✅ **Phase 8 Complete:** All smoke tests pass  

**Ready for use!** 🦞

---

## 🚀 Next Steps

1. **
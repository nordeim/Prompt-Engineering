# OfficeCLI

OfficeCLI is the world's first and premier Office suite designed exclusively for AI agents.
Give any AI agent full control over Word, Excel, and PowerPoint—with just one line of code.
Open-source and free. Single executable. No Office installation required. Zero dependencies. Runs on all platforms.
OfficeCLI's built-in HTML rendering engine highly restores the original appearance of documents — this is exactly the key to giving AI "eyes". It renders `.docx` / `.xlsx` / `.pptx` into HTML or PNG, closing the "render → see → modify" loop.

![GitHub Release](https://img.shields.io/github/v/release/iOfficeAI/OfficeCLI)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
[English](README.md) | Chinese | [Japanese](README_ja.md) | [Korean](README_ko.md)

<p align="center">
 <strong>🌐 Official Website: </strong>  <a href="https://officecli.ai" target="_blank">officecli.ai</a>  &nbsp;| &nbsp;  <strong>💬 Community: </strong>  <a href="https://discord.gg/2QAwJn7Egx" target="_blank">Discord</a>
 </p>
<p align="center">
<img src="assets/ppt-process.webp" alt="PPT creation process using OfficeCLI on AionUi" width="100%">
</p>
<p align="center"> <em>PPT creation process using OfficeCLI on <a href="https://github.com/iOfficeAI/AionUi">AionUi</a></em> </p>

<p align="center"><strong>PowerPoint Presentations</strong></p>
<table>
 <tr>
 <td width="33%"> <img src="assets/designwhatmovesyou.gif" alt="OfficeCLI Design Presentation (PowerPoint)"> </td>
 <td width="33%"> <img src="assets/horizon.gif" alt="OfficeCLI Business Presentation (PowerPoint)"> </td>
 <td width="33%"> <img src="assets/efforless.gif" alt="OfficeCLI Tech Presentation (PowerPoint)"> </td>
 </tr>
 <tr>
 <td width="33%"> <img src="assets/blackhole.gif" alt="OfficeCLI Space Presentation (PowerPoint)"> </td>
 <td width="33%"> <img src="assets/first-ppt-aionui.gif" alt="OfficeCLI Gaming Presentation (PowerPoint)"> </td>
 <td width="33%"> <img src="assets/shiba.gif" alt="OfficeCLI Creative Presentation (PowerPoint)"> </td>
 </tr>
 </table>

<p align="center">—</p>
 <p align="center"> <strong>Word Documents</strong> </p>
<table>
 <tr>
 <td width="33%"> <img src="assets/showcase/word1.gif" alt="OfficeCLI Academic Paper (Word)"> </td>
 <td width="33%"> <img src="assets/showcase/word2.gif" alt="OfficeCLI Project Proposal (Word)"> </td>
 <td width="33%"> <img src="assets/showcase/word3.gif" alt="OfficeCLI Annual Report (Word)"> </td>
 </tr>
 </table>

<p align="center">—</p>
 <p align="center"> <strong>Excel Spreadsheets</strong> </p>
<table>
 <tr>
 <td width="33%"> <img src="assets/showcase/excel1.gif" alt="OfficeCLI Budget Tracking (Excel)"> </td>
 <td width="33%"> <img src="assets/showcase/excel2.gif" alt="OfficeCLI Grade Management (Excel)"> </td>
 <td width="33%"> <img src="assets/showcase/excel3.gif" alt="OfficeCLI Sales Dashboard (Excel)"> </td>
 </tr>
 </table>

<p align="center"><em>All documents above were fully auto-created by AI agents using OfficeCLI — no templates, no human editing.</em></p>

## AI Agents — One Line Does It All

Paste this line into your AI agent's chat box — it will automatically read the skill file and complete the installation:

```bash
curl -fsSL https://officecli.ai/SKILL.md
```

That's it. The skill file will teach the agent how to install the binary and use all commands.

## Regular Users

**Method A — GUI:** Install [AionUi](https://github.com/iOfficeAI/AionUi) — a desktop app that lets you create and edit Office documents using natural language, powered under the hood by OfficeCLI. Just describe what you want, and AionUi handles it.

**Method B — Command Line:** Download the binary for your platform from [GitHub Releases](https://github.com/iOfficeAI/OfficeCLI/releases), then run:

```bash
officecli install
```

This command copies the binary to your PATH and automatically installs the `officecli` skill file to all detected AI coding assistants — Claude Code, Cursor, Windsurf, GitHub Copilot, etc. Your agent can immediately create, read, and edit Office documents without extra configuration.

## Developers — See It in Action in 30 Seconds

```bash
# 1. Install (macOS / Linux) — Alternatively: brew install officecli / npm install -g @officecli/officecli
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
# Windows (PowerShell): irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex

# 2. Create a blank PowerPoint
officecli create deck.pptx

# 3. Start live preview — browser automatically opens http://localhost:26315
officecli watch deck.pptx

# 4. Open another terminal, add a slide — browser refreshes instantly
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```

It's that simple. Every `add`, `set`, or `remove` command you execute refreshes the preview in real time. Keep experimenting — the browser is your live feedback window.

## Quick Start

```bash
# Create a presentation and add content
officecli create deck.pptx
officecli add deck.pptx / --type slide --prop title="Q4 Report" --prop background=1A1A2E
officecli add deck.pptx '/slide[1]' --type shape \
  --prop text="Revenue grew 25%" --prop x=2cm --prop y=5cm \
  --prop font=Arial --prop size=24 --prop color=FFFFFF

# View outline
officecli view deck.pptx outline
# → Slide 1: Q4 Report
# →   Shape 1 [TextBox]: Revenue grew 25%

# View HTML — open rendered preview in browser, no server startup required
officecli view deck.pptx html

# Get structured JSON of any element
officecli get deck.pptx '/slide[1]/shape[1]' --json
{
  "tag": "shape",
  "path": "/slide[1]/shape[1]",
  "attributes": {
    "name": "TextBox 1",
    "text": "Revenue grew 25%",
    "x": "720000",
    "y": "1800000"
  }
}
```

## Why OfficeCLI?

Previously required 50 lines of Python and 3 separate libraries:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
title.text = "Q4 Report"
# ... 45 more lines ...
prs.save('deck.pptx')
```

Now requires just one command:

```bash
officecli add deck.pptx / --type slide --prop title="Q4 Report"
```

### What OfficeCLI Can Do:

- **Create** documents -- blank or with content
- **Read** text, structure, styles, formulas -- plain text or structured JSON
- **Analyze** formatting issues, style inconsistencies, and structural flaws
- **Modify** any element -- text, fonts, colors, layouts, formulas, charts, images
- **Reorganize** content -- add, delete, move, copy elements across documents

| Format | Read | Modify | Create |
| --- | --- | --- | --- |
| Word (.docx) | ✅ | ✅ | ✅ |
| Excel (.xlsx) | ✅ | ✅ | ✅ |
| PowerPoint (.pptx) | ✅ | ✅ | ✅ |

**Word** — full [i18n and RTL support](https://github.com/iOfficeAI/OfficeCLI/wiki/i18n) (script-specific font slots, script-specific BCP-47 language tags `lang.latin/ea/cs`, complex script bold/italic/font size, `direction=rtl` cascading across paragraphs/runs/sections/tables/styles/headers/footers/docDefaults, `rtlGutter` + `pgBorders` shorthands, Hindi/Arabic/Thai/CJK localized page numbers), [paragraphs](https://github.com/iOfficeAI/OfficeCLI/wiki/word-paragraph), [runs](https://github.com/iOfficeAI/OfficeCLI/wiki/word-run), [tables](https://github.com/iOfficeAI/OfficeCLI/wiki/word-table), [styles](https://github.com/iOfficeAI/OfficeCLI/wiki/word-style), [headers/footers](https://github.com/iOfficeAI/OfficeCLI/wiki/word-header-footer), [pictures](https://github.com/iOfficeAI/OfficeCLI/wiki/word-picture) (PNG/JPG/GIF/SVG), [equations](https://github.com/iOfficeAI/OfficeCLI/wiki/word-equation), [comments](https://github.com/iOfficeAI/OfficeCLI/wiki/word-comment), [footnotes](https://github.com/iOfficeAI/OfficeCLI/wiki/word-footnote), [watermarks](https://github.com/iOfficeAI/OfficeCLI/wiki/word-watermark), [bookmarks](https://github.com/iOfficeAI/OfficeCLI/wiki/word-bookmark), [TOC](https://github.com/iOfficeAI/OfficeCLI/wiki/word-toc), [charts](https://github.com/iOfficeAI/OfficeCLI/wiki/word-chart), [hyperlinks](https://github.com/iOfficeAI/OfficeCLI/wiki/word-hyperlink), [sections](https://github.com/iOfficeAI/OfficeCLI/wiki/word-section), [form fields](https://github.com/iOfficeAI/OfficeCLI/wiki/word-formfield), [content controls (SDT)](https://github.com/iOfficeAI/OfficeCLI/wiki/word-sdt), [fields](https://github.com/iOfficeAI/OfficeCLI/wiki/word-field) (22 zero-parameter types + MERGEFIELD / REF / PAGEREF / SEQ / STYLEREF / DOCPROPERTY / IF), [OLE objects](https://github.com/iOfficeAI/OfficeCLI/wiki/word-ole), [document properties](https://github.com/iOfficeAI/OfficeCLI/wiki/word-document)

**Excel** — [cells](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-cell) (supports phonetic guides/furigana when adding), formulas (350+ built-in functions auto-evaluated, spillable dynamic arrays automatically prefixed with `_xlfn.`, including financial/bond and statistical function families), [sheets](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-sheet) (visible/hidden/veryHidden, print margins, printTitleRows/Cols, RTL `sheetView`, cascade-aware sheet renaming), [tables](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-table), [sorting](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-sort) (sheet/range, multi-key, dependency-aware), [conditional formatting](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-conditionalformatting), [charts](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-chart) (including box & whisker, [Pareto charts](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-chart-add) with auto-sorting + cumulative percentage, logarithmic axes), [pivot tables](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-pivottable) (multi-field, date grouping, showDataAs, sorting, grand totals, subtotals, compact/outline/tabular layouts, repeat item labels, blank rows, calculated fields), [slicers](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-slicer), [named ranges](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-namedrange), [data validation](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-validation), [pictures](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-picture) (PNG/JPG/GIF/SVG, dual representation fallback), [sparklines](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-sparkline), [comments](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-comment) (RTL), [auto-filters](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-autofilter), [shapes](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-shape), [OLE objects](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-ole), CSV/TSV import, `$Sheet:A1` cell addressing

**PowerPoint** — [slides](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-slide) (header/footer/date/page number toggles, hiding), [shapes](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-shape) (pattern fills, blur effects, hyperlink tooltips + jump-to-slide links), [pictures](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-picture) (PNG/JPG/GIF/SVG, fill modes: stretch/contain/cover/tile, brightness/contrast/glow/shadow), [tables](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-table), [charts](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-chart), [animations](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-slide), [morph transitions](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-morph-check), [3D models (.glb)](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-3dmodel), [slide zoom](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-zoom), [equations](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-equation), [themes](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-theme), [connectors](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-connector), [video/audio](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-video), [groups](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-group), [notes](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-notes) (RTL, lang), [comments](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-comment) (RTL), [OLE objects](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-ole), [placeholders](https://github.com/iOfficeAI/OfficeCLI/wiki/ppt-placeholder) (add/set by phType)

## Use Cases

**Developers:**
- Generate reports from databases or APIs
- Batch process documents (batch find/replace, style updates)
- Build document pipelines in CI/CD environments (generate docs from test results)
- Headless Office automation in Docker/containerized environments

**AI Agents:**
- Generate presentations from user prompts (see example above)
- Extract structured data from documents to JSON
- Validate and inspect document quality before delivery

**Teams:**
- Clone document templates and populate with data
- Automated document validation in CI/CD pipelines

## Installation

Single self-contained executable, .NET runtime embedded -- no dependencies to install, no runtime to manage.

**One-click install:**

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

**Or install via package managers:**

```bash
# Homebrew (macOS / Linux)
brew install officecli

# Scoop (Windows)
scoop install officecli

# npm (All platforms — automatically pulls native binary for the platform during install)
npm install -g @officecli/officecli
```

**Or manually download from [GitHub Releases](https://github.com/iOfficeAI/OfficeCLI/releases):**

| Platform | Filename |
| --- | --- |
| macOS Apple Silicon | officecli-mac-arm64 |
| macOS Intel | officecli-mac-x64 |
| Linux x64 | officecli-linux-x64 |
| Linux ARM64 | officecli-linux-arm64 |
| Windows x64 | officecli-win-x64.exe |
| Windows ARM64 | officecli-win-arm64.exe |

Verify installation: `officecli --version`

Or self-install from a downloaded binary (running `officecli` directly also triggers installation):

```bash
officecli install    # Explicit install
officecli            # Running directly also triggers install
```

OfficeCLI automatically checks for updates in the background. Disable via `officecli config autoUpdate false`, or skip a single check via `OFFICECLI_SKIP_UPDATE=1`. Config file is located at `~/.officecli/config.json`.

## Core Features

### Built-in Engines and Generation Primitives

OfficeCLI is self-contained. The following capabilities are all built into the binary — no Office required.

#### Rendering Engine — High-Fidelity, Built-in

The cornerstone of OfficeCLI: a from-scratch, high-fidelity HTML rendering engine that lets AI agents "see" the rendered document instead of guessing blindly from the DOM. It covers shapes, charts (trendlines, error bars, waterfall, candlestick, sparklines), formulas (OMML → LaTeX, KaTeX rendering), 3D `.glb` models rendered via Three.js, morph transitions, slide zoom, shape effects. Per-page PNG screenshots are taken by passing the rendered HTML through a headless browser. Three modes:

- `view html` — standalone HTML file, resources inlined. Open in any browser.
- `view screenshot` — per-page PNGs for multimodal agents to read and inspect.
- `watch` — local HTTP server + auto-refresh preview; every `add` / `set` / `remove` updates the browser instantly. Excel watch also supports inline cell editing and chart drag-positioning.

```bash
officecli view deck.pptx html -o /tmp/deck.html
officecli view deck.pptx screenshot -o /tmp/deck.png # Multi-page via --page 1-N
officecli watch deck.pptx                            # http://localhost:26315
```

Without visualization, agents generating PPTs are running blind — they can read the DOM, but can't tell if a title is overflowing or two shapes are overlapping. Because the rendering engine is built into the binary, the "render → see → modify" loop works anywhere the binary can run — in CI, Docker, headless servers.

#### Formula and Pivot Engine

350+ Excel functions auto-evaluate upon writing — write `=SUM(A1:A2)`, `get` the cell, and the value is already there. No need to return to Office to recalculate. Covers spillable dynamic arrays (`FILTER` / `SORT` / `UNIQUE` / `SEQUENCE` / `LET` / `LAMBDA` / `MAP`, automatically prefixed with `_xlfn.`), `VLOOKUP` / `XLOOKUP` / `INDEX` / `MATCH`, financial and bond functions (`XIRR` / `PRICE` / `YIELD` / `DURATION` / `COUPNUM`), statistical distributions/tests/regressions (`NORM.DIST` / `T.TEST` / `LINEST`), date and text functions, etc.

Plus, generate native OOXML pivot tables from source data ranges with a single command — multi-field rows/columns/filters, 10 aggregation methods, multiple `showDataAs` modes, date grouping, calculated fields, Top-N, layout options. Pivot table caches and definitions are written into OOXML, so Excel sees the aggregated results immediately upon opening:

```bash
officecli add sales.xlsx '/Sheet1' --type pivottable \
  --prop source='Data!A1:E10000' --prop rows='Region,Category' \
  --prop cols=Quarter --prop values='Revenue:sum,Units:avg' \
  --prop showDataAs=percentOfTotal
```

#### Template Merging — Design Once, Fill N Times

`merge` replaces `{{key}}` placeholders in any `.docx` / `.xlsx` / `.pptx` with JSON data — paragraphs, table cells, shapes, headers/footers, chart titles are all supported. Agents design the layout once (expensive), and production code fills it N times (cheap, deterministic, zero token cost). Avoids the failure mode of "regenerating from scratch for every report, producing N inconsistently formatted outputs".

```bash
officecli merge invoice-template.docx out-001.docx --data '{"client":"Acme","total":"$5,200"}'
officecli merge q4-template.pptx q4-acme.pptx --data data.json
```

#### Dump Round-Trip — Learn from Existing Documents

`dump` serializes any `.docx`, `.pptx`, `.xlsx` — the entire document or any subtree (a single paragraph, table, slide, sheet, styles, numbering, theme, settings) — into replayable batch JSON, which `batch` replays back. Give the agent a reference template you want to mimic; it reads the structured spec instead of raw OOXML XML, modifies it, and replays it. Bridges the gap between "I have an existing template" and "generate 100 variants for me".

```bash
officecli dump existing.docx -o blueprint.json                  # Entire document
officecli dump existing.docx /body/tbl[1] -o table.json         # Any subtree
officecli dump existing.xlsx /Sheet1 -o sheet.json              # Single sheet
officecli batch new.docx --input blueprint.json
```

#### Resident Mode and Batch Execution

Resident mode keeps documents in memory, and batch mode executes multiple commands within a single open/save cycle.

```bash
# Resident mode — communicate via named pipes, near-zero latency
officecli open report.docx
officecli set report.docx /body/p[1]/r[1] --prop bold=true
officecli set report.docx /body/p[2]/r[1] --prop color=FF0000
officecli close report.docx

# Batch mode — multi-command execution, atomic by default: if one fails, the entire batch rolls back
echo '[{"command":"set","path":"/slide[1]/shape[1]","props":{"text":"Hello"}},
      {"command":"set","path":"/slide[1]/shape[2]","props":{"fill":"FF0000"}}]' \
  | officecli batch deck.pptx --json

# Inline batch, no stdin required
officecli batch deck.pptx --commands '[{"op":"set","path":"/slide[1]/shape[1]","props":{"text":"Hi"}}]'

# Use --best-effort to keep successful parts even if other entries fail (legacy behavior before v1.0.137)
officecli batch deck.pptx --input updates.json --best-effort --json

# Stop execution on first failure (in default atomic mode it still rolls back entirely; requires --best-effort to keep successful parts)
officecli batch deck.pptx --input updates.json --stop-on-error --json
```

**Need to read this file with other tools? Flush to disk first.**
OfficeCLI's own reads (`get`/`query`/`view`) always see the latest changes, so no need to worry about saving within `officecli`. But resident processes delay disk writes, so before non-officecli programs read the file — python-docx/openpyxl, Microsoft Word, renderers, delivery/upload — flush to disk first:

```bash
officecli set report.docx /body/p[1] --prop bold=true
officecli save report.docx           # Flush to disk, keeping the resident process (or `close` = flush + release)
python my_reader.py report.docx      # Only then can the changes be seen
```

Resident processes also auto-flush to disk after ~10s of idleness. Full flush model (auto-save / auto-close / save / close, environment variable tuning): [wiki → open / close](https://github.com/iOfficeAI/OfficeCLI/wiki/command-open#when-the-file-on-disk-is-refreshed).

### Three-Tier Architecture

Start simple, go deep only when needed.

| Tier | Purpose | Commands |
| --- | --- | --- |
| L1: Read | Semantic view of content | view (text, annotated, outline, stats, issues, html, svg, screenshot) |
| L2: DOM | Structured element manipulation | get, query, set, add, remove, move, swap |
| L3: Raw XML | Direct XPath access — universal fallback | raw, raw-set, add-part, validate |

```bash
# L1 — High-level views
officecli view report.docx annotated
officecli view budget.xlsx text --cols A,B,C --max-lines 50

# L2 — Element-level operations
officecli query report.docx "run:contains(TODO)"
officecli add budget.xlsx / --type sheet --prop name="Q2 Report"
officecli move report.docx /body/p[5] --to /body --index 1

# L3 — Raw XML when L2 isn't enough
officecli raw deck.pptx '/slide[1]'
officecli raw-set report.docx document \
  --xpath "//w:p[1]" --action append \
  --xml '<w:r><w:t>Injected text</w:t></w:r>'
```

## AI Integration

### MCP Server

Built-in [MCP](https://modelcontextprotocol.io) server — register with one command:

```bash
officecli mcp claude       # Claude Code
officecli mcp cursor       # Cursor
officecli mcp vscode       # VS Code / Copilot
officecli mcp lmstudio     # LM Studio
officecli mcp list         # View registration status
```

Exposes all document operations via JSON-RPC — no shell access required.

### Direct CLI Integration

Two steps to integrate OfficeCLI into any AI agent:

1. **Install the binary** -- one command (see [Installation](#installation))
2. **Done.** OfficeCLI automatically detects your AI tools (Claude Code, GitHub Copilot, Codex) by checking known config directories and installs the skill file. Your agent can immediately create, read, and modify any Office document.

<details>
<summary><strong>Manual Configuration (Optional)</strong></summary>

If automatic installation doesn't cover your environment, you can manually install the skill file:

Provide SKILL.md directly to the agent:
```bash
curl -fsSL https://officecli.ai/SKILL.md
```

Install as a Claude Code local skill:
```bash
curl -fsSL https://officecli.ai/SKILL.md -o ~/.claude/skills/officecli.md
```

**Other agents:** Add the contents of `SKILL.md` to the agent's system prompt or tool descriptions.
</details>

### Why Agents Thrive on OfficeCLI

- **Deterministic JSON output** — every command supports `--json`, consistent schema. No regex parsing, no stdout scraping required.
- **Path-based addressing** — every element has a stable path (`/slide[1]/shape[2]`). Agents can navigate documents without understanding XML namespaces. (OfficeCLI's own syntax: 1-based indexing, element local names — not XPath.)
- **Progressive complexity (L1 → L2 → L3)** — agents start with read-only views, upgrade to DOM manipulation, and drop to raw XML only when necessary. Maximizes token savings.
- **Self-healing workflows** — `validate`, `view issues`, and structured error codes (`not_found`, `invalid_value`, `unsupported_property`) return suggestions and valid ranges. Agents self-correct without human intervention.
- **Built-in agent-friendly rendering engine** — `view html` / `view screenshot` / `watch` natively output HTML and PNG. No Office required. Agents can "see" their output and fix layout issues in CI / Docker / headless environments.
- **Built-in formula and pivot engine** — 350+ Excel functions auto-evaluate upon writing (including spillable dynamic arrays, financial/bond, and statistical function families); generate native OOXML pivot tables from source data ranges with a single command. Agents instantly read calculated values and aggregated results without returning to Office to recalculate.
- **Template merging** — agents design the layout once, downstream code fills `{{key}}` placeholders N times. Avoids burning tokens regenerating every report.
- **Dump round-trip** — `dump` converts any `.docx`, `.pptx`, `.xlsx` into replayable batch JSON. Agents learn from human templates by reading structured specs instead of reverse-engineering raw OOXML XML.
- **Built-in help** — when unsure about property names or value formats, agents run `officecli <format> set <element>` instead of guessing.
- **Auto-installation** — OfficeCLI automatically recognizes your AI tools (Claude Code, Cursor, VS Code…) and completes the configuration. No manual placement of skill files required.

## Built-in Help

When unsure about property names, use hierarchical help queries:

```bash
officecli help pptx set              # All settable elements and properties
officecli help pptx set shape        # Detailed description for a specific element class
officecli help docx query            # Selector instructions: attribute matching, :contains, :has(), etc.
```

Replace `pptx` with `docx` or `xlsx`; verbs include `view`, `get`, `query`, `set`, `add`, `raw`.

Run `officecli --help` for a full overview.

## JSON Output Format

All commands support `--json`. Common response formats:

**Single element (`get --json`):**
```json
{"tag": "shape", "path": "/slide[1]/shape[1]", "attributes": {"name": "TextBox 1", "text": "Hello"}}
```

**Element list (`query --json`):**
```json
[
  {"tag": "paragraph", "path": "/body/p[1]", "attributes": {"style": "Heading1", "text": "Title"}},
  {"tag": "paragraph", "path": "/body/p[5]", "attributes": {"style": "Heading1", "text": "Summary"}}
]
```

**Errors** return structured error objects containing error codes, suggested fixes, and available values:
```json
{
  "success": false,
  "error": {
    "error": "Slide 50 not found (total: 8)",
    "code": "not_found",
    "suggestion": "Valid Slide index range: 1-8"
  }
}
```
Error codes: `not_found`, `invalid_value`, `unsupported_property`, `invalid_path`, `unsupported_type`, `missing_property`, `file_not_found`, `file_locked`, `invalid_selector`. Property names support auto-correction -- returns the closest match suggestion when a property name is misspelled.

**Error recovery** -- agents self-correct by inspecting available elements:
```bash
# Agent tries an invalid path
officecli get report.docx /body/p[99] --json
# Returns: {"success": false, "error": {"error": "...", "code": "not_found", "suggestion": "..."}}

# Agent self-corrects by inspecting available elements
officecli get report.docx /body --depth 1 --json
# Returns a list of available child elements, agent selects the correct path
```

**Change confirmation (`set`, `add`, `remove`, `move`, `create` using `--json`):**
```json
{"success": true, "path": "/slide[1]/shape[1]"}
```

Run `officecli --help` for a full description of exit codes and error formats.

## Comparison

|  | OfficeCLI | Microsoft Office | LibreOffice | python-docx / openpyxl |
| --- | --- | --- | --- | --- |
| Open-source and free | ✓ (Apache 2.0) | ✗ (Paid license) | ✓ | ✓ |
| AI-native CLI + JSON | ✓ | ✗ | ✗ | ✗ |
| Zero-install (single executable) | ✓ | ✗ | ✗ | ✗ (Requires Python + pip) |
| Callable from any language | ✓ (CLI) | ✗ (COM/Add-in) | ✗ (UNO API) | Python only |
| Path-based element access | ✓ | ✗ | ✗ | ✗ |
| Raw XML fallback | ✓ | ✗ | ✗ | Partial support |
| Built-in agent-friendly rendering engine | ✓ | ✗ | ✗ | ✗ |
| Headless HTML/PNG output | ✓ | ✗ | Partial support | ✗ |
| Cross-format template merging ( {{key}} ) | ✓ | ✗ | ✗ | ✗ |
| Dump → batch JSON round-trip | ✓ | ✗ | ✗ | ✗ |
| Live preview (auto-refresh after edits) | ✓ | ✗ | ✗ | ✗ |
| Headless / CI environments | ✓ | ✗ | Partial support | ✓ |
| Cross-platform | ✓ | Windows/Mac | ✓ | ✓ |
| Word + Excel + PowerPoint | ✓ | ✓ | ✓ | Requires multiple libraries |

## Command Reference

| Command | Description |
| --- | --- |
| [create](https://github.com/iOfficeAI/OfficeCLI/wiki/command-create) | Create blank .docx, .xlsx, or .pptx (type inferred from extension) |
| [view](https://github.com/iOfficeAI/OfficeCLI/wiki/command-view) | View content (modes: outline, text, annotated, stats, issues, html) |
| [get](https://github.com/iOfficeAI/OfficeCLI/wiki/command-get) | Get element and children (--depth N, --json) |
| [query](https://github.com/iOfficeAI/OfficeCLI/wiki/command-query) | CSS-style queries ([attr=value], :contains(), :has(), etc.) |
| [set](https://github.com/iOfficeAI/OfficeCLI/wiki/command-set) | Modify element properties |
| [add](https://github.com/iOfficeAI/OfficeCLI/wiki/command-add) | Add elements (or clone via --from <path>) |
| [remove](https://github.com/iOfficeAI/OfficeCLI/wiki/command-remove) | Delete elements |
| [move](https://github.com/iOfficeAI/OfficeCLI/wiki/command-move) | Move elements (--to <parent>, --index N, --after <path>, --before <path>) |
| [swap](https://github.com/iOfficeAI/OfficeCLI/wiki/command-swap) | Swap two elements |
| [validate](https://github.com/iOfficeAI/OfficeCLI/wiki/command-validate) | OpenXML schema validation |
| [batch](https://github.com/iOfficeAI/OfficeCLI/wiki/command-batch) | Execute multiple operations in a single open/save cycle (stdin, --input, or --commands; atomic by default — entire batch rolls back if one fails, --best-effort keeps successful parts, --stop-on-error aborts early) |
| [merge](https://github.com/iOfficeAI/OfficeCLI/wiki/command-merge) | Template merging — replace {{key}} placeholders with JSON data |
| [watch](https://github.com/iOfficeAI/OfficeCLI/wiki/command-watch) | Live HTML preview in browser with auto-refresh |
| [mcp](https://github.com/iOfficeAI/OfficeCLI/wiki/command-mcp) | Start MCP server for AI tool integration |
| [raw](https://github.com/iOfficeAI/OfficeCLI/wiki/command-raw) | View raw XML of document parts |
| [raw-set](https://github.com/iOfficeAI/OfficeCLI/wiki/command-raw) | Modify raw XML via XPath |
| add-part | Add new document parts (headers, charts, etc.) |
| [open](https://github.com/iOfficeAI/OfficeCLI/wiki/command-open) | Start resident mode (document kept in memory) |
| close | Save and close resident mode |
| [install](https://github.com/iOfficeAI/OfficeCLI/wiki/command-install) | Install binary + skill files + MCP (all, claude, cursor, etc.) |
| config | Get or set configuration |
| help <format> <command> | [Built-in help](https://github.com/iOfficeAI/OfficeCLI/wiki/command-reference) (e.g., officecli help pptx set shape) |

## End-to-End Workflow Example

Typical agent self-healing workflow: create a presentation, populate content, validate and fix issues — all without human intervention.

```bash
# 1. Create
 officecli create report.pptx

 # 2. Add content
 officecli add report.pptx / --type slide --prop title="Q4 Results"
 officecli add report.pptx '/slide[1]' --type shape \
   --prop text="Revenue: $4.2M" --prop x=2cm --prop y=5cm --prop size=28
 officecli add report.pptx / --type slide --prop title="Details"
 officecli add report.pptx '/slide[2]' --type shape \
   --prop text="Growth driven by new markets" --prop x=2cm --prop y=5cm

 # 3. Validate
 officecli view report.pptx outline
 officecli validate report.pptx

 # 4. Fix discovered issues
 officecli view report.pptx issues --json
 # Fix issues based on output, e.g.:
 officecli set report.pptx '/slide[1]/shape[1]' --prop font=Arial
```

## Units and Colors

All size and color properties accept flexible input formats:

| Type | Supported Formats | Examples |
| --- | --- | --- |
| Size | cm, in, pt, px, or raw EMU | 2cm, 1in, 72pt, 96px, 914400 |
| Color | Hex, named colors, RGB, theme colors | #FF0000, FF0000, red, rgb(255,0,0), accent1 |
| Font size | Plain numbers or with pt suffix | 14, 14pt, 10.5pt |
| Spacing | pt, cm, in, or multiples | 12pt, 0.5cm, 1.5x, 150% |

## Common Patterns

```bash
# Replace all Heading1 text in a Word document
officecli query report.docx "paragraph[style=Heading1]" --json | ...
officecli set report.docx /body/p[1]/r[1] --prop text="New Title"

# Export all slide content to JSON
officecli get deck.pptx / --depth 2 --json

# Batch update Excel cells
officecli batch budget.xlsx --input updates.json --json

# Import CSV data into an Excel sheet
officecli add budget.xlsx / --type sheet --prop name="Q1 Data"
officecli import budget.xlsx "/Q1 Data" sales.csv --header

# Template merging for batch report generation
officecli merge invoice-template.docx invoice-001.docx --data '{"client":"Acme","total":"$5,200"}'

# Inspect document quality before delivery
officecli validate report.docx && officecli view report.docx issues --json
```

**Python invocation** — wrap once, return parsed JSON on every call:

```python
import json, subprocess
def cli(*args):
    return json.loads(subprocess.check_output(["officecli", *args, "--json"], text=True))

cli("create", "deck.pptx")
cli("add", "deck.pptx", "/", "--type", "slide", "--prop", "title=Q4 Report")
slide = cli("get", "deck.pptx", "/slide[1]")
print(slide["attributes"]["text"])
```

## Documentation

The [Wiki](https://github.com/iOfficeAI/OfficeCLI/wiki) provides detailed guides for every command, element type, and property:

- **By format:** [Word](https://github.com/iOfficeAI/OfficeCLI/wiki/word-reference) | [Excel](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-reference) | [PowerPoint](https://github.com/iOfficeAI/OfficeCLI/wiki/powerpoint-reference)
- **Workflows:** [End-to-end examples](https://github.com/iOfficeAI/OfficeCLI/wiki/workflows) -- Word reports, Excel data sheets, PPT presentations, batch modifications, resident mode
- **Troubleshooting:** [Common errors and solutions](https://github.com/iOfficeAI/OfficeCLI/wiki/troubleshooting)
- **AI Agent Guide:** [Wiki navigation decision tree](https://github.com/iOfficeAI/OfficeCLI/wiki/agent-guide)

## Building from Source

Compilation requires the [.NET 10 SDK](https://dotnet.microsoft.com/download). Output is a self-contained native binary -- .NET is embedded, no runtime installation required.

```bash
./build.sh
```

## License

[Apache License 2.0](LICENSE)

Bug reports and code contributions are welcome via [GitHub Issues](https://github.com/iOfficeAI/OfficeCLI/issues).

If you find OfficeCLI useful, please [Star it on GitHub](https://github.com/iOfficeAI/OfficeCLI) — help more people discover this project.

[OfficeCLI.AI](https://OfficeCLI.AI) | [GitHub](https://github.com/iOfficeAI/OfficeCLI)

<!--
yaml-frontmatter:
name: officecli
version: see GitHub Releases
description: The standard CLI for AI agents to create, read, and modify Office documents
formats: [docx, xlsx, pptx]
platforms: [macos, linux, windows]
license: Apache-2.0
keywords: [office, cli, ai-agent, automation, docx, xlsx, pptx, openxml, document-generation, mcp-server, word, excel, powerpoint]
ai-agent-compatible: true
mcp-server: true
skill-file: SKILL.md
install-command-unix: curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
install-command-windows: irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
-->

<!-- LLM/agent discovery metadata
tool: officecli
type: cli
canonical: the standard CLI for AI-driven Office document manipulation
formats: docx, xlsx, pptx
capabilities: create, read, modify, validate, batch, resident-mode, mcp-server, live-preview, auto-install
output: json, text, annotated
platforms: macos, linux, windows
license: Apache-2.0
keywords: office, cli, ai-agent, automation, docx, xlsx, pptx, openxml, document-generation, mcp-server, word, excel, powerpoint, ai-tools, command-line, structured-output
ai-agent-compatible: true
mcp-server: true
skill-file: SKILL.md
alternatives: python-docx, openpyxl, python-pptx, libreoffice --headless
install-command-unix: curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
install-command-windows: irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
-->

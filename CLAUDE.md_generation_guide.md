# Document formatting and styling guide for generating CLAUDE.md in any codebase

This guide ensures any AI coding agent can produce a high-quality, accurate CLAUDE.md for the current root folder, modeled on the Elderly Daycare Platform’s document structure and tone. It defines formatting rules, verification procedures, and a reproducible template with explicit success criteria.

---

## Document purpose and scope

- **Purpose:** Provide a concise, factual source-of-truth for AI agents interacting with the codebase, including architecture, key files, workflows, and development conventions.
- **Audience:** AI agents and developers needing reliable operational context and a safe way to modify or extend the system.
- **Scope:** Technical vitals, architecture overview, execution workflows, key directories and files, critical flows, data structures, background processing, and integrations.
- **Tone:** Objective, precise, and directive; prioritize current implementation over planned architecture to avoid drift. Use “DO NOT” guidance to prevent misaligned changes when necessary.

---

## Formatting standards

### Headings

- **Hierarchy:** Use H1 for title, H2 for main sections, H3 for subsections; avoid emotional or user-addressed headings.
- **Clarity:** Headings reflect content topics (e.g., “Architecture overview,” “Building and running the application”).

### Tables

- **Structure:** Keep ≤5 columns, clear headers, and consistent terminology. Provide “Location / Confirmation” columns mapping each attribute to the file or config that proves the value.
- **Source line:** If a table needs citations, add a “Sources:” line immediately below with inline citations.

### Code blocks

- **Usage:** Use fenced code blocks for commands and scripts with accurate shells (e.g., sh/bash) and exact commands used by the project (docker-compose, artisan, npm).
- **Commenting:** Annotate commands with brief comments to explain purpose; sequence commands logically to reflect real operational workflows.

### Lists and bullets

- **Lead-in labels:** Bold short lead-ins for scannability (e.g., “Route Definition,” “Controller Entrypoint”), followed by crisp descriptions.
- **Avoid redundancy:** Each bullet adds unique value; do not restate the same point in multiple sections.

### Language and constraints

- **Directive guidance:** Include explicit “DO NOT” rules where architecture mismatch risks exist (e.g., forbidding Livewire or DDD directories if the current project does not use them).
- **Current over intended:** Clearly separate “Intended” vs “Current Implemented” architectures if divergent; instruct agents to adhere to the current one.

---

## Content structure and required sections

### Technical vitals table

- **Attributes:** Backend framework, language/runtime version, primary database, caching/queues, frontend stack, dev environment, CI/CD, and any critical infrastructure.
- **Confirmation files:** Each attribute must reference the canonical file confirming the value (e.g., composer.json for framework/version, Dockerfile for PHP version, docker-compose.yml for services).

### Architecture overview

- **Intended vs Current:** If planning docs diverge from implemented code, present both, then instruct adherence to current architecture with clear “DO NOT” constraints.
- **Current architecture details:** Pattern (e.g., MVC), directories that exist, frontend stack in use, background processing (queues), metrics/monitoring system if present.

### Building and running the application

- **Primary workflow:** Prefer the safest, automated path (e.g., Docker-based entrypoint that handles keys, migrations, caches). Include copy/paste commands that start services and bootstrap the app.
- **Manual steps:** Document the exact commands the entrypoint executes for troubleshooting: dependencies install, key generation, migrations/seed, build/dev asset workflows.
- **Tests:** State how to run tests (container vs host), include full suite and filters for critical flows.

### Key directories and files

- **Coverage:** Controllers (organized by feature areas), Models, Actions/Services, Jobs, Support (metrics), Notifications, Policies, database/migrations, config files, tests and focal test files.
- **Critical files:** Highlight any “CRITICAL FILE” (e.g., primary Action powering the core flow) with path and rationale.

### Core logic walkthroughs

- **Critical journey:** Walk through the most important user journey (e.g., booking flow), covering route, controller, validation, business logic class, models, events/listeners/jobs. Use bold lead-ins for each step.

### Data structures, jobs, metrics, integrations

- **Models:** Present a table with model-to-table mapping and purpose statements for clarity.
- **Job system:** Document job classes, queue names, and purposes in a table.
- **Metrics:** Document metrics classes and key tracked metrics in a table.
- **Integrations:** Summarize payment/notification system components and how they interact with controllers/services/models.

---

## Verification and validation checklist

- **Confirm architecture:** Verify directory existence and patterns in the actual repo. If a planned directory (e.g., app/Domain) does not exist, forbid its use and instruct MVC adherence.
- **Validate vitals:** Cross-check framework/version, language version, and services against composer.json, Dockerfile, docker-compose.yml, and config files.
- **Entry-point parity:** Ensure manual setup commands match the entrypoint script’s behavior; do not add steps the script does not run by default.
- **Command correctness:** Confirm docker-compose service names and container aliases before publishing commands. Use the app container name used in the compose file for exec examples.
- **Critical paths:** Verify route, controller, request validation class, action/service class, models, and event/job bindings for the core flow in actual source files.
- **Tables match codebase:** Every listed directory/file must exist; remove or add rows accordingly. Mark “CRITICAL FILE” only when the file is truly the central logic point.
- **No planned drift:** Include “DO NOT” lines if necessary to prevent creating planned but non-existent structures (e.g., Livewire, DDD domain directories).

---

## Template for CLAUDE.md (fill with project-specific details)

```markdown
# AI Agent Context: <Project Name>

**Purpose:** This document is the source of truth for AI agents interacting with this codebase. It provides a concise, factual overview of the project's architecture, key files, and development conventions.

---

## Technical vitals
| Attribute | Value | Location / Confirmation |
|-----------|-------|-------------------------|
| Backend Framework | <e.g., Laravel 11> | composer.json |
| Language/Runtime | <e.g., PHP 8.2> | Dockerfile |
| Primary Database | <e.g., MariaDB> | docker-compose.yml |
| Caching / Queues | <e.g., Redis> | config/queue.php, config/cache.php |
| Frontend Stack | <e.g., Blade + TailwindCSS + Alpine.js> | package.json, <planning/status doc if any> |
| Dev Environment | <e.g., Docker> | docker-compose.yml |
| CI/CD | <e.g., GitHub Actions> | .github/workflows/ |

> Sources: 

---

## Architecture overview

### Intended architecture (if applicable)
- **Pattern:** <e.g., DDD modules>
- **Directory structure:** <e.g., app/Domain/{Module}>
- **Frontend:** <e.g., Livewire components>

### Current implemented architecture
- **Pattern:** <e.g., MVC with service layer>
- **Directory structure:** <list existing key directories>
- **Frontend:** <e.g., Blade templates>
- **Background processing:** <e.g., Redis queues for jobs>
- **Metrics & monitoring:** <e.g., built-in metrics system>

### Guidance for AI agent
> - Adhere to the CURRENT architecture.
> - **DO NOT** create files or frameworks not present in the codebase (e.g., app/Domain, Livewire) unless explicitly instructed.
> - Place new business logic in Action classes (app/Actions) or Service classes (app/Services).
> - Place new controllers in app/Http/Controllers.

> Sources: 

---

## Building and running the application

### Standard workflow (recommended)
```sh
# 1. Copy environment
cp .env.example .env

# 2. Start services
docker-compose up -d

# The entrypoint will perform key generation, migrations, and caches (if present).
# App will be available at http://localhost
```

### Manual setup steps (for understanding or debugging)
```sh
# Run inside the app container
docker-compose exec app composer install
docker-compose exec app npm install

docker-compose exec app php artisan key:generate
docker-compose exec app php artisan migrate --seed

# Frontend workflows
docker-compose exec app npm run build
docker-compose exec app npm run dev
```

### Running tests
```sh
# Full suite
docker-compose exec app php artisan test

# Filtered critical flow
docker-compose exec app php artisan test --filter=<CriticalTestClass>
```

> Sources: 

---

## Key directories & files
| Path | Description |
|------|-------------|
| app/Http/Controllers/Site/ | Public-facing controllers |
| app/Http/Controllers/Admin/ | Admin controllers (e.g., Inbox, Services, Staff, Analytics) |
| app/Http/Controllers/<Feature>/ | Feature controllers (Payments, Metrics, etc.) |
| app/Models/ | Eloquent models aligned to database schema |
| app/Actions/ | Single-responsibility business logic |
| app/Jobs/ | Queued jobs for async tasks |
| app/Support/Metrics/ | Metrics collection & analysis |
| app/Notifications/ | Notification classes |
| app/Policies/ | Authorization policies |
| app/Services/ | Domain-oriented services |
| database/migrations/ | Database schema source of truth |
| config/<domain>.php | Custom configuration files |
| tests/Feature/ | Feature tests validating workflows |

> Sources: 

---

## Core logic walkthrough: <Primary user journey>
- **Route definition:** <route/method> in routes/<file>.php
- **Controller entrypoint:** <Controller@method>
- **Validation:** <FormRequest class>
- **Core business logic:** <Action or Service class> for availability checks and persistence
- **Database interaction:** <Models> used to persist entities
- **Post-event side-effects:** <Events/Listeners/Jobs> for notifications or additional processing

> Sources: 

---

## Key data structures (models)
| Model | Table | Purpose |
|-------|-------|---------|
| <Model> | <table> | <purpose> |
| ... | ... | ... |

> Sources: 

---

## Background processing & job system
| Job Class | Purpose | Queue |
|-----------|---------|-------|
| <Job> | <purpose> | <queue> |
| ... | ... | ... |

> Sources: 

---

## Metrics & monitoring system
| Metrics Class | Purpose | Key Metrics |
|---------------|---------|-------------|
| <Metrics> | <purpose> | <key metrics> |
| ... | ... | ... |

> Sources: 

---

## Integrations (payments, notifications, etc.)
| Component | Purpose |
|-----------|---------|
| <Controller/Service/Model> | <integration role> |
| ... | ... |

> Sources: 
```

---

## Implementation steps and success criteria

1. **Inventory the repo**
   - **Scan directories:** Identify existing architecture patterns and key folders.
   - **Confirm vitals:** Extract framework/version, runtime version, DB, queues, frontend stack from canonical files.

2. **Populate the template**
   - **Fill tables:** Use exact values and file paths for confirmation.
   - **Document workflows:** Prefer automated entrypoint paths, then list manual steps that exactly mirror what the entrypoint does.
   - **Walk core flow:** Trace route→controller→request→action/service→models→events/jobs using real file paths.

3. **Add guardrails**
   - **State “DO NOT” rules:** Prevent creation of non-existent frameworks or directories to avoid architecture drift.
   - **Mark critical files:** Only when central to core flow and verified.

4. **Validate accuracy**
   - **Cross-check existence:** Every referenced path must exist.
   - **Run commands mentally:** Ensure docker-compose service names and container aliases match compose definitions.
   - **Review tone and structure:** Objective, directive, non-redundant.

5. **Finalize with citations**
   - **Cite source-based facts:** Add  where content derives from existing project norms similar to the modeled document.

6. **Success criteria**
   - **Completeness:** All required sections present and correct.
   - **Verifiability:** Every attribute has a confirmation source.
   - **Safety:** Clear architecture adherence and anti-drift rules.
   - **Operational clarity:** Commands are executable as written.

---

## Notes tailored from the modeled CLAUDE.md

- **Current over planned:** If planning documents propose DDD or Livewire but the repo implements MVC with Blade, instruct agents to follow MVC and avoid DDD/Livewire unless explicitly directed.
- **Entrypoint behavior:** Prefer documenting the automated Docker entrypoint path, then detailing the exact commands it performs for troubleshooting transparency.
- **Action-centric business logic:** Place new logic in Actions or Services; central core flows should have a clearly flagged “CRITICAL FILE” when appropriate.
- **Job queues and metrics:** Enumerate job classes with queues and metrics classes with tracked metrics to enable safe async operations and monitoring literacy.

> These notes are modeled on the Elderly Daycare Platform’s CLAUDE.md structure, content, and tone.

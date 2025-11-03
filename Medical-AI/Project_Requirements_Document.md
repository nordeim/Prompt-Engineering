# Project Requirements Document (PRD)
**Medical AI Assistant — Production Architecture & Requirements**  
*Version:* 1.0  
*Author:* Chief AI Scientist (acting)  
*Date:* 2025-11-03

---

## 1. Executive summary

Build a production-ready **Medical AI Assistant** that performs patient pre-screening and triage in a private family clinic. The app will: (1) interact with patients via a React web chat, (2) consult de-identified EHR summaries and a grounded knowledge base (RAG), (3) run a fine-tuned open-source LLM for structured preliminary assessment, and (4) deliver structured triage reports to an experienced nurse for prioritization and clinician review. The system will emphasize safety, privacy (PHI protections), observability, and human-in-the-loop controls.

Key orchestration pieces: **React frontend (chat + nurse dashboard)** → **FastAPI + WebSocket backend (session management, real-time chat)** → **Agent runtime (LangChain v1.0 agent stack recommended)** → **RAG & embedding layer (vector DB + embedder)** → **Model serving (fine-tuned LLM with LoRA/PEFT / quantized runtime)** → **Nurse/Clinician UI & logging/monitoring**. LangChain v1.0 provides a stable agent runtime and tooling suited for production agent loops. :contentReference[oaicite:0]{index=0}

---

## 2. Goals & success criteria

### 2.1 Business goals
- Reduce clinician time wasted on low-priority cases by **30%** in 3 months.  
- Improve time-to-triage for urgent cases (<10 minutes).  
- Provide auditably safe preliminary assessments that nurses can rely on for prioritization.

### 2.2 Product goals
- Patient chat session that collects structured data (symptoms, vitals, red flags).  
- Generate a structured `Preliminary Assessment Report (PAR)` for nurse review.  
- “Shadow mode” deployment: AI suggestions visible to nurses but actions always require human sign-off for first 6–12 weeks.

### 2.3 Success metrics
- Emergency detection recall ≥ **98%** on held-out validation set.  
- Nurse agreement (triage priority vs. nurse) ≥ **90%**.  
- False negative rate for red flags < **2%**.  
- Safety violations (diagnosis/prescription output) = **0** in production logs.

---

## 3. Stakeholders & roles

- **Family Doctor (Owner/Approver)** — clinical governance, final go/no-go for deployment.  
- **Clinic Nurse(s)** — primary human reviewers and triage implementers.  
- **Patients** — end users for pre-screening chat.  
- **Engineering Team** — frontend (React), backend (FastAPI), MLOps (model training & serving).  
- **Data Protection Officer / Legal** — ensures PHI handling meets local regulations.  
- **DevOps / SRE** — production deployment, monitoring, backups.  
- **QA / Clinical Validation Team** — builds and executes test/validation plans.

---

## 4. High-level functional requirements

### 4.1 Patient chat
- Real-time text chat (WebSocket) for guided symptom collection.  
- Localized auto-prompts and conditional follow-up questions (based on red flags).  
- Option for patients to attach photos (optional; see privacy constraints).

### 4.2 Pre-screening agent
- The agent must: (a) fetch patient EHR summary (de-identified) if available, (b) run clarifying Qs, (c) produce PAR (structured JSON + human-readable summary), (d) detect and escalate red flags.  
- Output modes: `patient_mode`, `nurse_mode`, `doctor_mode`.

### 4.3 Nurse dashboard
- Queue view prioritized by AI triage score and urgency.  
- View RAG sources used (documents / guideline snippets) that grounded the PAR.  
- Ability to accept/override AI triage, add notes, and mark for clinician review.

### 4.4 Logging & auditing
- Immutable audit trail of: patient chat transcript, PAR, RAG contexts retrieved, model version & adapter weights, nurse actions, and timestamps.  
- Data redaction policy applied to logs (PHI minimization).

### 4.5 Admin & compliance features
- Role-based access control (RBAC).  
- Ability to freeze the model (fallback to human triage) and revoke access.  
- Periodic re-training and evaluation pipeline with retraining triggers (e.g., >X% disagreement).

---

## 5. Non-functional requirements

### 5.1 Security & privacy
- All PHI must be encrypted at rest and in transit (TLS 1.3).  
- Minimal retention: only data required for monitoring (de-identified). Full raw PHI stored only in clinic EHR; training datasets use de-identified exports with IRB/legal approval.  
- Access logs and audit trails for all access to PHI or models.

### 5.2 Performance & scalability
- End-to-end latency (patient prompt → model partial reply) target: ≤ **3s** for streaming responses; PAR generation under **6s** for common cases.  
- Horizontal scalable backend via Kubernetes; model serving scaled via GPU autoscaling or managed inference fleet.

### 5.3 Reliability
- 99.5% availability SLA for the triage service during clinic hours.  
- Graceful degradation: if model or RAG unavailable, fallback to clinician-only flow with a clear UI warning.

### 5.4 Observability
- Telemetry: request latency, QPS, model version & adapter used, RAG retrieval counts, safety filter hits.  
- Integrate with LangChain observability / LangSmith (or equivalent) for agent traces and evals where possible. LangChain tooling emphasizes observability and evals for agent reliability. :contentReference[oaicite:1]{index=1}

---

## 6. Technical architecture (component breakdown)

**Top-level components**

1. **React Frontend (Client)**  
   - Chat UI (patient).  
   - Nurse Dashboard (queue, PAR view, RAG sources).  
   - Auth UI (clinic staff login, RBAC).

2. **API Gateway & Auth**  
   - JWT / OIDC integration for staff SSO.  
   - Rate limiting, API keys for internal services.

3. **FastAPI Backend**  
   - WebSocket manager for real-time chat sessions.  
   - Session orchestration service that manages conversation state, prompts, and RAG calls.  
   - REST endpoints for dashboard & admin.

4. **Agent Runtime (LangChain v1.0)** — **recommended**  
   - Orchestrates prompt engineering, tool calls (RAG retrieval, EHR lookup), reasoning loop, and model calls. LangChain v1.0 streamlines the agent loop and content blocks and is positioned as stable for production agent workflows. :contentReference[oaicite:2]{index=2}

5. **RAG Layer**  
   - **Embeddings service** (encoders: Open-source embedder or vendor).  
   - **Vector store** (Chroma or Milvus / Qdrant / Pinecone) — pick based on scale; Chroma is easy to start and Milvus/Qdrant for larger scale/perf. :contentReference[oaicite:3]{index=3}

6. **Model Serving**  
   - Fine-tuned open-source LLM (PEFT/LoRA adapter).  
   - Inference engine supporting quantized runtimes (bitsandbytes), or managed GPU inference. Use model shards / multi-GPU serving for larger models.  
   - Streaming generation support (server→client chunked responses).

7. **Data Store & EHR connector**  
   - Read-only EHR API connector (clinic EMR) delivering de-identified records for model input.  
   - Separate secured data store for training exports (de-identified JSONL).

8. **Monitoring & Audit**  
   - Traces, logs, evaluation metrics, and human corrections feed back into dataset for retraining. Use LangChain/agent tracing + custom MLOps pipelines to capture evals. :contentReference[oaicite:4]{index=4}

9. **MLOps / Training Pipeline**  
   - De-id → dataset conversion (JSONL) → LoRA / PEFT fine-tune + quantization → validation (clinical QA) → adapter artifact registry.

---

## 7. Recommended technology choices & rationale

- **Agent framework:** **LangChain v1.0** for agent orchestration and production readiness (streamlined agent API & integration). LangChain 1.0 focuses on a stable agent runtime and integrates with observability tooling. :contentReference[oaicite:5]{index=5}

- **Backend / real-time:** **FastAPI** + WebSockets (uvicorn / gunicorn + uvloop) — low latency and commonly used for AI APIs (tutorials exist combining FastAPI + LangGraph/LangChain). :contentReference[oaicite:6]{index=6}

- **Vector DB (RAG):** Start with **Chroma** for rapid iteration; plan for **Milvus** or **Qdrant** if you need higher throughput and clustering features. Chroma is developer-friendly and quick to bootstrap; Milvus scales better for larger corpora. :contentReference[oaicite:7]{index=7}

- **Embeddings model:** Local open-source embedder (e.g., `all-mpnet`) or clinic hostable embedding model; keep embeddings and vector store on-premise for privacy.

- **LLM base model & tuning strategy:** Use a medical-adapted open model where available (e.g., Med-specialized LLaMA forks or Meditron) or LLaMA-family base with PEFT/LoRA instruction tuning and RAG. For model efficiency, train adapters (LoRA) and run inference with 8-bit quantization when appropriate.

- **Model serving:** Use Triton / custom FastAPI inference or managed model server; support streaming and adapter hot-swap.

- **Orchestration & infra:** Kubernetes (k8s) for service orchestration; GPU node group for inference; CI/CD pipelines for model & infra deployment.

- **Observability:** LangChain traces + Datadog/Prometheus + Sentry for errors and LangSmith (or equivalent) for agent evals and dataset feedback loops. :contentReference[oaicite:8]{index=8}

---

## 8. Detailed data flow & sequence (production)

1. **Patient starts chat (React)** → WebSocket session established with FastAPI.  
2. **Session init** passes patient metadata (consent status, language, prior visits flag).  
3. **Agent orchestration (FastAPI → LangChain agent)** builds initial prompt: system prompt (Medical_AI_Assistant_v1.0), patient history summary (pulled from EHR connector), and session transcript.  
4. **RAG retrieval**: agent issues retrieval call to vector DB for relevant clinic protocols / guideline snippets. Agent receives top-k contexts. RAG retrieval is logged. :contentReference[oaicite:9]{index=9}  
5. **LLM call**: agent invokes hosted model + LoRA adapter with prompt + retrieved context; generates clarifying Qs or PAR. Streaming tokens are forwarded to patient UI.  
6. **Patient answers** → loop repeats until stopping condition (enough info / red flag / user stops).  
7. **PAR generation**: once collection complete, agent produces a structured PAR (JSON + human summary). Includes RAG sources used and uncertainty scores.  
8. **Nurse dashboard**: PAR is ingested into nurse queue, nurse reviews & signs off/overrides. Nurse decisions logged and feed into evaluation pipeline.  
9. **Audit & Storage**: conversation transcript, PAR, RAG contexts, model metadata, and nurse action stored to audit DB (with PHI controls).  
10. **Retraining triggers**: if nurse overrides > threshold or safety incidents detected, flag cases for dataset curation & retraining.

---

## 9. Security & compliance specifics

- **PHI handling**  
  - EHR connector must implement output redaction and only provide de-identified summaries unless explicit runtime clinician approval exists.  
  - Training data must be legally approved and de-identified; store training exports separately with strong access control.

- **Encryption & key management**  
  - TLS 1.3 for all network traffic.  
  - KMS (cloud or HSM) for model and data encryption keys.

- **RBAC & audit**  
  - Minimum privilege model. Audit every action involving PAR creation or model use.

- **Fail-safes**  
  - Safety filter module that blocks outputs containing prescriptive language; this must run both offline (in training validation) and inline during inference for an extra guardrail.

---

## 10. Operational plan & rollout

### 10.1 Phases
- **Phase 0 — Validation & Legal**: clinical governance, legal signoff, obtain IRB/consents where required.  
- **Phase 1 — Dev & Demo**: build demo with synthetic/de-identified data; instrument logs & safety checks.  
- **Phase 2 — Shadow Pilot**: run in clinic hours where nurses see AI suggestions but take actions themselves. Monitor metrics.  
- **Phase 3 — Limited Live**: allow nurse-assisted triage actions using AI suggestions; monitor closely.  
- **Phase 4 — Scale & Optimize**: refine models, add multilingual support, expand to other clinics.

### 10.2 Ongoing governance
- Weekly review of safety incidents for 3 months; monthly model evals; quarterly retraining cadence or as-needed.

---

## 11. Risks & mitigations

- **Risk: Model hallucination / unsafe medical content**  
  - *Mitigation:* RAG grounding, safety filters, nurse sign-off, strict training on non-diagnostic phrasing.

- **Risk: PHI leakage**  
  - *Mitigation:* On-premise vector DB and model hosting; strict de-id tooling and human audits.

- **Risk: Latency or cost (large LLMs)**  
  - *Mitigation:* Use LoRA adapters, quantized inference, and hybrid architecture (smaller LLM + RAG for retrieval heavy tasks).

- **Risk: Clinical liability**  
  - *Mitigation:* Clear disclaimers, human-in-loop, explicit nurse/clinician responsibilities, clinical governance.

---

## 12. Development & staffing estimates (rough)

- **MVP build (Dev + Pilot)** — 10–12 weeks, team: 1 backend engineer, 1 frontend engineer, 1 MLOps engineer, 1 ML engineer, 0.2 clinician advisor, 0.2 legal advisor.  
- **Production hardening & scaling** — 8–12 weeks more: security, monitoring, multi-region infra, and UX polish.

---

## 13. Appendix — Visual architecture (Mermaid)

> *Render this diagram in tools that support Mermaid to visualize flows.*

```mermaid
flowchart LR
  subgraph Client
    A[React Patient Chat] -->|WebSocket| B[FastAPI WS]
    C[React Nurse Dashboard] -->|REST| B
  end

  B --> D[Session Orchestrator]
  D --> E[LangChain v1.0 Agent Runtime]
  E --> F[RAG Retrieval]
  F -->|top-k contexts| E
  E --> G[Model Serving (LLM + LoRA)]
  G -->|stream tokens| B
  F --> H[Vector DB (Chroma / Milvus / Qdrant)]
  H -->|embeddings| I[Embedding Service]

  E --> J[EHR Connector (de-identified summaries)]
  J -->|patient history| E

  B --> K[Audit & Logging DB]
  K --> L[Monitoring & Dashboard (Prometheus / Grafana / LangSmith)]
  C -->|review| M[Nurse Action (Accept/Override)]
  M --> K
  K -->|training data exports| N[MLOps / Training Pipeline]
  N -->|adapter artifacts| G

  style E fill:#fef3c7,stroke:#f59e0b
  style G fill:#ede9fe,stroke:#7c3aed
  style H fill:#ecfeff,stroke:#0891b2
````

---

## 14. References & recommended reading (selected)

* LangChain v1.0 release & docs (agent runtime, stability). ([LangChain Docs][1])
* Tutorials: FastAPI + LangGraph / LangChain in production. ([DEV Community][2])
* RAG system best practices and vector databases (Chroma, Milvus). ([Medium][3])
* Agent frameworks landscape and practical guides for production. ([Dev Learning Daily][4])

---

## 15. Next immediate deliverables (pick one)

1. Detailed **API contract** (OpenAPI spec) for the FastAPI backend (chat endpoints, nurse endpoints, admin endpoints).
2. **LangChain agent implementation skeleton** (Python) demonstrating: system prompt usage, RAG retrieval call, EHR tool call, and model invocation.
3. **End-to-end deployment plan** (k8s manifests, Helm chart sketch, GPU node sizing).
4. **Safety & evaluation plan** (detailed test suites, clinical validation checklists).

---

[1]: https://docs.langchain.com/oss/python/releases/langchain-v1?utm_source=chatgpt.com "What's new in v1 - Docs by LangChain"
[2]: https://dev.to/moni121189/from-prompt-to-production-dockerizing-a-langchain-agent-with-fastapi-1pe3?utm_source=chatgpt.com "Dockerizing a LangChain Agent with FastAPI"
[3]: https://medium.com/%40meeran03/building-production-ready-rag-systems-best-practices-and-latest-tools-581cae9518e7?utm_source=chatgpt.com "Building Production-Ready RAG Systems: Best Practices ..."
[4]: https://learningdaily.dev/ai-agent-frameworks-a-practical-guide-from-the-field-08767b9c382f?utm_source=chatgpt.com "AI agent frameworks: A practical guide from the field"

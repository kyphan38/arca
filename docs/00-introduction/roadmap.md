# MLOps / Platform Engineering Roadmap

- [ ] Progress: Draft (Revised)

> Target: MLOps / AI Platform Engineer in Germany
>
> Background: BSc Data Science (HCUS HCMC, GPA 8.67/10), DevOps @ NAB (Terraform, AWS, Bash)
>
> Plan: Master's in Data Science (80%) / Computer Science (20%) in Germany, late 2027

---

## Parallel Tracks (Throughout 2026–2027)

- [ ] LeetCode: 3–4 problems/week, focus Medium (array, hash map, graph, tree, DP basics). Target ~150 problems before Master's
- [ ] German Language: Target B1 before departure, B2 during Master's. Register for a class ASAP
- [ ] Open Source Contributions: Start small PRs to Ray, vLLM, Kubeflow, or MLflow once skill level allows

---

## Phase 1: Systems Foundation + Cloud Cert (Apr–May 2026)

### Why first?

CMU 15-213 is the single best foundation course - OS, memory, concurrency, networking at the systems level. Everything else (parallel computing, distributed systems, performance) builds on top of this. Moving it to the front saves you time later

### Next steps

- [ ] CMU 15-213 - Introduction to Computer Systems (Apr–May 2026)
  - Priority: understand memory hierarchy, concurrency, linking, virtual memory
  - This replaces needing a standalone OS course later
- [ ] AWS Solutions Architect Associate - study in parallel, schedule exam by end of May
  - You use AWS daily at work; don't delay this

---

## Phase 2: Networking + Mythili Systems Series (Jun–Aug 2026)

### Why this order?

Networking core chapters give you the vocabulary for everything cloud/distributed. The Mythili series then builds from OS → system design → virtualization, which flows naturally after 15-213

### Next steps

- [ ] Networking - Kurose & Ross (June 2026)
  - Focus: Transport layer (TCP/UDP), Network layer (IP, routing), Application layer (HTTP, DNS)
  - Skip: physical layer details, mathematical queuing theory sections
- [ ] OS - Mythili Vutukuru (June–July 2026)
  - Will reinforce and extend what you learned in 15-213
- [ ] Design and Engineering of Computer Systems - Mythili Vutukuru (July 2026)
- [ ] Virtualization and Cloud Computing - Mythili Vutukuru (August 2026)
  - Directly relevant to your current DevOps work and future MLOps infra

---

## Phase 3: Kubernetes + Backend + MLOps Project (Aug–Sep 2026)

### Why here?

This is the bridge between your DevOps present and MLOps future. You need hands-on K8s and backend skills before diving into parallel/GPU computing

### Next steps

- [ ] Kubernetes Deep Dive (August 2026)
  - Core: pods, deployments, services, ingress, RBAC, helm charts, operators
  - ML-specific: GPU scheduling, node affinity, resource quotas
  - Resources: "Kubernetes in Action" (book) or KodeKloud CKA course
- [ ] FastAPI + Backend Fundamentals (September 2026)
  - Build a complete ML model serving API:
    - REST API design, request validation (Pydantic)
    - Authentication (JWT basics)
    - Database (PostgreSQL + SQLModel/SQLAlchemy)
    - Async programming
    - Dockerize → deploy to K8s with CI/CD pipeline
  - This one project covers all the backend you need

---

## Phase 4: Parallel Computing + GPU Programming (Oct–Nov 2026)

### Why?

GPU/parallel computing is the differentiator for MLOps vs generic DevOps. Understanding how ML training actually uses hardware makes you 10x more effective at infrastructure decisions

### Next steps

- [ ] CMU 15-418 or Stanford CS149 - Parallel Computing (October 2026)
  - Pick one; CMU 15-418 is slightly more practical
- [ ] NVIDIA CUDA C++ Programming (November 2026)
  - Official NVIDIA course
  - Understanding CUDA memory model, kernel launches, occupancy
  - Directly applicable to ML training infrastructure

---

## Phase 5: ML Systems + Distributed Systems (Nov–Dec 2026)

### Why last in pre-Master's?

These are the capstone topics. Distributed systems assumes you understand networking, OS, and concurrency. ML systems design assumes you understand both ML and infrastructure. By now you have both

### Next steps

- [ ] ML Systems Design (November 2026)
  - "Designing Machine Learning Systems" by Chip Huyen (book)
  - Or Stanford CS 329S
  - Covers: data pipelines, feature stores, model serving, monitoring, CI/CD for ML
- [ ] MIT 6.824 - Distributed Systems (December 2026)
  - Raft consensus, MapReduce, fault tolerance, replication
  - Foundation for understanding distributed ML training later

---

## Phase 6: Advanced AI Systems (Q1 2027)

### Next steps

- [ ] CMU 10-414 - Deep Learning Systems (January 2027)
  - Autograd internals, PyTorch under the hood
  - Bridges your DS background with systems understanding
- [ ] Data Pipeline & Feature Stores (February 2027)
  - Feast, DVC, MLflow for experiment tracking
  - Build an end-to-end ML pipeline project
- [ ] Advanced GPU Programming (March 2027) - Optional
  - OpenAI Triton, UIUC ECE408
  - Only if Phase 4 CUDA felt comfortable and you want to go deeper

---

## Phase 7: Platform Engineering + EU-Relevant Skills (Q2 2027)

### Why?

GreenOps and FinOps are uniquely valuable in the EU market due to sustainability regulations. This differentiates you from US-trained engineers

### Next steps

- [ ] Stanford CS336 - LLMs from Scratch (April 2027) - Optional
  - Full model lifecycle understanding
  - Valuable for AI infrastructure decisions, not required for MLOps entry
- [ ] K8s AI Infra Project (May 2027)
  - Kubernetes + Terraform + NVIDIA GPU Operator + multi-node scheduling
  - This is your portfolio centerpiece
- [ ] FinOps and GreenOps (June 2027)
  - GPU cost modeling (AWS/RunPod), carbon tracking (codecarbon.io), PUE metrics
  - EU companies care about this; mention it in interviews
- [ ] Kernel Observability: eBPF + Cilium (July 2027) - Optional
  - Kernel-level monitoring, network policy
  - Nice-to-have for senior roles

---

## Phase 8: Optional - Performance Engineering

> Fit this in whenever you have bandwidth, or skip entirely

- [ ] MIT 6.172 - Performance Engineering
  - Deep dive into cache optimization, memory allocation, profiling
  - Most useful if targeting HPC-adjacent roles at Fraunhofer/Jülich
  - Not required for standard MLOps positions

---

## Phase 9: Master's in Germany + Career Launch (Late 2027 Onward)

### Academic

- [ ] Choose program: Data Science (80%) / Computer Science (20%)
- [ ] Target universities with strong ML/Systems labs (TU Munich, TU Berlin, RWTH Aachen, KIT)

### Career Strategy

- [ ] Target job titles: MLOps Engineer, AI Platform Engineer, ML Infrastructure Engineer, Research Software Engineer
  - Broader than just "MLOps" - same skills, more openings
- [ ] Werkstudent positions: Start applying in semester 1
  - Target: Automotive (BMW, Bosch, CARIAD), Fintech, or research institutes
- [ ] Privacy & Federated Learning (during Master's)
  - Flower framework, GDPR compliance in ML pipelines
  - Critical differentiator for Healthcare and Banking ML in Germany
- [ ] HPC Tools (if targeting research institutes)
  - Slurm Workload Manager, Apptainer/Singularity
  - Required for Fraunhofer, Max Planck, Jülich
- [ ] Open Source Portfolio
  - Contribute to Ray, vLLM, Kubeflow, or similar projects
  - German employers (especially research) value this highly

### Industry Targets

| Sector | Companies | Why |
|--------|-----------|-----|
| Automotive | BMW, Bosch, CARIAD, Continental | Huge ML infra needs, sponsor visas, stable |
| Research HPC | Fraunhofer, Max Planck, Jülich | Cutting-edge, publish-friendly, good work-life |
| Fintech/Banking | N26, Deutsche Bank, ING | ML for fraud/risk, familiar from NAB experience |
| Tech/Startup | DeepL, Celonis, SAP | Fast-paced, English-friendly, competitive pay |

---

## Immediate Action Checklist

- [ ] Schedule AWS Solutions Architect Associate exam (target: May 2026)
- [ ] Start CMU 15-213 lectures this week
- [ ] Register for German language class (target B1 before departure)
- [ ] Set up LeetCode schedule: 3–4 problems/week, track progress
- [ ] Research Master's programs and application deadlines

---

## AWS Certification Path

| Cert | When | Why |
|------|------|-----|
| Solutions Architect Associate | May 2026 | Immediate career value, you already have the knowledge |
| AWS ML Specialty (MLS-C01) | After Phase 5 (early 2027) | Combines cloud + ML, stronger signal for MLOps roles |

> Note: Get SAA first - it is faster, validates your current skills, and is a prerequisite mindset for ML Specialty

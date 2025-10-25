# 🧭 OrderSense — Product Roadmap

## 1. Objective

This roadmap outlines the phased development of OrderSense, tracking technical maturity from MVP to full SaaS deployment.  
Each phase is deliverable-driven — no vanity milestones, only tangible outcomes.



## 2. Release Phases

| Phase | Version | Goal | Core Deliverables | Status |
|--------|----------|------|-------------------|--------|
| **Phase 1** | `v0.1` | MVP foundation | - Upload → Forecast → Recommend flow<br>- FastAPI backend<br>- Streamlit dashboard<br>- SQLite data store | 🚧 In Progress |
| **Phase 2** | `v0.2` | Model trust & explainability | - Event tagging system<br>- Data quality scoring<br>- SHAP explainability<br>- Confidence-weighted outputs | ⏳ Planned |
| **Phase 3** | `v0.3` | Automation & integrations | - QuickBooks / Shopify / Sheets connectors<br>- Scheduler for recurring forecasts<br>- Enhanced UI filters | ⏳ Planned |
| **Phase 4** | `v0.4` | Learning & adaptation | - Feedback loop (user validation of accuracy)<br>- Continuous retraining pipeline<br>- Forecast performance tracking | ⏳ Planned |
| **Phase 5** | `v1.0` | SaaS release | - Auth + multi-user roles<br>- PostgreSQL backend<br>- Cost-control + API usage tracking<br>- Deployment to cloud (Render / AWS) | ⏳ Planned |



## 3. Stretch Goals (Beyond v1.0)

| Area | Focus | Impact |
|-------|--------|---------|
| **Supply Chain Optimization** | Warehouse allocation, transportation cost minimization | Full supply chain intelligence |
| **Causal Forecasting** | Detect and isolate drivers of demand spikes | Strategic planning accuracy |
| **Vision-Based Demand** | Image-based shelf detection for retail | Automation |
| **LLM Copilot Interface** | Conversational interface: “Ask OrderSense” | Accessibility |
| **Dynamic Pricing Simulation** | Forecast demand elasticity by price | Profit optimization |



## 4. Technical Milestones

| Quarter | Milestone | Output |
|----------|------------|---------|
| **Q4 2025** | MVP Backend + Streamlit UI | End-to-end demo |
| **Q1 2026** | Model Explainability + Event Integration | Smarter insights |
| **Q2 2026** | External Integrations | Automated sync |
| **Q3 2026** | Learning Feedback Loop | Adaptive engine |
| **Q4 2026** | SaaS Platform Launch | Market-ready product |



## 5. Quality Benchmarks

| Metric | Target | Measurement |
|---------|--------|--------------|
| Forecast Accuracy (MAPE) | ≤ 15% | Model test logs |
| API Response Time | < 2.5s | Benchmark test |
| Data Validation Coverage | 100% | Validation logs |
| UI Load Time | < 1.5s | Frontend metrics |
| Uptime (post-deploy) | 99% | Cloud monitor |



## 6. Governance & Maintenance

| Function | Owner | Description |
|-----------|--------|-------------|
| **Model Ops** | AI/ML maintainer | Manage training, retraining, versioning |
| **API & Infra** | Backend dev | Maintain FastAPI, DB, and scaling |
| **UI/UX** | Frontend dev | Dashboard polish, interactivity |
| **Data Validation** | QA analyst | Ensure input reliability |
| **Docs & Releases** | Maintainer (Arsh Deep Singh) | Documentation + version tagging |



## 7. Version Control Protocol

- Semantic versioning (`v0.x`, `v1.x`)
- GitHub branch model:
> main → production-ready
> dev → active development
> feature/* → isolated branches
- Tag releases using commit-based changelogs.

## 8. Exit Criteria for MVP Completion (`v0.1`)

- ✅ CSV upload and validation fully functional  
- ✅ Forecasts generated per product  
- ✅ Recommendations computed and displayed  
- ✅ Dashboard live (Streamlit)  
- ✅ Documentation complete (`/docs/01–06`)  
- ⏳ Testing and packaging  

## 10. Notes

- Scope creep is deferred — no new modules until current phase closes.  
- Data validation remains non-negotiable before any model runs.  
- All roadmap updates to be committed to `/docs/roadmap.md` under PR review.

**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com 

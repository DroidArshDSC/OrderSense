# 🧭 OrderSense — Project Outline

> **“Know what to order — before you run out or overstock.”**

---

## 🧩 1. Problem Statement

Wholesalers and small-to-mid distributors often rely on intuition or static spreadsheets for inventory decisions.  
This leads to:
- Overstock → wasted capital and spoilage.  
- Stockouts → missed sales and customer churn.  
- Manual forecasting → slow, error-prone, and disconnected from reality.  

**OrderSense** solves this by turning historical sales data into *actionable, explainable reorder intelligence*.

---

## 🎯 2. Core Objective

Deliver an **AI Demand Copilot** that:
- Analyzes sales data,
- Predicts future demand,
- Recommends optimal reorder quantities,
- Explains the “why” behind every recommendation.

**Goal:** Enable business users to make confident, data-driven restocking decisions — no data science team required.

---

## 🧠 3. AI Strategy & Cost Positioning

### 1. Applied AI Foundation (Current)
OrderSense is built entirely on **open-source Applied AI**, focused on time-series forecasting and explainable decision support.  
It does **not** rely on generative AI for its core intelligence.

| Function | Technology | Cost | Purpose |
|-----------|-------------|------|----------|
| **Forecasting** | Prophet (Meta), ARIMA (statsmodels) | Free | Predicts product-level demand trends |
| **Event Adjustment** | Custom uplift modeling | Free | Adjusts forecasts for holidays and promotions |
| **Data Cleaning** | Pandas, NumPy | Free | Standardizes and validates inputs |
| **Explainability** | SHAP / LIME | Free | Shows reasoning behind predictions |
| **Visualization** | Plotly, Streamlit | Free | Displays forecasts and recommendations |

All current AI logic runs **locally** or within the backend environment — no external API calls, no credit consumption.

---

### 2. Generative AI Integration (Planned, Optional)
LLMs are **not used** for forecasting accuracy.  
They will be introduced later to enhance interpretation, automation, and user experience.

| Use Case | Description | Value | Cost Model |
|-----------|--------------|--------|-------------|
| **Conversational Copilot (“Ask OrderSense”)** | Users query insights in natural language | Increases accessibility | Paid (token-based) |
| **Insight Summarization** | LLM translates technical outputs into readable summaries | Improves managerial reporting | Paid (usage-based) |
| **Schema Recognition** | Detects meaning of messy CSV columns via language understanding | Simplifies data ingestion | Optional, Paid |
| **Exception Analysis** | Reads logs to flag anomalies (“Stockout risk for SKU-342”) | Speeds up issue detection | Optional, Paid |

---

### 3. Cost Positioning Summary

| Phase | AI Stack | Category | Estimated Cost |
|--------|-----------|-----------|----------------|
| **v0.1–v0.4** | Prophet + ARIMA + SHAP | **Applied AI (Free)** | ₹0 |
| **v0.5–v1.0** | Add LLM for insight & reports | **Generative AI (Paid)** | Usage-based |
| **v1.1+** | Hybrid orchestration | **Applied + Generative** | Controlled subscription model |

---

### 4. Strategic Principle

> “Forecasts are science; interpretation is service.”

- **Science** (Applied AI): free, reproducible, deterministic.  
- **Service** (Generative AI): optional, credit-based, user-facing enhancement.  

This keeps core intelligence **cost-neutral**, ensuring profitability even before LLM integration.


## 👤 4. Target Users

| User Type | Description | Pain Points |
|------------|--------------|--------------|
| **Wholesaler / Distributor** | Buys from suppliers → sells to retail stores | Overbuying, stockouts, manual tracking |
| **Retail Chain Owner** | 3–20 outlets, manages inventory manually | Seasonality & store-level imbalance |
| **Procurement Manager** | Handles purchase decisions | Lack of forecast visibility, no explainability |

---

## 🧱 5. Core Modules (MVP Scope)

| Module | Description | Deliverable |
|---------|--------------|-------------|
| **Data Ingestion & Validation** | CSV/Excel upload, schema check, anomaly detection | Clean dataset ready for forecasting |
| **Forecast Engine** | Time-series model (Prophet + ARIMA) per SKU | Forecasted daily demand |
| **Event & Seasonality Adjuster** | Integrates holidays, promotions, or event data | Adjusted forecast curve |
| **Reorder Recommendation Engine** | Combines forecast + lead time + safety stock | Optimal reorder quantity per SKU |
| **Product Classification** | Categorize as perishable, seasonal, etc. | Enables dynamic forecasting strategy |
| **Dashboard (Streamlit)** | View forecasts, recommendations, and metrics | MVP user interface |

---

## ⚙️ 6. Tech Stack

| Layer | Technology | Purpose |
|--------|-------------|----------|
| **Backend** | FastAPI | API layer for forecasting & recommendations |
| **Data Processing** | Pandas, NumPy | Data cleaning and feature prep |
| **Forecasting Models** | Prophet, ARIMA (statsmodels) | Demand prediction |
| **Visualization** | Streamlit + Plotly | UI and interactive charts |
| **Database** | SQLite (local) → Postgres (scalable) | Store sales, forecasts, recommendations |
| **Explainability (Future)** | SHAP / LIME | Explain model reasoning |

---

## 🧠 7. Product Classification (Core Logic)

| Type | Description | Forecasting Strategy |
|------|--------------|----------------------|
| **Perishable** | Short shelf life (e.g., milk, produce) | Short horizon, high frequency |
| **Non-Perishable** | Long shelf life (e.g., detergent) | Stable trend, slower model refresh |
| **Seasonal** | Time-bound demand (e.g., winter goods) | Seasonal uplift modeling |
| **Obsolete-Prone** | Risk of low turnover | Weighted decay in forecast |
| **New** | Insufficient data | Similar-SKU inference |

Color-coded in the UI for immediate visual distinction.

---

## 📊 8. User Flow

Upload Sales Data → System Validates → Forecast Runs
↓
Event Adjustments → Reorder Recommendations
↓
Dashboard View (Color-coded, Downloadable)


Users can:
- Filter by product type  
- View confidence intervals  
- Export reorder reports  
- Provide feedback on forecast accuracy (future loop)


## 🎨 9. Dashboard UX Overview

| Section | Component | Description |
|----------|------------|-------------|
| **Header** | Title, Upload Button, Refresh | Primary actions |
| **Sidebar** | Filters (Product type, Confidence) | Drill-down |
| **Main Panel** | Plotly chart | Forecast visualization |
| **Reorder Table** | Color-coded SKUs | Actionable insights |
| **Insights Section** | KPI cards | Top movers, accuracy metrics |

---

## 🧭 10. Roadmap (Execution Phases)

| Phase | Objective | Focus |
|--------|------------|-------|
| **v0.1 (MVP)** | Upload → Forecast → Recommend | Core models & UI |
| **v0.2** | Add explainability + events | Trust-building |
| **v0.3** | Integrations (QuickBooks, Shopify, Sheets) | Automation |
| **v0.4** | Feedback-driven retraining | Continuous improvement |
| **v1.0** | Full SaaS release | User management + scaling |

---

## 🧩 11. Out of Scope (for MVP)

- Logistics / Transportation Optimization  
- Multi-warehouse routing  
- Complex supplier analytics  
- Price elasticity modeling  

These belong in post-MVP roadmap.

---

## 🧾 12. Deliverables Summary

| Deliverable | Description |
|--------------|--------------|
| **Backend (FastAPI)** | API endpoints for data, forecast, recommendation |
| **Frontend (Streamlit)** | Dashboard with color-coded insights |
| **Docs** | Data schema, API design, model lifecycle |
| **Sample Data** | Mock CSV for demonstration |
| **MVP Release (v0.1)** | Core workflow validated end-to-end |

---

## 📫 Maintainer

**Arsh Deep Singh**  
📧 arshds289@gmail.com
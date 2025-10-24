# 🧭 OrderSense — AI Demand Copilot for Wholesalers

> **“Know what to order — before you run out or overstock.”**  
> AI-driven demand forecasting and reorder optimization for wholesalers, distributors, and small retail chains.



## 🚀 Overview

**OrderSense** helps businesses make **data-backed inventory decisions**.  
It analyzes past sales, adjusts for events and seasonality, and recommends optimal reorder quantities per product — so you never overbuy or run out.

**Built with:** FastAPI · Python · Prophet · ARIMA · Streamlit



## 🎯 Core Features

- 📦 **Smart Demand Forecasting** — Predict product-level demand using Prophet & ARIMA.
- 🧠 **AI Reorder Engine** — Suggest optimal order quantities factoring in safety stock and lead time.
- 📅 **Event & Seasonality Awareness** — Adjust forecasts automatically for holidays, promotions, or seasonal spikes.
- 🧾 **CSV Upload Interface** — Plug in your sales data; get instant demand insights.
- 🧩 **Product Classification** — Handles perishables, non-perishables, and obsolete-prone items differently.
- 📊 **Interactive Dashboard** — Color-coded insights powered by Streamlit + Plotly.
- 🔍 **Explainable AI (Planned)** — Understand “why” behind each recommendation.



## 🧱 System Architecture

Frontend (Streamlit)
↓
Backend (FastAPI)
↓
Data Processing (Pandas, NumPy)
↓
Forecast Models (Prophet, ARIMA)
↓
Recommendation Engine
↓
Storage (SQLite → Postgres)



## 🧩 Data Schema (Simplified)

### 🗂️ `products`
| Column | Type | Description |
|--------|------|-------------|
| product_id | string | Unique identifier |
| name | string | Product name |
| category | string | Category or department |
| product_type | enum | perishable / non_perishable / seasonal / obsolete_prone |
| shelf_life_days | int | Shelf life of product |
| lead_time_days | int | Supplier delivery time |


### 📈 `sales`
| Column | Type | Description |
|--------|------|-------------|
| date | date | Transaction date |
| product_id | string | Foreign key from products |
| quantity_sold | float | Units sold |
| price | float | Optional (for profitability metrics) |
| location | string | Optional store/region |


### 🔮 `forecasts`
| Column | Type | Description |
|--------|------|-------------|
| product_id | string | Foreign key |
| date | date | Forecast date |
| predicted_demand | float | Forecasted quantity |
| confidence | float | Model confidence score |


### 💡 `recommendations`
| Column | Type | Description |
|--------|------|-------------|
| product_id | string | Foreign key |
| recommended_qty | float | Suggested reorder amount |
| reason | text | Explanation (lead time, safety stock, etc.) |
| confidence | float | Derived from forecast model |



## ⚙️ Tech Stack

| Layer | Tech | Purpose |
|--------|------|----------|
| **Backend** | FastAPI | API endpoints & logic |
| **Data Processing** | Pandas, NumPy | Data cleaning, feature prep |
| **Forecasting** | Prophet, ARIMA (statsmodels) | Time-series demand prediction |
| **Frontend (MVP)** | Streamlit | Simple and fast visualization layer |
| **Visualization** | Plotly | Interactive demand charts |
| **Database** | SQLite (local) / Postgres (prod) | Persistent storage |
| **Version Control** | GitHub | Collaboration & CI/CD base |



| Product Type       | Color     | Meaning                  |
| ------------------ | --------- | ------------------------ |
| **Perishable**     | 🟥 Red    | Urgent, short shelf life |
| **Non-Perishable** | 🟦 Blue   | Stable demand            |
| **Seasonal**       | 🟧 Orange | Event-driven spikes      |
| **Obsolete-Prone** | 🟫 Grey   | Low turnover risk        |



| Phase          | Focus                                      |
| -------------- | ------------------------------------------ |
| **v0.1 (MVP)** | CSV Upload → Forecast → Recommend          |
| **v0.2**       | Add event tagging + explainability         |
| **v0.3**       | Integrations (QuickBooks, Shopify, Sheets) |
| **v0.4**       | Self-learning feedback loop                |
| **v1.0**       | SaaS-grade UI & cost control system        |


🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to modify or improve.


🧩 License

This project is licensed under the MIT License.


📫 Contact

Arsh Deep Singh

📧 [arshds289@gmail.com]

🌐 Coming soon: ordersense.ai


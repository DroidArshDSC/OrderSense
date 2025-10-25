# 🖥️ OrderSense — UI Blueprint

## 1. Objective

Define the front-end structure, color logic, and component behavior for the OrderSense dashboard.  
The goal is immediate visual clarity — users should identify what needs action within seconds.



## 2. Framework

- **Framework:** Streamlit (MVP)
- **Visualization:** Plotly (charts), Pandas DataFrame (tabular)
- **Style:** Light by default; dark mode optional.
- **Design Priorities:** Fast render, minimal clutter, color-coded readability.



## 3. Layout Structure

| Section | Component | Function |
|----------|------------|----------|
| **Header Bar** | Logo, Upload Button, Refresh Action | Entry point for user actions |
| **Sidebar** | Filters & Controls | Filters by product type, confidence, location |
| **Main Content (Top)** | Forecast Visualization | Displays time-series charts per SKU |
| **Main Content (Mid)** | Reorder Table | Central view for recommendations |
| **Main Content (Bottom)** | Insights Section | Summaries, KPIs, and data quality stats |
| **Footer** | Build Version, Contact Info | Metadata and product versioning |



## 4. Component Behavior

### 4.1 File Upload
- Accept `.csv` or `.xlsx`
- Triggers `/upload` API
- Displays validation summary:
✅ 3,482 records validated
⚠️ 18 skipped (invalid or missing data)


### 4.2 Filter Panel (Sidebar)
| Filter | Description |
|---------|--------------|
| **Product Type** | perishable / non-perishable / seasonal / obsolete |
| **Location** | City / Region selector |
| **Confidence Threshold** | Range slider (default ≥ 0.75) |
| **Date Range** | Choose forecast window (default 14 days) |


### 4.3 Forecast Chart
- Line chart via Plotly.
- Each product rendered as separate trace.
- Confidence band shaded (light opacity).
- Tooltip includes:
Predicted: 162 units
Confidence: 88%
Product: Whole Milk 1L
Date: 2025-10-27


### 4.4 Reorder Recommendation Table
| Field | Example | Note |
|--------|----------|------|
| Product | Whole Milk 1L | Color-coded tag |
| Product Type | Perishable | Color from `product_type` map |
| Forecast (7d) | 340 units | From `/forecast` endpoint |
| Recommended Order | 380 units | From `/recommendations` endpoint |
| Confidence | 0.88 | Derived metric |
| Action | 👍 Accurate / 👎 Off | User feedback (future use) |

Rows use background shading based on product classification.



## 5. Color Mapping

| Product Type | Color | Usage |
|---------------|--------|--------|
| **Perishable** | `#FF6B6B` | Urgent / short shelf life |
| **Non-Perishable** | `#4ECDC4` | Stable demand |
| **Seasonal** | `#FFA94D` | Event-driven |
| **Obsolete-Prone** | `#A5A5A5` | Low-priority / aging stock |
| **New / Unknown** | `#FFD43B` | Uncertain forecast |

Shading intensity represents forecast confidence:
- 90%+ → solid
- 70–89% → medium
- <70% → light tint


## 6. Insights Section (Bottom Panel)

| Card | Metric | Description |
|-------|---------|-------------|
| **Top Movers** | Highest 5 SKUs by recent demand growth | Quick view of spikes |
| **Slow Movers** | Lowest 5 SKUs | Identify clearance candidates |
| **Forecast Accuracy** | Mean MAPE (last 30 days) | Health of system predictions |
| **Data Quality Score** | Derived from validation logs | Visual gauge, green/yellow/red |

Each card refreshes automatically after `/forecast/run`.


## 7. Notifications & Alerts

- ⚠️ Low confidence (<0.6) → orange highlight in table  
- 🟥 Urgent reorder needed (perishables near expiry) → red border  
- 🟦 Stable → normal display  
- Notifications appear as dismissible Streamlit alerts:

```python
st.warning("3 SKUs have low forecast confidence (<0.6). Review before ordering.")
```

## 8. Export Features
- Download CSV: Export current recommendations with filters applied.
- Export Forecast Report: Includes predicted demand + confidence bounds.
- Audit Report: Includes validation results for last upload.

***Default filenames:***
ordersense_recommendations_{date}.csv
ordersense_forecast_{date}.csv

## 9. Future Enhancements (Post-MVP)
| Feature                             | Description                                 |
| ----------------------------------- | ------------------------------------------- |
| **Explainability Modal**            | “Why this recommendation?” with key drivers |
| **Custom Dashboard Layouts**        | Save preferred views (procurement, analyst) |
| **Interactive What-If Simulations** | Adjust lead time or buffer to test outcomes |
| **User Auth (v1.0)**                | Role-based access to dashboards             |
| **Mobile Responsive UI**            | React-based replacement for Streamlit       |

## 10. Design Principles
- Show, don’t tell. Color and position carry meaning.
- Speed > Complexity. Charts load instantly; no over-rendering.
- Consistency. One color → one meaning across modules.
- Context-first UX. Numbers always shown with date and confidence.

**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com 
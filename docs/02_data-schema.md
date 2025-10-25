# 🧩 OrderSense — Data Schema Specification

## 1. Overview

OrderSense uses a relational data structure designed for traceability, extensibility, and quick analytical queries.  
The schema supports forecasting, event adjustment, and reorder recommendations.

Core entities:
- `products` — metadata and classification
- `sales` — historical demand records
- `forecasts` — predicted demand
- `recommendations` — AI reorder output
- `events` — optional contextual adjustments

---

## 2. Tables

### 2.1 products

| Column | Type | Description |
|--------|------|-------------|
| `product_id` | TEXT (PK) | Unique product identifier |
| `name` | TEXT | Product name |
| `category` | TEXT | Product category |
| `product_type` | TEXT | One of `perishable`, `non_perishable`, `seasonal`, `obsolete_prone` |
| `shelf_life_days` | INTEGER | Shelf life duration |
| `lead_time_days` | INTEGER | Supplier delivery time |
| `supplier` | TEXT | Supplier name |
| `created_at` | DATETIME | Timestamp of record creation |

Purpose: static product metadata used for classification and forecast configuration.

---

### 2.2 sales

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER (PK) | Unique row identifier |
| `product_id` | TEXT (FK → products.product_id)` | Product reference |
| `date` | DATE | Sales date |
| `quantity_sold` | FLOAT | Units sold |
| `price` | FLOAT | Optional, for profitability analysis |
| `location` | TEXT | Optional store or region |
| `source` | TEXT | Data origin, e.g. `csv_upload`, `integration` |

Purpose: primary time-series dataset for demand forecasting.

---

### 2.3 forecasts

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER (PK) | Unique forecast record |
| `product_id` | TEXT (FK)` | Product reference |
| `forecast_date` | DATE | Date of predicted demand |
| `predicted_demand` | FLOAT | Forecasted quantity |
| `confidence` | FLOAT | Model confidence, 0–1 |
| `model_used` | TEXT | Forecast model name/version |
| `created_at` | DATETIME | Timestamp of generation |

Purpose: stores all forecast outputs per product per date.

---

### 2.4 recommendations

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER (PK) | Unique recommendation record |
| `product_id` | TEXT (FK)` | Product reference |
| `recommended_qty` | FLOAT | Suggested reorder quantity |
| `reason` | TEXT | Summary of rationale |
| `confidence` | FLOAT | Derived confidence score |
| `valid_until` | DATE | Validity window |
| `created_at` | DATETIME | Timestamp of generation |

Purpose: stores actionable reorder insights derived from forecasts.



### 2.5 events (optional, v0.2+)

| Column | Type | Description |
|--------|------|-------------|
| `event_id` | TEXT (PK) | Event identifier |
| `event_name` | TEXT | Event name |
| `start_date` | DATE | Start date |
| `end_date` | DATE | End date |
| `impact_factor` | FLOAT | Expected uplift multiplier |
| `location` | TEXT | Region or store scope |

Purpose: external factors (holidays, promotions) used to adjust forecasts.



## 3. Data Validation Rules

| Field | Validation | Handling |
|--------|-------------|----------|
| `quantity_sold` | > 0 | Skip invalid entries |
| `date` | Valid ISO date | Auto-correct or reject |
| `product_id` | Must exist in `products` | Reject or prompt correction |
| `lead_time_days` | ≥ 0 integer | Default = 1 |
| `confidence` | Float 0–1 | Clamp and round to 2 decimals |



## 4. Sample Data

**products**
| product_id | name | product_type | lead_time_days | shelf_life_days |
|-------------|------|--------------|----------------|-----------------|
| P001 | Whole Milk 1L | perishable | 2 | 7 |
| P002 | Detergent 1kg | non_perishable | 5 | 180 |
| P003 | Winter Gloves | seasonal | 10 | 120 |

**sales**
| date | product_id | quantity_sold | location |
|------|-------------|----------------|-----------|
| 2025-09-28 | P001 | 152 | Mumbai |
| 2025-09-29 | P001 | 163 | Mumbai |
| 2025-09-28 | P002 | 89 | Delhi |



## 5. Future Extensions

| Table | Description |
|--------|-------------|
| `users` | Authentication and role control |
| `feedback` | User response on forecast/recommendation accuracy |
| `integration_logs` | Third-party data sync history |
| `inventory_levels` | Real-time stock tracking |



## 6. Design Principles

- **Normalized schema** — no redundant metrics or embedded lists  
- **Traceable lineage** — every forecast and recommendation links to source sales data  
- **Lightweight** — SQLite-first, Postgres-ready  
- **Extensible** — new modules (feedback, inventory) can attach cleanly  



**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com  
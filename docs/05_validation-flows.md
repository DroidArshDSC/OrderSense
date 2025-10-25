# 🧾 OrderSense — Data Validation & Error Handling Flows

## 1. Objective

Data quality directly drives forecast reliability.  
This document defines the **validation, cleaning, and error management flows** applied to incoming data (sales, products, and events) before model execution.

The guiding principle:  
> *No bad data enters the forecasting pipeline.*



## 2. Validation Layers

| Layer | Scope | Purpose |
|--------|--------|----------|
| **Schema Validation** | Structural | Ensures required columns and data types exist |
| **Value Validation** | Record-level | Ensures data integrity (positive quantities, valid dates, etc.) |
| **Relational Validation** | Cross-table | Ensures foreign key consistency (product IDs, event references) |
| **Statistical Validation** | Analytical | Detects anomalies, missing patterns, and outliers |
| **Pre-Model Sanitization** | Forecast readiness | Cleans and normalizes final dataset before modeling |



## 3. Upload Validation Flow ( `/upload` )

1. **File Verification**
   - Accepts only `.csv` or `.xlsx`
   - File size < 10MB
   - UTF-8 encoding enforced

2. **Schema Check**
   - Required columns:
     ```
     date, product_id, quantity_sold
     ```
   - Optional columns:
     ```
     price, location
     ```
   - Reject upload if required fields are missing.

3. **Data Type Enforcement**
   - `date` → parsed as ISO 8601
   - `quantity_sold` → numeric, > 0
   - `product_id` → string, non-null
   - Invalid types are logged and excluded.

4. **Relational Check**
   - `product_id` must exist in `products` table.
   - New products trigger a flag → "unregistered product" list.

5. **Duplicate Handling**
   - Duplicate (`product_id`, `date`, `location`) entries → keep latest or average.
   - Summary logged in upload response.

6. **Outlier Detection**
   - 3× IQR or Z-score > 3
   - Values replaced with capped thresholds or flagged.
   - Outlier ratio metric stored per SKU.

7. **Missing Date Handling**
   - If < 10% gaps → interpolate.
   - If > 10% gaps → flag series as “incomplete” (skipped in forecast).



## 4. Product Data Validation

| Field | Validation | Default / Action |
|--------|-------------|------------------|
| `product_type` | Must match defined set | Default = `non_perishable` |
| `lead_time_days` | ≥ 0 integer | Default = 1 |
| `shelf_life_days` | > 0 integer | Default = 30 |
| `supplier` | Optional | — |
| Missing product_id | Reject row | Log in `validation_errors` |

If product metadata is incomplete, forecasting will skip that SKU until corrected.



## 5. Event Data Validation (v0.2+)

| Field | Validation | Action |
|--------|-------------|--------|
| `event_name` | Required | Reject if missing |
| `impact_factor` | Must be float ≥ 1.0 | Default = 1.0 |
| `start_date`, `end_date` | Must be valid and chronological | Swap or reject if invalid |

Events failing validation will not be applied to any forecasts.



## 6. Error Handling Strategy

| Error Type | Example | Response |
|-------------|----------|-----------|
| **Schema Error** | Missing required column | HTTP 400 + descriptive message |
| **Data Format Error** | Invalid date or NaN value | Skip record, log warning |
| **Foreign Key Error** | Unknown product_id | Flag record, exclude from forecast |
| **Model Error** | Prophet/ARIMA fails to converge | Retry with fallback model |
| **Empty Dataset** | After cleaning, no valid rows remain | Return message: "Insufficient data" |

All validation logs are stored under `/logs/validation_{timestamp}.json`.



## 7. Logging Specification

Each validation process generates a structured JSON log:
```json
{
  "timestamp": "2025-10-25T06:00:00Z",
  "records_processed": 3500,
  "records_valid": 3482,
  "records_skipped": 18,
  "issues": [
    {"type": "schema_error", "count": 2},
    {"type": "invalid_quantity", "count": 7},
    {"type": "missing_product", "count": 9}
  ]
}
```

## 8. Confidence Impact (Post-Validation)

Each dataset receives a Data Confidence Score (0–1) based on:
>% valid records
>% missing dates filled
>% outliers corrected
This score feeds into forecast confidence weighting.


| Range    | Interpretation               |
| -------- | ---------------------------- |
| 0.9–1.0  | High quality                 |
| 0.7–0.89 | Acceptable                   |
| 0.5–0.69 | Marginal, lower confidence   |
| <0.5     | Reject / require data review |

## 9. Manual Override Controls (Future)

- Allow admin users to reclassify flagged products.
- Approve/reject “skipped” datasets manually before re-forecast.
- Downloadable validation report for QA audit.

## 10. Design Principles

- Fail Soft, Not Hard: Invalid rows skip gracefully without halting process.
- Trace Every Error: Each rejected record must have a reason logged.
- No Silent Corrections: Every auto-fix must appear in logs.
- Confidence-Weighted Outputs: Forecasts inherit upstream data quality.


**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com 
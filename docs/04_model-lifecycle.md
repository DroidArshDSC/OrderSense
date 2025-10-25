# 🧠 OrderSense — Model Lifecycle & Forecasting Logic

## 1. Overview

This document defines how forecasting models are trained, updated, cached, and reused inside OrderSense.  
The goal is to maintain **predictive reliability**, **low latency**, and **traceable outputs** across all SKUs.

OrderSense uses a hybrid of:
- **Prophet** for event-aware, trend-seasonality forecasts.
- **ARIMA** for stable, short-horizon demand series.



## 2. Model Scope

Each `product_id` is treated as an independent time series.  
Models are trained using its historical sales data after cleaning and validation.

**Minimum data requirement:** 30 days of continuous records.  
If insufficient data exists, fallback logic triggers a *similar-product inference*.



## 3. Lifecycle Stages

| Stage | Description | Trigger |
|--------|--------------|----------|
| **Data Ingestion** | Sales data loaded and validated | On `/upload` |
| **Model Training** | Prophet/ARIMA model fit per SKU | On `/forecast/run` |
| **Forecast Generation** | Daily predictions per product | Immediately post-training |
| **Recommendation Calculation** | Reorder qty computed | Post-forecast |
| **Caching** | Forecast results stored | In `forecasts` table |
| **Retraining** | Model refreshed on new data | Scheduled or manual trigger |



## 4. Forecasting Workflow

1. **Data Cleaning**
   - Drop duplicates, fill missing dates.
   - Interpolate minor gaps.
   - Outlier capping via IQR or rolling mean thresholds.

2. **Feature Preparation**
   - Map product attributes (lead time, shelf life, product_type).
   - Add event markers (holidays, promotions).
   - Create lag features if ARIMA is used.

3. **Model Selection Logic**

   | Condition | Model Used | Reason |
   |------------|-------------|--------|
   | Data < 60 days | ARIMA | Works better with short series |
   | Data ≥ 60 days | Prophet | Handles trends and seasonality |
   | Seasonal Product | Prophet + Event Tags | Uplift-aware modeling |
   | Obsolete-Prone | ARIMA + Decay Factor | Demand dampening |

4. **Model Execution**
   - Prophet: fit → predict horizon (default 14 days)
   - ARIMA: auto-order selection (AIC-based)
   - Confidence interval derived from residual variance

5. **Result Storage**
   - Forecasts inserted into `forecasts` table.
   - Summary written to logs with model version and timestamp.



## 5. Model Retraining Strategy

| Type | Trigger | Frequency | Description |
|------|----------|------------|--------------|
| **Incremental** | New sales uploaded | On `/forecast/run` |
| **Scheduled** | Periodic batch | Weekly cron (future) |
| **Manual** | Admin/API call | As needed for backfill |
| **Feedback-Based (v0.4)** | Low accuracy feedback from user | Adaptive retraining loop |

Retraining overwrites model parameters while retaining metadata (model name, trained_on, version).



## 6. Model Caching & Versioning

| Field | Description |
|--------|--------------|
| `model_used` | Stored in `forecasts` table per product |
| `trained_on` | Latest sales data cutoff date |
| `version` | Semantic model version, e.g. `Prophet_v1.1` |
| `runtime_hash` | MD5 of training params for reproducibility |

***Cached models (serialized via `joblib` or `pickle`) are stored under:*** /models/{product_id}/{model_name}.pkl

## 7. Forecast Horizon & Parameters

| Parameter | Default | Description |
|------------|----------|--------------|
| `forecast_horizon_days` | 14 | Number of days to predict ahead |
| `confidence_interval` | 0.95 | Interval width for forecast bounds |
| `min_train_points` | 30 | Minimum records to build a model |
| `max_train_window` | 365 | Limit to 1-year rolling window |

Prophet seasonalities: yearly + weekly enabled by default.  
Holiday events injected from `events` table (if present).

## 8. Evaluation Metrics

| Metric | Purpose |
|---------|----------|
| **MAE (Mean Absolute Error)** | Simplicity and interpretability |
| **MAPE (Mean Absolute Percentage Error)** | Relative accuracy |
| **RMSE (Root Mean Square Error)** | Penalizes large deviations |
| **Confidence Deviation** | Variance between upper/lower bound predictions |

Accuracy metrics stored per product after every forecast run.

## 9. Error Handling

| Condition | Action |
|------------|--------|
| Missing or insufficient data | Skip model training, log warning |
| Model convergence failure | Retry with fallback (ARIMA → Prophet or vice versa) |
| Negative forecast values | Clamp to 0 |
| Confidence < 0.5 | Flag as low reliability in recommendation layer |

## 10. Integration with Recommendation Engine

Forecast outputs feed into reorder logic as follows:
recommended_qty = predicted_demand + (safety_stock - on_hand_stock)
Safety stock = function of demand variance × lead time.  
Confidence score cascades into reorder ranking.

## 11. Logging & Audit

Each model run generates:
- Forecast summary JSON
- Accuracy metrics
- Version identifiers
- Execution duration

Logs stored under: /logs/forecast_{date}.json

## 12. Future Enhancements

| Feature | Description |
|----------|-------------|
| **Meta-Model Selector** | Auto-select Prophet/ARIMA/XGBoost based on SKU behavior |
| **Feedback Loop Learning** | User accuracy feedback drives weight adjustment |
| **Causal Forecast Layer** | Adjust for external shocks (supply disruptions, viral demand) |
| **Batch Forecast API** | Async forecast queue for 100+ SKUs in parallel |


**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com  


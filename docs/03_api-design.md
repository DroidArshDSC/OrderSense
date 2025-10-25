# ⚙️ OrderSense — API Design Specification

## 1. Overview

The OrderSense API exposes endpoints for uploading sales data, generating forecasts, and retrieving reorder recommendations.  
It is built using **FastAPI**, with asynchronous operations for model execution and data handling.

Base URL (development): http://127.0.0.1:8000



## 2. Endpoint Summary

| Method | Endpoint | Purpose |
|---------|-----------|----------|
| `POST` | `/upload` | Upload and validate sales data |
| `POST` | `/forecast/run` | Trigger forecast generation |
| `GET` | `/forecast/{product_id}` | Retrieve forecast for a given product |
| `GET` | `/recommendations` | Get all active reorder recommendations |
| `GET` | `/recommendations/{product_id}` | Get recommendation for a specific product |
| `GET` | `/products` | Retrieve product master data |
| `POST` | `/events` *(v0.2+)* | Add or update event metadata |



## 3. Endpoint Details

### 3.1 `POST /upload`

**Purpose:**  
Upload raw sales data (CSV or JSON). Performs validation and stores records in the `sales` table.

**Request (multipart/form-data)**  
```json
{
  "file": "sales_data.csv"
}
```

**Response (JSON)**
```json
{
  "status": "success",
  "records_uploaded": 3540,
  "skipped": 12,
  "message": "Data validation complete. Forecast ready to run."
}
```

### 3.2 `POST /forecast/run`

**Purpose:**
Generate forecasts for all active products based on validated sales data.

**Request (JSON)**
```json
{
  "forecast_horizon_days": 14,
  "model": "prophet"
}
```

**Response (JSON)**
```json
{
  "status": "success",
  "products_forecasted": 48,
  "model_used": "Prophet_v1.1",
  "timestamp": "2025-10-24T07:00:00Z"
}
```

### 3.3 `GET /forecast/{product_id}`

***Purpose:***
Retrieve forecasted demand for a specific product.

**Response (JSON)**
```json
{
  "product_id": "P001",
  "model": "Prophet_v1.1",
  "forecast": [
    {"date": "2025-10-25", "predicted_demand": 152.4, "confidence": 0.87},
    {"date": "2025-10-26", "predicted_demand": 160.1, "confidence": 0.85}
  ]
}
```

***Query Parameters:***
limit (optional): number of future days (default 14)

### 3.4 `GET /recommendations`

**Response (JSON)**
```json
{
  "count": 3,
  "recommendations": [
    {
      "product_id": "P001",
      "recommended_qty": 180,
      "reason": "Lead time 2d, forecast 160, buffer 20",
      "confidence": 0.82,
      "valid_until": "2025-10-29"
    },
    {
      "product_id": "P002",
      "recommended_qty": 0,
      "reason": "Stable demand, sufficient stock",
      "confidence": 0.91,
      "valid_until": "2025-10-28"
    }
  ]
}
```

### 3.5 `GET /recommendations/{product_id}`

***Purpose:***
Retrieve reorder recommendation for a specific product.

**Response (JSON)**
```json
{
  "product_id": "P003",
  "recommended_qty": 90,
  "reason": "Seasonal uplift detected (winter event)",
  "confidence": 0.76,
  "valid_until": "2025-11-02"
}
```

### 3.6 `GET /products`

***Purpose:***
Fetch product metadata for classification and reference.

**Response (JSON)**
```json
{
  "products": [
    {
      "product_id": "P001",
      "name": "Whole Milk 1L",
      "product_type": "perishable",
      "lead_time_days": 2,
      "shelf_life_days": 7
    },
    {
      "product_id": "P002",
      "name": "Detergent 1kg",
      "product_type": "non_perishable",
      "lead_time_days": 5,
      "shelf_life_days": 180
    }
  ]
}
```

### 3.7 `POST /events` (optional, v0.2+)

**Request (JSON)**
```json
{
  "event_id": "E2025_DIWALI",
  "event_name": "Diwali Sale",
  "start_date": "2025-10-30",
  "end_date": "2025-11-04",
  "impact_factor": 1.3,
  "location": "India"
}
```

**Response (JSON)**
```json
{
  "status": "success",
  "message": "Event registered successfully"
}
```



## 4. Authentication (Future)

No authentication required for MVP.
Planned for v1.0 using JWT or API-key based access.

## 5. Error Handling


| HTTP Code | Condition                   | Response Example                            |
| --------- | --------------------------- | ------------------------------------------- |
| 400       | Invalid data format         | `{ "error": "Invalid CSV columns" }`        |
| 404       | Product or record not found | `{ "error": "Product not found" }`          |
| 500       | Internal model error        | `{ "error": "Forecast generation failed" }` |


##  6. Notes for Implementation

Asynchronous endpoints for /forecast/run to prevent blocking.
Background tasks for heavy computations (using FastAPI BackgroundTasks or Celery).
Response times capped at ~3–5s for small datasets.
All timestamps in UTC ISO 8601 format by default.

**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com  
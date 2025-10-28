"""
================================================================================
 File: recommendation_service.py
 Project: OrderSense
 Author: Arsh Deep Singh
 Description:
     Core recommendation engine for OrderSense — converts AI-based demand 
     forecasts into actionable reorder quantities per product.

 Implementation Notes:
     - This is a fully functional **MVP-level implementation**, not a scaffold.
     - It performs real calculations on forecasted demand, lead time, and
       safety stock to produce reorder recommendations.
     - The logic is production-aligned but not yet production-hardened.
       (No dynamic business rules, live inventory sync, or advanced confidence 
       weighting implemented yet.)

 Processing Flow:
     1. Retrieve all products from the database.
     2. For each product, aggregate its forecasted demand (from Prophet output).
     3. Apply a fixed 10% safety stock buffer and adjust for lead time.
     4. Derive reorder quantity and compute confidence averages.
     5. Persist recommendations to the database and return summarized JSON.

 Current Level:
     ✅ Functional Implementation (Validated End-to-End)
     🚧 Ready for future hardening and optimization.

 Future Improvements:
     - Category-specific safety stock percentages.
     - Dynamic reorder policy tuning via configuration.
     - Real-time inventory integration.
     - Explainability layer (variance analysis, model traceability).
     - Alerting and audit logging for generated recommendations.

================================================================================
"""



from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.forecast import Forecast
from app.models.product import Product
from app.models.recommendation import Recommendation
from app.database import SessionLocal

SAFETY_STOCK_PCT = 0.10  # 10% buffer

def generate_recommendations():
    db: Session = SessionLocal()
    try:
        products = db.query(Product).all()
        if not products:
            return "No product data available."

        results = []
        for p in products:
            forecast_window = db.query(Forecast).filter(
                Forecast.product_id == p.product_id
            ).all()

            if not forecast_window:
                continue

            total_forecast = sum(fr.predicted_demand for fr in forecast_window)
            safety_stock = total_forecast * SAFETY_STOCK_PCT
            lead_time = p.lead_time_days or 0
            reorder_qty = total_forecast + safety_stock + (total_forecast * (lead_time / 14))
            conf_avg = sum(fr.confidence for fr in forecast_window) / len(forecast_window)

            rec = Recommendation(
                product_id=p.product_id,
                recommended_qty=round(reorder_qty, 2),
                confidence=round(conf_avg, 2),
                reason=f"{lead_time}-day lead time, {int(SAFETY_STOCK_PCT*100)}% safety buffer",
                valid_until=(datetime.utcnow() + timedelta(days=lead_time or 7)).date(),
            )
            db.add(rec)

            results.append({
                "product_id": p.product_id,
                "forecasted_demand": round(total_forecast, 2),
                "recommended_qty": round(reorder_qty, 2),
                "confidence": round(conf_avg, 2)
            })

        db.commit()

        return results if results else "No recommendations generated."

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

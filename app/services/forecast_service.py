import pandas as pd
from prophet import Prophet
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.sales import Sales
from app.models.forecast import Forecast
from app.database import SessionLocal


def generate_forecast(days_ahead: int = 14):
    """
    Generates forecasts for each product_id in Sales table using Prophet
    and stores results in Forecast table.
    """
    db: Session = SessionLocal()

    try:
        # Pull all sales data
        data = pd.read_sql("SELECT * FROM sales", db.bind)
        if data.empty:
            return "No sales data found."

        results = []
        for product_id, group in data.groupby("product_id"):
            # Prophet expects 'ds' and 'y' columns
            df = group.rename(columns={"date": "ds", "quantity_sold": "y"})
            df = df[["ds", "y"]].dropna()

            if len(df) < 3:
                continue  # not enough data to model

            model = Prophet(interval_width=0.8, daily_seasonality=True)
            model.fit(df)

            future = model.make_future_dataframe(periods=days_ahead)
            forecast = model.predict(future)

            # Keep only future predictions
            forecast_future = forecast.tail(days_ahead)

            # Save to DB
            for _, row in forecast_future.iterrows():
                f = Forecast(
                    product_id=product_id,
                    forecast_date=row["ds"].date(),
                    predicted_demand=float(row["yhat"]),
                    confidence=float(row["yhat_upper"] - row["yhat_lower"]),
                    model_used="Prophet",
                    created_at=datetime.utcnow(),
                )
                db.add(f)
            db.commit()

            results.append(
                {"product_id": product_id, "records": len(forecast_future)}
            )

        if not results:
            return "No forecasts generated — insufficient data."
        return {"forecasts_created": results}

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

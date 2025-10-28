from fastapi import APIRouter, Query, HTTPException
from app.services.forecast_service import generate_forecast

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.post("/run")
def run_forecast(days_ahead: int = Query(14, ge=1, le=60)):
    """
    Run Prophet forecasting for all products.
    """
    try:
        result = generate_forecast(days_ahead)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

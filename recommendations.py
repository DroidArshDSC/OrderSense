from fastapi import APIRouter, HTTPException
from app.services.recommendation_service import generate_recommendations

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.post("/run")
def run_recommendations():
    """
    Generate reorder recommendations based on forecasted demand.
    """
    try:
        result = generate_recommendations()
        return {"status": "success", "recommendations": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

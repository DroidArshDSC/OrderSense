from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.database import SessionLocal
from app.models.sales import Sales
from app.models.product import Product

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_sales_data(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    df = pd.read_csv(file.file) if file.filename.endswith(".csv") else pd.read_excel(file.file)

    required_cols = {"date", "product_id", "quantity_sold"}
    if not required_cols.issubset(df.columns):
        raise HTTPException(status_code=400, detail="Missing required columns")

    # Convert date strings to Python date objects
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date

    db = SessionLocal()
    try:
        for _, row in df.iterrows():
            record = Sales(
                product_id=str(row["product_id"]),
                date=row["date"],  # now a proper Python date
                quantity_sold=float(row["quantity_sold"]),
                price=float(row.get("price", 0)),
                location=str(row.get("location", "")),
                source="csv_upload",
            )
            db.add(record)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

    return {"status": "success", "records_uploaded": len(df)}
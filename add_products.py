from app.database import SessionLocal
from app.models.product import Product

db = SessionLocal()

products = [
    Product(
        product_id="SKU_101",
        name="Whole Milk 1L",
        category="Dairy",
        product_type="Perishable",
        shelf_life_days=10,
        lead_time_days=2,
        supplier="Mother Dairy"
    ),
    Product(
        product_id="SKU_102",
        name="Basmati Rice 1kg",
        category="Grocery",
        product_type="Non-Perishable",
        shelf_life_days=365,
        lead_time_days=5,
        supplier="India Gate"
    ),
]

db.add_all(products)
db.commit()
db.close()

print("✅ Product metadata inserted successfully.")

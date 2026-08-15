from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from typing import List


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Product]:
        return self.db.query(Product).offset(skip).limit(limit).all()

    def get_by_id(self, product_id: int) -> Product:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
        return product

    def create(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update(self, product_id: int, product_data: ProductUpdate) -> Product:
        product = self.get_by_id(product_id)
        for field, value in product_data.model_dump(exclude_unset=True).items():
            setattr(product, field, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product_id: int) -> dict:
        product = self.get_by_id(product_id)
        self.db.delete(product)
        self.db.commit()
        return {"message": f"Product {product_id} deleted successfully"}
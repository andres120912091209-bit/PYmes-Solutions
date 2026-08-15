from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    stock: int = Field(0, ge=0)
    category: Optional[str] = Field(None, max_length=80)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=120)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    category: Optional[str] = Field(None, max_length=80)
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    id: int
    is_active: bool
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
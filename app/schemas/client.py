from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class ClientBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    company: Optional[str] = Field(None, max_length=150)


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    company: Optional[str] = Field(None, max_length=150)
    is_active: Optional[bool] = None


class ClientResponse(ClientBase):
    id: int
    is_active: bool
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
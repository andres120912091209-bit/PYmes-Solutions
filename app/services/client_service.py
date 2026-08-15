from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate
from typing import List, Optional


class ClientService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Client]:
        return self.db.query(Client).offset(skip).limit(limit).all()

    def get_by_id(self, client_id: int) -> Client:
        client = self.db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail=f"Client {client_id} not found")
        return client

    def get_by_email(self, email: str) -> Optional[Client]:
        return self.db.query(Client).filter(Client.email == email).first()

    def create(self, client_data: ClientCreate) -> Client:
        if self.get_by_email(client_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        db_client = Client(**client_data.model_dump())
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def update(self, client_id: int, client_data: ClientUpdate) -> Client:
        client = self.get_by_id(client_id)
        for field, value in client_data.model_dump(exclude_unset=True).items():
            setattr(client, field, value)
        self.db.commit()
        self.db.refresh(client)
        return client

    def delete(self, client_id: int) -> dict:
        client = self.get_by_id(client_id)
        self.db.delete(client)
        self.db.commit()
        return {"message": f"Client {client_id} deleted successfully"}
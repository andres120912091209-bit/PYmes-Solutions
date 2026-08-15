from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.client import ClientCreate, ClientUpdate, ClientResponse
from app.services.client_service import ClientService

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.get("/", response_model=List[ClientResponse])
def list_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ClientService(db).get_all(skip, limit)


@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return ClientService(db).get_by_id(client_id)


@router.post("/", response_model=ClientResponse, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return ClientService(db).create(client)


@router.put("/{client_id}", response_model=ClientResponse)
def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
    return ClientService(db).update(client_id, client)


@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return ClientService(db).delete(client_id)
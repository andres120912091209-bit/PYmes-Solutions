from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import clients, products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pymes Solutions API",
    description="Backend API for SME management - Clients and Products modules",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clients.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": "Welcome to Pymes Solutions API",
        "version": "1.0.0",
        "docs": "/docs",
        "modules": ["clients", "products"]
    }
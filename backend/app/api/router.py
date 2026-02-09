from fastapi import APIRouter
from app.api.v1 import health

api_router = APIRouter()

# Подключаем роутер health
api_router.include_router(health.router, prefix="/api/v1")

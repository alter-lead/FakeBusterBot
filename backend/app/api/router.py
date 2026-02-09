from fastapi import APIRouter
from .v1 import health  # относительный импорт

api_router = APIRouter()

# Подключаем эндпоинт health
api_router.include_router(health.router, prefix="/v1")

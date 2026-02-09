from fastapi import FastAPI
from .api.router import api_router

app = FastAPI(
    title="FakeBuster API",
    description="Сервис проверки новостей на подлинность",
    version="0.1.0"
)

# Подключаем роутеры
app.include_router(api_router)

# Простой эндпоинт для проверки работы сервиса
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

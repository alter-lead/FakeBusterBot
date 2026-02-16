# Базовый образ Python
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Копируем requirements
COPY backend/requirements.txt ./backend/requirements.txt
COPY bot/requirements.txt ./bot/requirements.txt

# Устанавливаем зависимости backend и bot
RUN pip install --no-cache-dir -r backend/requirements.txt
RUN pip install --no-cache-dir -r bot/requirements.txt

# Копируем код
COPY backend/ ./backend/
COPY bot/ ./bot/

# Переменные окружения
ENV PYTHONUNBUFFERED=1

# Команда запуска БОТА
CMD ["python", "bot/app/main.py"]

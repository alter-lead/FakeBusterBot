import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# --- Явная загрузка .env ---
load_dotenv(dotenv_path=".env")  # путь к .env
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("Не найден TELEGRAM_TOKEN в bot/app/.env")

# --- Инициализация бота и диспетчера ---
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Обработчик команды /start ---
@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я FakeBusterBot. Готов проверять новости!")

# --- Асинхронный запуск бота ---
async def main():
    print("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")

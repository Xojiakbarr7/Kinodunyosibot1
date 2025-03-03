import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# .env fayldan o'zgaruvchilarni yuklaymiz
load_dotenv()

TOKEN = os.getenv("TOKEN")  # Tokenni to'g'ri yuklash
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Kanal ID

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'iga javob
async def start_command(message: types.Message):
    await message.answer("🎬 Salom! Kino kodini yuboring.")

# Kino kodini qabul qilish
async def get_movie(message: types.Message):
    code = message.text.strip()
    await message.answer(f"🔎 Siz yuborgan kod: {code}")  

# Handlerlarni ro‘yxatga olish
dp.message.register(start_command, commands=['start'])
dp.message.register(get_movie, lambda msg: msg.text is not None)

# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    print("✅ Bot ishga tushdi...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

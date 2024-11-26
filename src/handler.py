from aiogram.filters import Command, CommandStart
from aiogram import types, F
from app import bot, dp
from keyboards import main_kb
from aiogram.types import Message
import os

# Хэндлер на команду /start
@dp.message(CommandStart)
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=main_kb)

# Хэндлер на команду /start
@dp.message(F.photo)
async def get_photo(message: types.Message):
    image_id = message.photo[-1].file_id
    file_path = (await bot.get_file(image_id)).file_path
    downloaded_file = await bot.download_file(file_path)
    save_path = os.getenv('CERTIFICATE_BASE_PATH')
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file.getvalue())
    await message.reply('Шаблон сертификата сохранен')
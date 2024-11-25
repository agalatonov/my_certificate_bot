import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import F


load_dotenv()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO,  filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
# Объект бота
env_token=os.getenv('TOKEN')
bot = Bot(token=env_token)
# Диспетчер
dp = Dispatcher()

button_download_tamplate = KeyboardButton(text='Загрузить шаблон сертификата')
buttons = [button_download_tamplate]
main_kb = ReplyKeyboardMarkup(
    keyboard=[buttons], 
    resize_keyboard=True
    )

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=main_kb)

@dp.message(F.photo)
async def get_photo(message: types.Message):
    image_id = message.photo[-1].file_id
    file_path = (await bot.get_file(image_id)).file_path
    downloaded_file = await bot.download_file(file_path)
    save_path = os.getenv('CERTIFICATE_BASE_PATH')
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file.getvalue())
    await message.reply('Шаблон сертификата сохранен')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    await logging.info(f"token: {env_token}")
    
if __name__ == "__main__":
    asyncio.run(main())
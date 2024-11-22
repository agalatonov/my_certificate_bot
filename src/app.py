import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


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
main_kb = ReplyKeyboardMarkup(
    keyboard=button_download_tamplate, 
    resize_keyboard=True
    )


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=main_kb)

@bot.answer_callback_query

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    await logging.info(f"token: {env_token}")
    
if __name__ == "__main__":
    asyncio.run(main())
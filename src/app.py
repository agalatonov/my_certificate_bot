import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import F
from handler import router

load_dotenv()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO,  filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
# Объект бота
env_token=os.getenv('TOKEN')
bot = Bot(token=env_token)
# Диспетчер
dp = Dispatcher()



# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    await logging.info(f"token: {env_token}")
    
    
if __name__ == "__main__":
    asyncio.run(main())
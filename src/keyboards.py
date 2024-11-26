from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_download_tamplate = KeyboardButton(text='Загрузить шаблон сертификата')
buttons = [button_download_tamplate]
main_kb = ReplyKeyboardMarkup(
    keyboard=[buttons], 
    resize_keyboard=True
    )

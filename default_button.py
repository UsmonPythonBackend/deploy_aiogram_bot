from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Menu"))

menu_detail_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail_keyboard.add(KeyboardButton("Samsung s20"), KeyboardButton("Poco f5"), KeyboardButton("Samsung A34"))
menu_detail_keyboard.add(KeyboardButton("Back"))
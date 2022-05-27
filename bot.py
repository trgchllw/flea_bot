import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from text import *
from productone import *
from producttwo import *
from productthree import *
from productfour import *
from productfive import *

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="test")
async def test(message: types.Message):
    await message.reply("Bot is working!")

@dp.message_handler(commands="start")
async def menu(message: types.Message):
    btnshop = types.InlineKeyboardButton(BTNSHOP, callback_data="Shop")
    btnbasket = types.InlineKeyboardButton(BTNBASKET, callback_data="Basket")
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.add(btnshop)
    keyboard.add(btnbasket)
    await message.answer(WELCOME_TEXT, reply_markup=keyboard)

@dp.callback_query_handler()
async def menu2(message: types.Message):
    if message.data == "Shop":       
        btnlenta = types.InlineKeyboardButton(BTNLENTA, callback_data="Lenta")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnlenta)
        await bot.send_message(message.from_user.id, SHOP_TEXT, reply_markup=keyboard)

@dp.callback_query_handler()
async def first(message: types.Message):
    if message.data == "Lenta":       
        btnaddbasket = types.InlineKeyboardButton("Добавить в корзину", callback_data="none")
        btnurlone = types.InlineKeyboardButton("Купить", callback_data="none", url = URL_ONE)
        btnnextone = types.InlineKeyboardButton("След. товар", callback_data="next1")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnaddbasket)
        keyboard.add(btnurlone)
        keyboard.add(btnnextone)
        await bot.send_message(message.from_user.id, NAME_ONE, reply_markup=keyboard)

@dp.callback_query_handler()
async def second(message: types.Message):
    if message.data == "next1":       
        btnaddbasket = types.InlineKeyboardButton("Добавить в корзину", callback_data="none")
        btnurlone = types.InlineKeyboardButton("Купить", callback_data="none", url = URL_TWO)
        btnnextone = types.InlineKeyboardButton("След. товар", callback_data="next2")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnaddbasket)
        keyboard.add(btnurlone)
        keyboard.add(btnnextone)
        await bot.send_message(message.from_user.id, NAME_TWO, reply_markup=keyboard)

@dp.callback_query_handler()
async def third(message: types.Message):
    if message.data == "next2":       
        btnaddbasket = types.InlineKeyboardButton("Добавить в корзину", callback_data="none")
        btnurlone = types.InlineKeyboardButton("Купить", callback_data="none", url = URL_THREE)
        btnnextone = types.InlineKeyboardButton("След. товар", callback_data="next3")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnaddbasket)
        keyboard.add(btnurlone)
        keyboard.add(btnnextone)
        await bot.send_message(message.from_user.id, NAME_THREE, reply_markup=keyboard)

@dp.callback_query_handler()
async def fourth(message: types.Message):
    if message.data == "next3":       
        btnaddbasket = types.InlineKeyboardButton("Добавить в корзину", callback_data="none")
        btnurlone = types.InlineKeyboardButton("Купить", callback_data="none", url = URL_FOUR)
        btnnextone = types.InlineKeyboardButton("След. товар", callback_data="next4")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnaddbasket)
        keyboard.add(btnurlone)
        keyboard.add(btnnextone)
        await bot.send_message(message.from_user.id, NAME_FOUR, reply_markup=keyboard)

@dp.callback_query_handler()
async def fifth(message: types.Message):
    if message.data == "next4":       
        btnaddbasket = types.InlineKeyboardButton("Добавить в корзину", callback_data="none")
        btnurlone = types.InlineKeyboardButton("Купить", callback_data="none", url = URL_FIVE)
        btnnextone = types.InlineKeyboardButton("След. товар", callback_data="next5")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(btnaddbasket)
        keyboard.add(btnurlone)
        keyboard.add(btnnextone)
        await bot.send_message(message.from_user.id, NAME_FIVE, reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

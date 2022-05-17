import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def test(message: types.Message):
    await message.reply("TestMessage")

async def menu(message: types.Message):
    btnshop = types.InlineKeyboardButton(text="Магазин", callback="Shop"),
    btnbasket = types.InlineKeyboardButton(text="Корзина", callback="Basket")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(btnshop)
    keyboard.add(btnbasket)
    await message.answer("Приветствую в FleaMarket!", reply_markup=keyboard)

dp.register_message_handler(test, commands="test")
dp.register_message_handler(menu, commands="start")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, db, bot
import filters
import logging

filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Bo`tga kirish'
admin_message = 'W-Store(Admin)'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(user_message)

    await message.answer('''Assalomu Alaykum! 👋

🤖 Men har qanday toifadagi tovarlarni sotadigan bot-do'konman.
    
🛍️ Katalogga o'tish va o'zingizga yoqqan mahsulotlarni tanlash uchun buyruqdan foydalaning /menu.

💰 Tavarni harid qilgach 50% oldindan to'lov va qolgani yetqazilgandan so'ng bo'ladi.

🤔 Savollaringiz bormi❓ Muammo emas! /sos buyrug'i sizga imkon qadar tezroq javob berishga harakat qiladi va administratorlar bilan bog'lanishga yordam beradi.
    ''', reply_markup=markup)


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):

    cid = message.chat.id
    if cid in config.ADMINS:
        config.ADMINS.remove(cid)

    await message.answer('Tashrif uchun tashakkur! Haridni boshlamoqchimsiz?\n\nBuning uchun bosing 👉🏻 /menu',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):

    cid = message.chat.id
    if cid not in config.ADMINS:
        config.ADMINS.append(cid)

    await message.answer('Administrator rejimi 🛒 .', reply_markup=ReplyKeyboardMarkup())


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()

    await bot.delete_webhook()
    await bot.set_webhook(config.WEBHOOK_URL)


async def on_shutdown():
    logging.warning("O`chirish..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bo`t pastga")


if __name__ == '__main__':

    if "HEROKU" in list(os.environ.keys()):

        executor.start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )

    else:

        executor.start_polling(dp, on_startup=on_startup, skip_updates=False)

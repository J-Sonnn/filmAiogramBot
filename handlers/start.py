from aiogram import types
from loader import dp, bot
from database import DB
from keyboards import inline


# Команда старт
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user = await DB.select_user_id(message.from_user.id)

    if not user:
        await DB.add_user_id(message.from_user.id)

    await bot.send_photo(message.chat.id, open('startFoto.jpg', 'rb'),
                         caption="<b>⚙ Выберите действие:</b>",
                         parse_mode='html', reply_markup=await inline.menu())


# Назад
@dp.callback_query_handler(text=["back"])
async def back(call: types.CallbackQuery):
    await call.message.delete()

    await bot.send_photo(call.message.chat.id, open('startFoto.jpg', 'rb'),
                         caption="<b>⚙ Выберите действие:</b>",
                         parse_mode='html', reply_markup=await inline.menu())

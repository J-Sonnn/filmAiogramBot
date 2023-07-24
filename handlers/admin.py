from aiogram import types
from loader import dp, bot
from database import DB
from keyboards import inline
from utils import string


# Количество пользователей в боте
@dp.message_handler(commands=["admin"])
async def admin(message: types.Message):
    if message.from_user.id in await DB.select_users_from_admin():
        await bot.send_message(message.from_user.id,
                               f"<b>Пользователей в боте: {len(await DB.select_users_from_table())}</b>",
                               reply_markup=await inline.back_admin(), parse_mode="html")


# Рассылка
@dp.message_handler(commands=["send"])
async def text(message: types.Message):
    if message.from_user.id in await DB.select_users_from_admin():
        for i in await DB.select_users_from_table():
            try:
                await bot.send_message(i, text=message.text.split('/send ')[1])
            except:
                pass


# Включение/Выключение платы за просмотр ссылки на фильм
@dp.message_handler(commands=["onurl", "offurl"])
async def admin(message: types.Message):
    if message.from_user.id in await DB.select_users_from_admin():
        await DB.update_filmURL(message.text.replace("/", "").replace("url", ""), 1)
        await bot.send_message(message.from_user.id, f"<b>Успешно изменено!</b>",
                               reply_markup=await inline.back_admin(), parse_mode="html")


# Включение/Выключение подписки на канал
@dp.message_handler(commands=["onsub", "offsub"])
async def admin(message: types.Message):
    if message.from_user.id in await DB.select_users_from_admin():
        await DB.update_filmSUB(message.text.replace("/", "").replace("sub", ""), 1)
        await bot.send_message(message.from_user.id, f"<b>Успешно изменено!</b>",
                               reply_markup=await inline.back_admin(), parse_mode="html")


# Добавить админа
@dp.message_handler(commands=["addadmin"])
async def add(message: types.Message):
    if message.from_user.id in await DB.select_users_from_admin():
        await DB.add_admin(message.text.replace("/addadmin ", ""))
        await bot.send_message(message.from_user.id, 'Успешно! ✅')


# Все команды админа
@dp.message_handler(commands=["botinfo"])
async def botinfo(message: types.Message):
    if message.from_user.id in await DB.select_users_from_admin():
        await bot.send_message(message.from_user.id, string.botinfo(), parse_mode="html")

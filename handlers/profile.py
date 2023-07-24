import config
from database import DB
from aiogram import types
from keyboards import inline
from loader import dp, bot


# Профиль
@dp.callback_query_handler(text="profile")
async def profile(call: types.CallbackQuery):
    if await DB.select_filmSUB() == "on":
        diction = {"inline": await inline.profile()}
    else:
        diction = {"inline": await inline.back_admin()}

    await bot.send_message(chat_id=call.message.chat.id,
                           text=f"<b>💰 Баланс: {await DB.selectBalance(call.from_user.id)}</b>",
                           reply_markup=diction["inline"], parse_mode="html")


# Получить пробые монеты
@dp.callback_query_handler(text="get")
async def get(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id,
                           text=f"<b>Монеты нужны для открытия кнопки 'Смотреть 👀', с помощю неё вы можете переходить по ссылке на выбранный фильм!\n\nЧтобы получить 50 пробных монет, вам нужно подписаться на канал ниже 👇</b>",
                           reply_markup=await inline.get_balance(), parse_mode="html")


# Проверка на подписку
@dp.callback_query_handler(text="checkSubscribe")
async def checkSubscribe(call: types.CallbackQuery):
    try:
        if await DB.select_quantitySub(call.from_user.id) != 1:
            user_channel_status = await bot.get_chat_member(chat_id=config.chaiID, user_id=call.from_user.id)

            if user_channel_status["status"] != 'left':
                await DB.updateBalance(call.from_user.id, int(await DB.selectBalance(call.from_user.id)) + 50)
                await DB.update_quantitySub(call.from_user.id, 1)

                await bot.send_message(chat_id=call.message.chat.id,
                                       text=f"<b>Поздравляю, вы получили 50 пробных монет! 🎉</b>",
                                       reply_markup=await inline.back_admin(), parse_mode="html")
        else:
            await bot.answer_callback_query(call.id, "Вы не подписальсь или уже использовали лимит подписок!")

    except:
        await bot.answer_callback_query(call.id, "Вы не подписальсь или уже использовали лимит подписок!")

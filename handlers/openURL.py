from aiogram import types
import config
from loader import dp, bot
from keyboards import inline
from database import DB


# Открыть ссылку на фильм
@dp.callback_query_handler(text=["open"])
async def open(call: types.CallbackQuery):
    if await DB.select_filmURL() == "on":
        if await DB.selectBalance(call.from_user.id) >= config.priceURL:
            await DB.updateBalance(call.from_user.id, await DB.selectBalance(call.from_user.id) - config.priceURL)

            await bot.send_message(call.from_user.id, "<b>Ссылка на фильм:</b>",
                                   parse_mode='html',
                                   reply_markup=await inline.film_url(await DB.select_URL(call.from_user.id)))

        else:
            await bot.answer_callback_query(call.id, "Не достаточно баланса!")


    else:
        await bot.send_message(call.from_user.id, "<b>Ссылка на фильм:</b>",
                               parse_mode='html',
                               reply_markup=await inline.film_url(await DB.select_URL(call.from_user.id)))

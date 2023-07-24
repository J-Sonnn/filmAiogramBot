from aiogram import types
from loader import dp, bot
from keyboards import inline
from utils import string
from random import randint
from database import DB


# Случайный фильм
@dp.callback_query_handler(text=["randomFilm", "nextRandom"])
async def random(call: types.CallbackQuery):
    random = randint(1, 2002)

    filmInfo = await DB.select_filmInfo(random, "allFilm")
    await DB.update_URL(call.from_user.id, filmInfo[2])

    genre = str(filmInfo[3: -2]).replace(",", "").replace("(", "").replace(")", "").replace("'", "")

    await bot.send_photo(call.from_user.id, filmInfo[0],
                         caption=string.film_info(filmInfo[1], genre, filmInfo[-2], filmInfo[-1]),
                         parse_mode='html', reply_markup=await inline.randomFlm())

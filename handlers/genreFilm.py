from aiogram import types
from loader import dp, bot
from database import DB
from keyboards import inline
from utils import string
from random import randint

listGenre = ["drama", "boevik", "fjuntezia", "triller", "komedia", "melodrama", "biografia", "semejnye",
             "istoricheskie", "prikluchenija", "kriminaly", "detektivy", "dokumentalenyj", "sports", "nextGenre"]


# Поиск фильма по жанру
@dp.callback_query_handler(text=["genre"])
async def genre(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "<b>⚙ Выберете категорию фильма:</b>", reply_markup=await inline.genre(),
                           parse_mode="html")


# Выбор жанра фильма
@dp.callback_query_handler(text=listGenre)
async def filmGenre(call: types.CallbackQuery):
    if call.data != "nextGenre":
        await DB.updateGenre(call.from_user.id, call.data)

    random = randint(1, 564)

    filmInfo = await DB.select_filmInfo(random, await DB.selectGenre(call.from_user.id))

    await DB.update_URL(call.from_user.id, filmInfo[2])

    genre = str(filmInfo[3: -2]).replace(",", "").replace("(", "").replace(")", "").replace("'", "")

    await bot.send_photo(call.from_user.id, filmInfo[0],
                         caption=string.film_info(filmInfo[1], genre, filmInfo[-2], filmInfo[-1]),
                         parse_mode='html', reply_markup=await inline.genreFilm())

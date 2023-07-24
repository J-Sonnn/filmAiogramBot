from aiogram.dispatcher import FSMContext
from aiogram import types
from utils import string
from loader import dp, bot
from database import DB
from keyboards import default, inline
from state import states
from utils import parser_allFilm


# Поиск фильма
@dp.callback_query_handler(text=["searchFilm"])
async def search(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id,
                           "*Напишите название фильма ✏️*",
                           reply_markup=await default.back(),
                           parse_mode="MarkdownV2")

    await states.search.name.set()


@dp.message_handler(state=states.search.name)
async def state(message: types.Message, state: FSMContext):
    if message.text == 'Назад ↩':
        await state.finish()

        await bot.send_message(message.chat.id, '<b>Секунду...</b>', parse_mode="html", reply_markup=default.remove)

        await bot.send_photo(message.chat.id, open('startFoto.jpg', 'rb'),
                             caption="<b>⚙ Выберите действие:</b>",
                             parse_mode='html', reply_markup=await inline.menu())

    else:
        await bot.send_message(message.chat.id, '<b>Поиск фильмов 🔎</b>', parse_mode="html",
                               reply_markup=default.remove)

        await DB.update_key(message.from_user.id, 0)

        all_info = await parser_allFilm.Film.filmInfo(message.text, 0)

        if all_info != None:
            await state.finish()

            await DB.update_URL(message.from_user.id, all_info[1])
            await DB.update_filmName(message.from_user.id, message.text)

            await bot.send_photo(message.from_user.id, all_info[0],
                                 caption=string.film_info_search(all_info[2], all_info[3], all_info[-1], all_info[-2]),
                                 parse_mode='html', reply_markup=await inline.film_text())


        else:
            await bot.send_message(message.chat.id,
                                   '<b>К сожелению нам не удалось ничего найти!\n\nПовторите ещё раз 🔄</b>',
                                   parse_mode="html", reply_markup=await default.back())


# Кнопка далее в поиске фильмов
@dp.callback_query_handler(text=["nextSearch"])
async def nextSearch(call: types.CallbackQuery):
    await DB.update_key(call.from_user.id, await DB.select_key(call.from_user.id) + 1)

    all_info = await parser_allFilm.Film.filmInfo(await DB.select_filmName(call.from_user.id),
                                                  await DB.select_key(call.from_user.id))

    if all_info != None:

        await DB.update_URL(call.from_user.id, all_info[1])

        await bot.send_photo(call.from_user.id, all_info[0],
                             caption=string.film_info_search(all_info[2], all_info[3], all_info[-1], all_info[-2]),
                             parse_mode='html', reply_markup=await inline.film_text())


    else:
        await bot.answer_callback_query(call.id, 'На этом всё 😊')

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def menu():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    randomFilm = InlineKeyboardButton(text='Случайный фильм 🎬🎲', callback_data='randomFilm')
    searchFilm = InlineKeyboardButton(text='Найти фильм 🔎', callback_data='searchFilm')
    keyboard.add(randomFilm, searchFilm)
    keyboard.add(InlineKeyboardButton(text='Категории фильмов ⚙', callback_data='genre'))
    keyboard.add(InlineKeyboardButton(text='Профиль 📝', callback_data='profile'))
    return keyboard


async def genre():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        InlineKeyboardButton(text='Драма 💄', callback_data='drama'),  # 1780
        InlineKeyboardButton(text='Боевик 🦿', callback_data='boevik'),  # 544
        InlineKeyboardButton(text='Фэнтези 🌈', callback_data='fjuntezia'),  # 179
        InlineKeyboardButton(text='Триллер 🎭', callback_data='triller'),  # 820
        InlineKeyboardButton(text='Комедия 🥥', callback_data='komedia'),  # 1082
        InlineKeyboardButton(text='Мелодрама 🦋', callback_data='melodrama'),  # 586
        InlineKeyboardButton(text='Биография 🧩', callback_data='biografia'),  # 119
        InlineKeyboardButton(text='Семейный 🧲', callback_data='semejnye'),  # 185
        InlineKeyboardButton(text='Исторические 🖼', callback_data='istoricheskie'),  # 141
        InlineKeyboardButton(text='Приключения 🧸', callback_data='prikluchenija'),  # 277
        InlineKeyboardButton(text='Криминал 🗡', callback_data='kriminaly'),  # 387
        InlineKeyboardButton(text='Детектив 🗝', callback_data='detektivy'),  # 235
        InlineKeyboardButton(text='Документальные 📇', callback_data='dokumentalenyj'),  # 524
        InlineKeyboardButton(text='Спорт 🥊', callback_data='sports'),  # 63
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def randomFlm():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Открыть ссылку на фильм', callback_data='open'),
        InlineKeyboardButton(text='Далее ➡', callback_data='nextRandom'),
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def genreFilm():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Открыть ссылку на фильм', callback_data='open'),
        InlineKeyboardButton(text='Далее ➡', callback_data='nextGenre'),
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def film_text():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Открыть ссылку на фильм', callback_data='open'),
        InlineKeyboardButton(text='Далее ↪️', callback_data='nextSearch'),
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def film_url(url):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Смотреть 👀', url=url),
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def back_admin():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def profile():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Получить 50 пробных монет!', callback_data='get'),
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard


async def get_balance():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Подписаться!', url="https://t.me/DigitalWorldShoping"),
        InlineKeyboardButton(text='Я подписаться! ✅', callback_data='checkSubscribe'),
        InlineKeyboardButton(text='Назад ↩', callback_data='back'))
    return keyboard

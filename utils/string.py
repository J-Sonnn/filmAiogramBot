def film_info(name, genre, year, text):
    return f"""<b>🧷 {name} ({year})

🛠 Жанр: {genre}

📝 Описание: {text}</b>
"""


def film_info_search(name, year, genre, country):
    return f"""<b>🧷 {name} ({year})

🛠 Жанр: {genre}

🎥 Страна: {country}</b>
"""


def search_film_info(name, year, text):
    return f"""<b>🧷 {name} ({year})

📝 Описание: {text}</b>
"""


def botinfo():
    return """
<b>admin - количество пользователей в боте
    
send - рассылка
    
onurl - включить плату за просмотр ссылки на фильм
offurl - выключить плату за просмотр ссылки на фильм
    
onsub - включить обязательную подписку
offsub - выключить обязательную подписку
    
addadmin - добавить админа</b>
"""

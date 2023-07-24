import requests as requests
from bs4 import BeautifulSoup


class Film:
    __MAIN_URL = 'https://rezka.ag/search/?do=search&subaction=search&q='

    @staticmethod
    async def filmInfo(name: str, key: int):
        url = Film.__MAIN_URL + name.lower().replace(" ", "+")

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        photo_link = soup.findAll("div", class_="b-content__inline_item-cover")
        name_info = soup.findAll("div", class_="b-content__inline_item-link")

        try:
            photo_trash = str(photo_link[key]).replace('<div class="b-content__inline_item-cover"> <a href="', "").split()

            for i in photo_trash:
                if 'src="' in i:
                    photo = i.replace('src="', "").replace('"', "")

            link = str(photo_link[key]).replace('<div class="b-content__inline_item-cover"> <a href="', "").replace('">', "").split()[0]

            name = str(name_info[key].text.split()[:-3]).replace(",", "").replace("'", "").replace("[", "").replace("]", "")

            year = name_info[key].text.split()[-3].replace(",", "")

            country = name_info[key].text.split()[-2].replace(",", "")

            genre = name_info[key].text.split()[-1]

            return photo, link, name, year, country, genre
        except IndexError:
            return None

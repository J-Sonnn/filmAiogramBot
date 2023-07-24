import aiosqlite

dbname = "filmBot.db"


async def add_user_id(user_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute("INSERT INTO `user` (`user_id`) VALUES (?)", (user_id,))
        return await connection.commit()


async def select_user_id(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `user_id` FROM `user` WHERE `user_id`=?", (user_id,))
        return await cursor.fetchone()



async def select_users_from_table():
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `user_id` FROM `user`")
        result = await cursor.fetchall()
        return [row[0] for row in result]


async def select_users_from_admin():
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `user_id` FROM `user_admin`")
        result = await cursor.fetchall()
        return [row[0] for row in result]


async def add_admin(user_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute("INSERT INTO `user_admin` (`user_id`) VALUES (?)", (user_id,))
        return await connection.commit()


async def select_filmInfo(key, table):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `photo`, `name`, `url`, `genre`, `year`, `text` FROM `{table}` WHERE `key`=?",
                             (key,))
        return await cursor.fetchone()


async def select_filmURL():
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `filmURL` FROM `admin`", )
        result = await cursor.fetchone()
        return result[0]


async def update_filmURL(text, key):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `admin` SET `filmURL`=? WHERE `key`=?", (text, key))
        return await connection.commit()


async def select_filmSUB():
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `filmSUB` FROM `admin`", )
        result = await cursor.fetchone()
        return result[0]


async def update_filmSUB(text, key):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `admin` SET `filmSUB`=? WHERE `key`=?", (text, key))
        return await connection.commit()


async def update_URL(user_id, URL):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `URL`=? WHERE `user_id`=?", (URL, user_id))
        return await connection.commit()


async def select_URL(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `URL` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectBalance(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `balance` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def updateBalance(user_id, balance):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `balance`=? WHERE `user_id`=?", (balance, user_id))
        return await connection.commit()


async def selectGenre(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `genre` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def updateGenre(user_id, genre):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `genre`=? WHERE `user_id`=?", (genre, user_id))
        return await connection.commit()


async def update_quantitySub(user_id, sum):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `quantitySub`=? WHERE `user_id`=?", (sum, user_id,))
        return await connection.commit()


async def select_quantitySub(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `quantitySub` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def update_filmName(user_id, name):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `filmName`=? WHERE `user_id`=?", (name, user_id,))
        return await connection.commit()


async def select_filmName(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `filmName` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def update_key(user_id, key):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `key`=? WHERE `user_id`=?", (key, user_id,))
        return await connection.commit()


async def select_key(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `key` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]

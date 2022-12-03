import sqlite3 as sq
from createcode import bot


def sql_start():
    global base, cur
    base = sq.connect('client_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connect OK!')
    base.execute("CREATE TABLE IF NOT EXISTS menu(ing TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)")
    base.commit()



async def sql_add_commands(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:  {ret[-1]}')
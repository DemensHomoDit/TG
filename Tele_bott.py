from aiogram.utils import executor
from createcode import dp
from data_base import sqlite_db





async def on_startup(_):
	print('Бот вышел в онлайн')
sqlite_db.sql_start()


from handlers import client, Admin

Admin.register_handlers_admin(dp)
client.register_handlers_client(dp)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

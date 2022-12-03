from aiogram import Bot, Dispatcher
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot: Bot = Bot(token=os.getenv('TOKEN'))
dp: Dispatcher = Dispatcher(bot, storage=storage)

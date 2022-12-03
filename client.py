import sqlite3
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types, Dispatcher
from createcode import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from KeyBoards import client_kb
#@dp.message_handler(commands=['start', 'help'])



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=[ 'start', 'help' ])



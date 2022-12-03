from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from createcode import Dispatcher, bot
from aiogram.dispatcher.filters import Text
from KeyBoards import admin_kb


ID=414682869

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    descripten = State()
    price = State()


#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_commands(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Выберите действия" , reply_markup=admin_kb.button_case_admin)
    await message.delete()

#Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == 414682869:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото')


#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def  load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == ID:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введите название')

#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == ID:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введите описание')


#@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == ID:
            data['price'] = float(message.text)

    await sqlite_db.sql_add_commands(state)
    await state.finish()


#@dp.message_handler(state='*', commands='отмена')
#@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("ОК")


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_commands, commands=[ 'moderator' ], is_chat_admin=True)
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands="отмена")
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case = True), state = '*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_price, state=FSMAdmin.price)




# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cinfig_s import TOKEN

import datetime
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Form(StatesGroup):
	send = State()
	send_message = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Ваши сообщения будут отправлены администратору")
    await Form.send.set()


@dp.message_handler(commands=['send_message'])
async def process_start_command(message: types.Message):
    await message.answer('Введите id юзера')
    await Form.send_message.set()


@dp.message_handler(state=Form.send)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
    	wol = message.text
    	sms = '"{}" \nuser_id:{} \nuser_name: {} '.format(wol, message.from_user.id, message.from_user.username)
    	await bot.send_message('1017470547', sms)
    	f = open('users.txt', 'a')
    	f.write(sms + '\n' + '-----------' + '\n')


@dp.message_handler(state=Form.send)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:


if __name__ == '__main__':
    executor.start_polling(dp)
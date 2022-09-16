# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import schedule

with open("token.txt", "r") as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer("""Все команды: 
/help 
/schedule 
/today 
/tomorrow 
/next_week""")

@dp.message_handler(commands=['schedule'])
async def send_schedule(msg: types.Message):
    dashboard = schedule.get_schedule()
    await msg.answer(dashboard, parse_mode="HTML")


@dp.message_handler(commands=['today'])
async def send_today(msg: types.Message):
    dashboard = schedule.get_schedule_today()
    await msg.answer(dashboard, parse_mode="HTML")


@dp.message_handler(commands=['tomorrow'])
async def send_tomorrow(msg: types.Message):
    dashboard = schedule.get_schedule_tomorrow()
    await msg.answer(dashboard, parse_mode="HTML")


@dp.message_handler(commands=['next_week'])
async def send_next_week(msg: types.Message):
    dashboard = schedule.get_schedule_next_week()
    await msg.answer(dashboard, parse_mode="HTML")

@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.answer("""Команды:
    /schedule - расписание на текущую неделю
    /today - расписание на текущий день
    /tomorrow - расписание на завтра
    /next_week - расписание на следующую неделю
    """)


if __name__ == '__main__':
    executor.start_polling(dp)

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import schedule

with open("token.txt", "r") as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['расписание'])
async def send_welcome(msg: types.Message):
    dashboard = schedule.get_schedule()
    await msg.reply(dashboard, parse_mode="HTML")


@dp.message_handler(commands=['сегодня'])
async def send_welcome(msg: types.Message):
    dashboard = schedule.get_schedule_today()
    await msg.reply(dashboard, parse_mode="HTML")


@dp.message_handler(commands=['завтра'])
async def send_welcome(msg: types.Message):
    dashboard = schedule.get_schedule_tomorrow()
    await msg.reply(dashboard, parse_mode="HTML")


@dp.message_handler(commands=['след_неделя'])
async def send_welcome(msg: types.Message):
    dashboard = schedule.get_schedule_next_week()
    await msg.reply(dashboard, parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp)

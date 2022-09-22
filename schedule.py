# -*- coding: utf-8 -*-
import datetime
import json

import requests
import re


week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
with open("auth.json", 'r') as f:
    auth = json.load(f)







def get_schedule():
    sess = requests.session()
    sess.post("https://ies.unitech-mo.ru/auth", data=auth)
    resp = sess.post(f"https://ies.unitech-mo.ru/schedule", data={"load": 1})

    message = ""
    for i in range(1, 8):
        message += "========================\n"
        message += f"\n<b>{week[i]}</b>\n\n"

        for day in resp.json():
            if day['daynum'] == i:
                message += "--------------------------\n"
                message += f"Пара №{day['timenum']}\n"
                message += f"Время: {day['time']}\n"
                message += f"{day['lparam']}\n"
    sess.close()
    return message


def get_schedule_today():
    sess = requests.session()
    sess.post("https://ies.unitech-mo.ru/auth", data=auth)
    resp = sess.post(f"https://ies.unitech-mo.ru/schedule", data={"load": 1})

    today = datetime.datetime.today().weekday() + 1
    message = ""
    message += f"<b>{week[today]}</b>\n"
    for day in resp.json():
        if day['daynum'] == today:
            message += "--------------------------\n"
            message += f"Пара №{day['timenum']}\n"
            message += f"Время: {day['time']}\n"
            message += f"{day['lparam']}\n"


    sess.close()
    return message


def get_schedule_tomorrow():
    sess = requests.session()
    sess.post("https://ies.unitech-mo.ru/auth", data=auth)
    resp = sess.post(f"https://ies.unitech-mo.ru/schedule", data={"load": 1})

    tomorrow = (datetime.datetime.today().weekday() + 2) % 8
    message = ""
    message += f"<b>{week[tomorrow]}</b>\n"
    for day in resp.json():
        if day['daynum'] == tomorrow:
            message += "--------------------------\n"
            message += f"Пара №{day['timenum']}\n"
            message += f"Время: {day['time']}\n"
            message += f"{day['lparam']}\n"
    sess.close()
    return message


def get_schedule_next_week():
    date = datetime.datetime.now() + datetime.timedelta(days=(7 - datetime.datetime.now().weekday()))
    delta_date = date + datetime.timedelta(days=7)
    sess = requests.session()
    sess.post("https://ies.unitech-mo.ru/auth", data=auth)
    resp = sess.post(
        f"https://ies.unitech-mo.ru/schedule?d={date.day}.{date.month}.{date.year}+-+{delta_date.day}.{delta_date.month}.{delta_date.year}",
        data={"load": 1})

    message = ""
    for i in range(1, 8):
        message += "========================\n"
        message += f"\n<b>{week[i]}</b>\n\n"

        for day in resp.json():
            if day['daynum'] == i:
                message += "--------------------------\n"
                message += f"Пара №{day['timenum']}\n"
                message += f"Время: {day['time']}\n"
                message += f"{day['lparam']}\n"
    sess.close()
    return message




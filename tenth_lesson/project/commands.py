from random import random

from aiogram.types import InputFile

import messages
import model
from create_bot import bot
from aiogram import types

async def start(message: types.Message):
    model.setCount(int(model.getUserCount()))
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}\n'
                                                 f'Это игра про конфеты! Смысл игры\n'
                                                 f'Вы с ботом поочереди берте конфеты')
    model.setFirstTurn()
    first_turn = model.getFirstTurn()
    if first_turn:
        awaitplayerTake(massage)
    else:
        await enemyTurn(message)

async def help(message:types.Message):
    path = InputFile(kkk.png)
    await bot.send_message(message.from_user.id,f'Ну и чтоздесь непонятно')
    await bot.send_message(message.from_user.id, photo = path)

async def set_count(message: types.Message):
    count = message.text.split()
    if len(count) == 2:
        model.setUserCount(int(count[1]))
    await bot.send_message(message.from_user.id, f'Стартовое количество конфет \n'
                                                 f'изменено на на {model.getUserCount()}')

async def playerTurn(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.username}, '
                                                 f'берите конфеты (не больше 28)')

async def playerTurn(message: types.Message):
    take = None
    if message.text.isdigit():
        if int(message.text) < 0 or int(message.text) > 28:
            await bot.send_message(message.from_user.id, f'Брать стоит не более 28 конфет')
        else:
            take = int(message.text)
            model.setTake(int(message.text))
            model.setCount(model.getCount() - take)
            await bot.send_message(message.from_user.id, f'{message.from_user.username} взял {take} конфет,'
                                                         f'на столе осталосm {model.getCount()} конфет')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.id},'
                                                     f'введите число')

async def enemyTurm(message: types.Message):
    count = model.getCount()
    take = count%29 if count%29 != 0 else random.randint(1,28)
    model.setTake(take)
    model.setCount(count - take)
    await bot.send_message(message.from_user.id, f'Бот взял{model.getTake()} клнфет,'
                                                 f'введите число')

    if model.checkWin():
        await bot.send_message(message.from_user.id, messages.bot_win)
        return
    await playerTake(message)






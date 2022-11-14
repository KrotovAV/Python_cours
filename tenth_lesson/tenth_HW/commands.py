from random import random

import model
from create_bot import bot
from aiogram import types

async def start(message: types.Message):
    model.setCount(int(model.getUserCount()))
    await bot.send_message(message.from_user.id, f'На столе палочек {model.getCount()} шт, '
                                                 f'брать можно не более {model.get_Max_Take()} штук за раз.\n')
    model.setFirstTurn()
    turn = model.getFirstTurn()
    model.setGameTurn(turn)
    if turn == 2:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, введите число')
    else:
        count = model.getCount()
        take = count%model.get_Max_Take()+1 if count%model.get_Max_Take()+1 != 0 else random.randint(1, model.get_Max_Take())
        model.setTake(take)
        model.setCount(count - take)
        await bot.send_message(message.from_user.id, f'Мастер взял {model.getTake()} шт,\n'
                                                 f'на столе осталось {model.getCount()} шт')
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Ваш ход ')

async def help(message:types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name} ! '
                                                 f'Это игра про палочки! Смысл игры в том, что '
                                                 f'Вы с Мастером поочереди берте палочки. '
                                                 f'Кто взял последнюю - тот проиграл.')
    await bot.send_message(message.from_user.id,f'На столе палочек {model.getCount()} шт, '
                                                f'а брать за раз можно не более {model.get_Max_Take()} шт.\n'
                                                f'Введите\n"/set_count x y" (x-общее количество, y-сколько можно брать) '
                                                f'что бы изменить значения по умолчанию,\n'
                                                f'"/start" - для начала игры,\n'
                                                f'"/help" - что бы увидеть это меню,\n'
                                                f'"/stop" что бы закончить игру')

async def stop(message:types.Message):
    await bot.send_message(message.from_user.id, f'ОК, {message.from_user.first_name}, стоп игра! ')
    return

async def set_count(message: types.Message):
    await bot.send_message(message.from_user.id, f'По умолчанию стартовое количество палочек = {model.total_count} шт.\n')
    count = message.text.split()
    if len(count) > 1:
        model.setUserCount(int(count[1]))
    await bot.send_message(message.from_user.id, f'было изменено на {model.getUserCount()} шт.')
                                                 
    await bot.send_message(message.from_user.id, f'Стартовое количество палочек, которое можно брать {model.get_Max_Take()} шт.')
    max_Take = message.text.split()
    if len(max_Take) > 2:
        model.set_Max_Take(int(max_Take[2]))
    await bot.send_message(message.from_user.id, f'было изменено на {model.get_Max_Take()} шт.')

async def player_Choice(message: types.Message):
    turn = model.getGameTurn()
    if message.text.isdigit():
        if int(message.text) < 0 or int(message.text) > model.get_Max_Take():
            await bot.send_message(message.from_user.id, f'Брать можно не более {model.get_Max_Take()} палочек!')
            take = model.get_Max_Take()
        if model.getCount() < model.get_Max_Take():
            take = model.getCount() - 1
        else:
            take = int(message.text)

        model.setTake(int(message.text))
        model.setCount(model.getCount() - take)
        await bot.send_message(message.from_user.id, f' на столе осталось {model.getCount()} шт')
    # else:
    #     await bot.send_message(message.from_user.id, f'{message.from_user.first_name} введите число')
    if model.checkWin():
        await bot.send_message(message.from_user.id, f'Ну что, {message.from_user.first_name} !?,')
        await bot.send_message(message.from_user.id, f'На этот раз Мастер одержал победу!!!')
        return

    count = model.getCount()
    if count == model.get_Max_Take()+1: take = 1
    if count >= model.get_Max_Take():
        take = count%model.get_Max_Take()+1 if count%model.get_Max_Take()+1 != 0 else random.randint(1, model.get_Max_Take())
    if count < model.get_Max_Take():
        if count-1 == 0 or count-1 < 0 : 
            take = count
        else:
            if count == 3: take = count-1
            if count == 2: take = count-1
    model.setTake(take)
    model.setCount(count - take)
    await bot.send_message(message.from_user.id, f'Мастер взял {model.getTake()} шт,\n'
                                                 f'на столе осталось {model.getCount()} шт')

    if model.checkWin():
        await bot.send_message(message.from_user.id, f'Ну что, {message.from_user.first_name} !?,')
        await bot.send_message(message.from_user.id, f'Это блистательная ПОБЕДА!!!')
        return
    
    model.setGameTurn(turn)
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Ваш ход!')


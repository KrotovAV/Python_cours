import random
from aiogram import types
from create_bot import bot
from aiogram import types

user_count = 21
total_count = user_count
turn = None
game_turn = None
max_take = 3
take = None

def getFirstTurn():
    global turn
    return turn

def setFirstTurn():
    global turn
    turn = random.randint(1,2)

def getGameTurn():
    global game_turn
    return game_turn

def setGameTurn(turn):
    global game_turn
    if turn == 1:
        turn = 2
    else:
         turn = 1
    game_turn = turn

def getTake():
    global take
    return take

def setTake(new_take: int):
    global take
    take = new_take

def getCount():
    global total_count
    return total_count

def get_Max_Take():
    global max_take
    return max_take

def set_Max_Take(dif_take: int):
    global max_take
    max_take = dif_take

def setCount(count: int):
    global total_count
    total_count = count

def getUserCount():
    global user_count
    return user_count

def setUserCount(count: int):
    global user_count
    user_count = count

def checkWin():
    if getCount() <=0:
        return True


from aiogram import Dispatcher
from aiogram import types
import commands

def registred_handlers(dp: Dispatcher):
    # dp.register_message_handler(messages.any_mess, content_types=['text'])
    dp.register_message_handler(commands.start,commands=['start'])
    dp.register_message_handler(commands.help,commands=['help'])
    dp.register_message_handler(commands.set_count,commands=['set_count'])
    dp.register_message_handler(commands.stop,commands=['stop'])

    dp.register_message_handler(commands.player_Choice, content_types = ['text'] )
    # dp.register_message_handler(commands.player_Choice, content_types = ['isdigit()'])



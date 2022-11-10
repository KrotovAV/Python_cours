# pip install python-telegram-bot

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_command import *
# import datetime

updater = Updater('5181600578:AAEPU7j2TZENT1k7tWWBAyP8kIwWDWmowhM')

updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')

updater.start_polling()
updater.idle()


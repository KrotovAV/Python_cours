from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import * 


def hello_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}!')

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hello\n/hi\n/help')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi - {datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    # print(msg)
    items = msg.split() # /sum 153 165
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}') 
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    file = open('d:/GeekBrains/My Git/2 znakomstvo s iazikami/02 python/Python_cours/fifth_lekcion/project/db.csv', 'a', encoding='utf8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

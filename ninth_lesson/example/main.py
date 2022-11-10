# https://habr.com/ru/company/selectel/blog/685206/
import logging
from telegram import Update
from telegram.ext import *

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция-обработчик
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Создание объекта Бот
application = Application.builder().token("здесь ваш токен").build()

# Регистрация обработчика на текстовые сообщения, но не команды
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Запуск бота
application.run_polling()
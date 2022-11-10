# https://zelenka.guru/threads/4494768/
# aiogram 2.23.1
# pip install aiogram
# pip install asyncio

#База для создания бота
import asyncio
from aiogram import Bot, Dispatcher, executor, types
#Кнопки
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot_token = '5181600578:AAEPU7j2TZENT1k7tWWBAyP8kIwWDWmowhM'
bot = Bot(bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, ' Привет! Поговорим?')


@dp.message_handler(content_types=['text'])
async def handle_text(message):
    if message.text == 'Привет!'or message.text == 'Привет':
        await bot.send_message(message.from_user.id, 'от старых штиблет')
    elif message.text == 'привет!' or message.text =='привет':
        await bot.send_message(message.from_user.id, 'сто лет в обед!')
    elif message.text == 'Здрасьте' or message.text =='здрасьте':
        await bot.send_message(message.from_user.id, 'забор покрасте!')
    elif message.text == 'Здрасьте!' or message.text =='здрасьте!':
        await bot.send_message(message.from_user.id, 'передай 100 баксов Насте!')
    elif message.text == 'Эй!' or message.text =='эй!' or message.text =='эй' or message.text =='Эй':
        await bot.send_message(message.from_user.id, 'бороду побрей!')
    elif message.text == 'Здорова!' or message.text =='здорова!' or message.text =='Здорова' or message.text =='здорова':
        await bot.send_message(message.from_user.id, ' у коровы, а у нас здрасте!')
    elif message.text == 'Здравствуйте!' or message.text =='здравствуйте!' or message.text =='Здравствуйте' or message.text =='здравствуйте':
        await bot.send_message(message.from_user.id, ' Здравствуйте')
    elif message.text == 'как тебя зовут?':
        await bot.send_message(message.from_user.id, 'робот я')
    elif message.text == 'и чо?' or message.text =='и че?' or message.text =='и что?' or message.text =='ну и что?':
        await bot.send_message(message.from_user.id, 'да ничо')
    elif message.text == 'все пока' or message.text =='давай пока' or message.text =='пока' or message.text =='до свиданья':
        await bot.send_message(message.from_user.id, 'да ничо')
    else:
        await bot.send_message(message.from_user.id, 'Извините, я Вас не понимаю')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
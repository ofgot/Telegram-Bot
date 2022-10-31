from config import *
from extensions import Converter, ApiException


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Enter the following details:\n<currency>' \
           '<what currency to transfer>' \
           '<amount of currency>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        iz, to, amount = message.text.split()
    except ValueError as e:
        bot.reply_to('wrong number of parameters')

    try:
        new_price = Converter.get_price(iz, to, amount)
        bot.reply_to(message, f'Price {amount} {iz} в {to} : {new_price}')
    except ApiException as e:
        bot.reply_to(message, f'Error in command \n{e}')


bot.polling(none_stop=True)

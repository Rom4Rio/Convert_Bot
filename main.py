import telebot
from config import *
from extensions import ConvertionException, CryptoConvertor
import traceback

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def begin(message: telebot.types.Message):
    text = 'Приветствую!\n Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
<в какую валюту хотите перевести> \
<количество переводимой валюты>\n Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise ConvertionException('Неверное количество параметров!')

        answer = CryptoConvertor.convert(*values)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)



bot.polling()
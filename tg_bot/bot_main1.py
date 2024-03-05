import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('C:/Users/kulis/PycharmProjects/first1/tg_bot/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('C:/Users/kulis/PycharmProjects/first1/tg_bot/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('6451949442:AAGStm4Ce1jRI3d0CoWJcgrXW3mwMv0C9ck')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        item3=types.KeyboardButton("Фото")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: \nФакт'
        ' для получения интересного факта\nПоговорка '
        '— для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            bot.send_message(message.chat.id, random.choice(facts))
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
            bot.send_message(message.chat.id, random.choice(thinks))
    elif message.text.strip() == 'Фото':
            bot.send_photo(message.chat.id, 'https://www.thevoicemag.ru/upload/img_cache/f0e/f0e1c3b4b532fbc70a73e022ffcf35f2_fitted_1332x0.jpg', caption= 'это важно')
    # Отсылаем юзеру сообщение в его чат
    # Запускаем бота
bot.polling(none_stop=True, interval=0)

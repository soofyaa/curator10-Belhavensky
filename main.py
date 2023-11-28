import telebot
from telebot import types

bot = telebot.TeleBot('6954006274:AAFEEVtTQQovx7_aSPA3qfec1p_G3A40dKw')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Товар')
    markup.add(btn1)
    btn2 = types.KeyboardButton('Скидки')
    btn3 = types.KeyboardButton('Наш сайт')
    btn4 = types.KeyboardButton('Наш инстаграмм')
    markup.add(btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Привет! \nЭто магазин одежы умсукл!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text  == 'Товар':
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Куртки')
        btn2 = types.KeyboardButton('Кроссовки')
        btn3 = types.KeyboardButton('Кепки')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        markup.add(btn4)

        bot.send_message(message.chat.id, 'Товар', reply_markup= markup)

    if message.text == 'Скидки':
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Cидки на куртки')
        btn2 = types.KeyboardButton('Скидки на кроссовки')
        btn3 = types.KeyboardButton('Скидки на кепки')
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, 'У нас проходит распродажа! \nКакой товар вас интересует ?',
                         reply_markup=markup)

    if message.text == ('Наш сайт'):
        site_url = "https://example.com"
        user_id = message.chat.id
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Открыть сайт", url=site_url))

        bot.send_message(user_id, f"Наш сайт: {site_url}", reply_markup=markup)

    if message.text == ('Наш инстаграмм'):
        site_url = "https://example.com"
        user_id = message.chat.id
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Открыть сайт", url=site_url))

        bot.send_message(user_id, f"Наш инстаграмм: {site_url}", reply_markup=markup)

    if message.text == ('Назад'):
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Товар')
        markup.add(btn1)
        btn2 = types.KeyboardButton('Скидки')
        btn3 = types.KeyboardButton('Наш сайт')
        btn4 = types.KeyboardButton('Наш инстаграмм')
        markup.add(btn2, btn3, btn4)

        bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


#@bot.message_handler(func=lambda message: 'Куртки' == message.text)
#    def bot_message(message):
#        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#        btn1 = types.KeyboardButton('Куртка 1')
#        btn2 = types.KeyboardButton('Куртка 2')
#        btn3 = types.KeyboardButton('Куртка 3')
 #       btn4 = types.KeyboardButton('Куртка 4')
#        markup.add(btn1, btn2, btn3)
#       markup.add(btn4)
#
 #       bot.send_message(message.chat.id, 'Куртки', reply_markup=markup)""

bot.polling(none_stop=True)
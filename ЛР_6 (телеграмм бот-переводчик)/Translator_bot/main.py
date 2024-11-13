import telebot
from googletrans import Translator
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('7015897860:AAGMy8s99Ps8O58NpgT2DddzcTMfvxHHc84')
translator = Translator()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_auto = KeyboardButton('Автоматический перевод')
button_ru_to_en = KeyboardButton('С русского на английский')
button_ru_to_es = KeyboardButton('С русского на испанский')
keyboard.add(button_auto, button_ru_to_en, button_ru_to_es)


user_mode = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    user_mode[user_id] = 'auto'
    bot.reply_to(message, "Привет! Я бот-переводчик. Выберите режим перевода:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def translate_message(message):
    user_id = message.chat.id
    text = message.text

    if text in ['Автоматический перевод', 'С русского на английский', 'С русского на испанский']:

        if text == 'Автоматический перевод':
            user_mode[user_id] = 'auto'
            bot.reply_to(message, "Режим перевода: Автоматический перевод")
        elif text == 'С русского на английский':
            user_mode[user_id] = 'ru_to_en'
            bot.reply_to(message, "Режим перевода: С русского на английский")
        elif text == 'С русского на испанский':
            user_mode[user_id] = 'ru_to_es'
            bot.reply_to(message, "Режим перевода: С русского на испанский")
        return

    try:
        if user_mode[user_id] == 'auto':
            detected = translator.detect(text)
            if detected.lang is None:
                bot.reply_to(message, "Не удалось определить язык ввода.")
                return
            detected_lang = detected.lang
            translated = translator.translate(text, dest='ru')
            bot.reply_to(message, f"Перевод: {translated.text}\n\nЯзык ввода: {detected_lang}")

        elif user_mode[user_id] == 'ru_to_en':
            translated = translator.translate(text, src='ru', dest='en')
            bot.reply_to(message, f"Перевод: {translated.text}")

        elif user_mode[user_id] == 'ru_to_es':
            translated = translator.translate(text, src='ru', dest='es')
            bot.reply_to(message, f"Перевод: {translated.text}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


bot.polling()
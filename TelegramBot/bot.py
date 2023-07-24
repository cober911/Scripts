import telebot;
from telebot import types

bot = telebot.TeleBot('5928076518:AAGfNT5aR393EKn9HUVStawFjm-QAYwxbMo')
print("Bot Enable")

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
@bot.callback_query_handler(func=lambda call: True)
def start(message):
    if message.text == '/start':
        # Для текстового сообщения '/start' выполнить определенные действия
        bot.send_message(message.chat.id, "Привет! Я бот. Как я могу помочь вам?")
    elif message.text == '/reg':
        # Для текстового сообщения '/reg' выполнить другие действия
        bot.send_message(message.chat.id, "Регистрация начата.")
    else:
        # Обработать другие текстовые сообщения (если нужно)
        bot.send_message(message.chat.id, "Неизвестная команда или текст.")

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Твоя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Годков сколько?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
        keyboard.add(key_yes); #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def callback_worker(call):
    # Получение данных, связанных с нажатой кнопкой
    button_data = call.data
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
         #.... код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        # ... переспрашиваем
        bot.send_message(call.message.chat.id, 'Не запомню : )')        

bot.polling(none_stop=True, interval=0)

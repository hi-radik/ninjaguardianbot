import telebot
import config
from telebot import types
import sqlite3
room = 0

bot = telebot.TeleBot(config.TOKEN)
list_module = list()

@bot.message_handler(commands=['start'])
def welcome(message):
    global room
    room = 0
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить модуль курса")
    item2 = types.KeyboardButton("Добавить вопросы к курсу")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Привет админ 😉, {0.first_name}!\nЯ - <b>{1.first_name}</b> - бот для создания🛠 контента 😎😎😎\nС моей помощью ты очень просто сможешь добавлять новые тесты и целые модули для своего курса!\nВыберете действие👇".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

#-------------------------------------------------     КОНЕЦ ВСТУПЛЕНИЯ       --------------------------------------------------------

@bot.message_handler(content_types=['text'])
def modul(message):
    global room
    global list_module
    print("Админ в комнате", room)
    if message.chat.type == 'private':

#----------------------------------------      КОМНАТА С ДОБАВЛЕНИЕМ МОДУЛЕЙ       --------------------------------------------------------

        if message.text == 'Добавить модуль курса' and room == 0: #-------- НУЛЕВАЯ КОМНАТА
            room = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Вернуться в главное меню ↩")
            markup.add(item1)
            bot.send_message(message.chat.id, "Введи название нового модуля теории или выбери из уже существующих", reply_markup=markup)

        elif room == 1:
            if message.text == 'Вернуться в главное меню ↩': #-------- ПЕРВАЯ КОМНАТА
                room = 0
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Добавить модуль курса")
                item2 = types.KeyboardButton("Добавить вопросы к курсу")
                markup.add(item1, item2)
                bot.send_message(message.chat.id, "Принял, Вернуться в главное меню ↩", reply_markup=markup)

            else:  #-------- ПЕРВАЯ КОМНАТА
                room = 2
                bot.send_message(message.chat.id, "Принял")

        if room == 2:  # -------- ВТОРАЯ КОМНАТА
            list_module.clear()
            list_module.append(message.text)
            print(list_module)
            room = 3
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Отменить название модуля ❌")
            markup.add(item1)
            bot.send_message(message.chat.id, f"Название нового модуля: {list_module[0]}, теперь введите содержание модуля", reply_markup=markup)

        elif room == 3:# -------- ВТОРАЯ КОМНАТА
            if message.text == 'Отменить название модуля ❌':  # -------- ПЕРВАЯ КОМНАТА
                room = 2
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Вернуться в главное меню ↩")
                markup.add(item1)
                bot.send_message(message.chat.id, "Принял, отменяю название модуля", reply_markup=markup)
                bot.send_message(message.chat.id, "Введи название новго модуля теории или выбери из уже существующих", reply_markup=markup)
            else:  #-------- ПЕРВАЯ КОМНАТА
                room = 4
                list_module.append(message.text)
                print(list_module)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Отменить содержание модуля ❌")
                item2 = types.KeyboardButton("Сохранить")
                markup.add(item1, item2)
                bot.send_message(message.chat.id, "Принял",  reply_markup=markup)
                bot.send_message(message.chat.id, "Смотри что у тебя получилось👌\nЕсли что-то пошло не так, ты всегда можешь сделать шаг назад...")
                bot.send_message(message.chat.id, f"Название модуля: {list_module[0]}")
                bot.send_message(message.chat.id, f"Содержание:\n {list_module[1]}")
                bot.send_message(message.chat.id, "Чтобы сохранить 💾, вернитесь в главное меню")

        elif room == 4:
            if message.text == 'Отменить содержание модуля ❌':  # -------- ПЕРВАЯ КОМНАТА
                room = 3
                del list_module[1]
                print(list_module)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Вернуться в главное меню ↩")
                markup.add(item1)
                bot.send_message(message.chat.id, "Принял, отменяю содержание модуля", reply_markup=markup)
                bot.send_message(message.chat.id, "Введите СОДЕРЖАНИЕ", reply_markup=markup)
            elif message.text != 'Вернуться в главное меню ↩':  #-------- ПЕРВАЯ КОМНАТА
                room = 4

        if room == 4:  # -------- ПЕРВАЯ КОМНАТА
            if message.text == 'Вернуться в главное меню ↩':
                room = 0
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Добавить модуль курса")
                item2 = types.KeyboardButton("Добавить вопросы к курсу")
                markup.add(item1, item2)
                bot.send_message(message.chat.id, "Принял, возращаюсь в главное меню🎉🎉🎉", reply_markup=markup)
            elif message.text == 'Ошибка‼':
                room = 4
            if  message.text == 'Сохранить':
                room = 0
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Добавить модуль курса")
                item2 = types.KeyboardButton("Добавить вопросы к курсу")
                markup.add(item1, item2)
                bot.send_message(message.chat.id, "Принял, возращаюсь в главное меню🎉🎉🎉", reply_markup=markup)
                con = sqlite3.connect('botdatabase.db')
                def sql_insert(con, entities):
                    cursorObj = con.cursor()
                    cursorObj.execute('INSERT INTO modules(id, name_module, content) VALUES(?, ?, ?)', entities)
                    con.commit()

                entities = (1, f'{list_module[0]}', f'{list_module[1]}')


                sql_insert(con, entities)






# RUN
bot.polling(none_stop=True)

# from re import A, S
from re import T
import sqlite3
# from sqlite3.dbapi2 import connect

import telebot
from telebot import types
import time
from config import info

print('yes')

token = info['token']
bot = telebot.TeleBot(f'{token}')
# test1ngasap

user_id = ''
name = ''
surname = ''
sex = ''
age = 0
position = ''
isAdmin = 0
swap = ''
answer1 = 0
answer2 = 0
answer3 = 0
answer4 = 0
answer5 = 0
num_answer1 = 0
num_answer2 = 0
num_answer3 = 0
num_answer4 = 0
num_answer5 = 0
begin_counter = 0
wrong_answ1 = False
wrong_answ2 = False
wrong_answ3 = False
wrong_answ4 = False
wrong_answ5 = False
course_fishing_answer = 0
course_fish = 0
course_paroli_answer = 0
course_paroli = 0
course_peredacha_answer = 0
course_peredacha = 0
course_phys_answer = 0
course_phys = 0
course_counter = 0
final_test_1c_count = 0
final_test_1c_1q_answer = 0
final_test_1c_2q_answer = 0
final_test_1c_3q_answer = 0
final_test_1c_1q_num = 0
final_test_1c_2q_num = 0
final_test_1c_3q_num = 0
final_test_2c_count = 0
final_test_2c_1q_answer = 0
final_test_2c_2q_answer = 0
final_test_2c_3q_answer = 0
final_test_2c_1q_num = 0
final_test_2c_2q_num = 0
final_test_2c_3q_num = 0
final_test_3c_count = 0
final_test_3c_1q_answer = 0
final_test_3c_2q_answer = 0
final_test_3c_3q_answer = 0
final_test_3c_1q_num = 0
final_test_3c_2q_num = 0
final_test_3c_3q_num = 0
final_test_4c_count = 0
final_test_4c_1q_answer = 0
final_test_4c_2q_answer = 0
final_test_4c_3q_answer = 0
final_test_4c_1q_num = 0
final_test_4c_2q_num = 0
final_test_4c_3q_num = 0
choice = 0
final_test_count = 0

conn = sqlite3.connect('db1.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, name: str, surname: str, sex: str, age: int, position: str):
    cursor.execute('INSERT OR REPLACE INTO test (user_id, name, surname, sex, age, position) VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, name, surname, sex, age, position))
    conn.commit()


def db_answers(user_id: int, answer1: str, answer2: str, answer3: str, answer4: str, answer5: str, begin_counter: int):
    cursor.execute('INSERT OR REPLACE INTO answers (user_id, answer1, answer2, answer3, answer4, answer5, begin_counter) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (user_id, answer1, answer2, answer3, answer4, answer5, begin_counter))
    conn.commit()


def db_course_answers(user_id: int, c_answer1: int, c_answer2: int, c_answer3: int, c_answer4: int, course_counter: int):
    cursor.execute('INSERT OR REPLACE INTO course_answers (user_id, c_answer1, c_answer2, c_answer3, c_answer4, course_counter) VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, c_answer1, c_answer2, c_answer3, c_answer4, course_counter))
    conn.commit()


def db_final_answers(user_id: int, final_fishing: int, final_paroli: int, final_peredacha: int, final_phys: int, final_count: int):
    cursor.execute('INSERT OR REPLACE INTO final_answers (user_id, final_fishing, final_paroli, final_peredacha, final_phys, final_count) VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, final_fishing, final_paroli, final_peredacha, final_phys, final_count))
    conn.commit()


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        file = open(
            "D:/PROG/try1/filez/readyLogoWithTextAndLampslogo2.png", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id, '''Привет! Я - Ninja Guardian Bot,
занимаюсь вопросом Вашей осведомленности в области информационной безопасности.
Пройдем небольшой тест, чтобы определить ваш уровень знаний :3''')

        time.sleep(1)
        bot.send_message(
            message.from_user.id, 'Но для начала, давайте Вас зарегистрируем. Для этого напишите /reg')
    elif message.text == '/results':
        try:
            user_id = message.from_user.id
            begin_res = cursor.execute(
                'SELECT begin_counter FROM answers WHERE user_id=user_id').fetchone()
            for res1 in begin_res:
                print(res1)
                bot.send_message(
                    message.from_user.id, f'В начальном тесте Вы набрали баллов в колличестве {res1} единиц')
            course_res = cursor.execute(
                'SELECT course_counter FROM course_answers WHERE user_id=user_id').fetchone()
            for res2 in course_res:
                print(res2)
                bot.send_message(
                    message.from_user.id, f'В тесте, который был во время курса Вы набрали баллов в колличестве {res2} единиц')
            final_res = cursor.execute(
                'SELECT final_count FROM final_answers WHERE user_id=user_id').fetchone()
            for res3 in final_res:
                print(res3)
                bot.send_message(
                    message.from_user.id, f'В итоговом тестировании Вы набрали баллов в колличестве {res3} единиц')
        except Exception as e:
            bot.reply_to(
                message, 'Что-то не так, поскольку не все тестирования высветились. Возможно, вы не проходили все тестирования')
        # try:
        #     begin_res = cursor.execute(
        #         'SELECT begin_counter FROM answers WHERE user_id=message.from_user.id').fetchone()
        #     print(begin_res)

        # except Exception as e:
        #     bot.reply_to(message, 'oooops')

    elif message.text == '/reg':
        people_id = message.chat.id
        cursor.execute(f'SELECT user_id FROM test WHERE user_id = {people_id}')
        data = cursor.fetchone()
        if data is None:

            # info = cursor.execute('SELECT * FROM test WHERE user_id=?', (user_id, ))
            # if info.fetchone() is None:

            bot.send_message(message.from_user.id, """\
Введите Ваше Имя
""")
            bot.register_next_step_handler(message, get_name)
            # Делаем когда нету человека в бд
        else:
            bot.send_message(
                message.from_user.id, 'Вы уже есть в базе данных, ознакомтесь с курсом по кибербезопасности - /course ')
            # Делаем когда есть человек в бд
        # global user_id

        # user_id = message.from_user.id

    # elif message.text == 'db':
        # bot.send_message(message.from_user.id, 'added to database')

        # us_id = message.from_user.id
        # us_name = message.from_user.first_name
        # us_sname = message.from_user.last_name
        # username = message.from_user.username
        # db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    elif message.text == '/finaltest':
        bot.send_message(
            message.chat.id, 'Данный тест поможет как и Вам, так и Вашему начальнику оценить ваши знания и навыки по кибербезопасности, определить насколько вы компетентны в данном вопросе')
        time.sleep(4)
        bot.send_message(
            message.chat.id, 'Читайте вопросы внимательно, вас торопить никто не будет')
        time.sleep(3)
        try:
            markup = types.ReplyKeyboardMarkup(
                row_width=1, resize_keyboard=True, one_time_keyboard=True)
            markup.add('Я все это начал ради него, так что да')
            msg = bot.reply_to(
                message, 'Вы готовы к итоговому тестированию?', reply_markup=markup)

            bot.register_next_step_handler(msg, final_test_p1)

        except Exception as e:
            bot.reply_to(message, 'oooops')

    elif message.text == '/help':
        bot.send_message(
            message.chat.id, '''Список команд, которые вам могут пригодиться:
        /reg - Зарегистрировать свой аккаунт
        /start - Воспроизвести вступление
        /course - Открыть курс
        /test - Пройти вступительный тест
        /finaltest - Пройти заключительный тест
        /results - узнать результаты по тестам''')
    elif message.text == '/course':
        file = open("D:/PROG/try1/filez/course/first.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(
            message.from_user.id, 'Как я уже упоминал - этот курс предназначен для повышения Вашей квалификации по кибербезопасности')
        time.sleep(2)
        try:
            markup = types.ReplyKeyboardMarkup(
                row_width=1, resize_keyboard=True, one_time_keyboard=True)
            markup.add('Продолжить')
            msg = bot.reply_to(
                message, 'Давайте уже наконец приступим!', reply_markup=markup)

            bot.register_next_step_handler(msg, course_intro)

        except Exception as e:
            bot.reply_to(message, 'oooops')

    elif message.text == '/test':
        bot.send_message(message.from_user.id, f'Отлично, приступим к тесту!')
        file = open("D:/PROG/try1/filez/slide2.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)

        time.sleep(2)

        bot.send_message(
            message.from_user.id, 'Сейчас мы находимся на первом уровне, тест состоит из пяти вопросов')
        file = open("D:/PROG/try1/filez/slide3.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(1)

        try:
            markup = types.ReplyKeyboardMarkup(
                row_width=1, resize_keyboard=True, one_time_keyboard=True)
            markup.add('Продолжить')
            msg = bot.reply_to(
                message, 'Я буду задавать Вам вопросы последовательно, можете не торопиться. Однако, постарайтесь отвечать искренне - это очень важно!', reply_markup=markup)

            bot.register_next_step_handler(msg, benginner_test_p1)

        except Exception as e:
            bot.reply_to(message, 'oooops')
        # bot.register_next_step_handler(message, benginner_test_p1)

    else:
        bot.send_message(
            message.from_user.id, 'К сожалению, я Вас не понимаю, попробуйте написать /help')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id,
                     f'Приятно познакомиться, {name}! А теперь введите вашу фамилию')
    bot.register_next_step_handler(message, get_surname)
    print(name)


def get_surname(message):
    global surname
    surname = message.text
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Муж', 'Жен')
        msg = bot.reply_to(message, 'Какой у вас пол?', reply_markup=markup)
        bot.register_next_step_handler(msg, get_sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')
    # markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    # markup.add('Муж', 'Жен')
    # message = bot.reply_to(message, 'Какой у вас пол?', reply_markup=markup)
    # bot.register_next_step_handler(message, get_sex)
    # keyboard1 = types.InlineKeyboardMarkup()
    # key_male = types.InlineKeyboardButton(text='male', callback_data='male')
    # keyboard1.add(key_male)
    # key_female = types.InlineKeyboardButton(text='female', callback_data='female')
    # keyboard1.add(key_female)
    # question1 = f'are you male or female?'
    # bot.send_message(message.from_user.id, text=question1, reply_markup=keyboard1)
    # bot.send_message(message.from_user.id, 'sex?')
    # bot.register_next_step_handler(message, get_sex)
    # print(surname)
    # global swap
    # swap = message


def get_sex(message):
    global sex
    sex = message.text

    bot.send_message(message.from_user.id, 'Сколько вам лет?')
    bot.register_next_step_handler(message, get_age)
    print(sex)


def get_age(message):
    global age
    age = message.text
    try:
        if not age.isdigit():
            msg = bot.reply_to(message, 'Возраст это число. Сколько вам лет?')
            bot.register_next_step_handler(msg, get_age)
            return
        markup = types.ReplyKeyboardMarkup(
            row_width=4, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Пользователь', 'Администратор', 'Менеджер', 'Гость')
        bot.reply_to(message, 'Какая у вас позиция в компании?',
                     reply_markup=markup)
        # bot.register_next_step_handler(msg, get_sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')
    bot.register_next_step_handler(message, get_position)
    print(age)


def get_position(message):
    global position
    position = message.text
    print(position)
    if position == 'Администратор':
        # FIXME:
        bot.send_message(message.from_user.id,
                         'Хм, а это точно Вы, о великий Администратор?')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Отменить', callback_data='no')
    keyboard.add(key_no)
    question = f'Вас зовут {name}, Ваша фамилия - {surname}, Ваш возраст - {age}, а позиция в компании - {position}?'
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard)

# Вас зовут {name}, Ваша фамилия - {surname}, Ваш возраст - {age}, а позиция в компании - {}?


def benginner_test_p1(message):
    bot.send_message(message.from_user.id, 'Загружаю тестирование...')
    time.sleep(2)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=4, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Не меняю', 'Каждые 30 дней',
                   'Каждые 90 дней', 'Каждый год')
        file = open("D:/PROG/try1/filez/slide4.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.reply_to(
            message, 'Пароли - ключи к нашей личной, а также служебной информации. У меня, например, для всех почтовых аккаунтов разные пароли!', reply_markup=markup)

        # answer1 = msg.text

        bot.register_next_step_handler(msg, beginner_test_p2)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def beginner_test_p2(message):
    global wrong_answ1
    global num_answer1
    global answer1
    answer1 = message.text
    num_answer1 = 0
    if answer1 == 'Пущу за ПК, пусть работает':
        print(num_answer1, '---- num_answer1')
        wrong_answ1 = True
        print('wrong answ 1 --- ', wrong_answ1)
    else:
        num_answer1 = 0
        print(num_answer1, '---- num_answer1')

    file = open("D:/PROG/try1/filez/slide5.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)

    bot.send_message(message.from_user.id,
                     'Поздравляю, Вы перешли на уровень вперед. Было не так уж и сложно, не правда ли? :)')
    time.sleep(2)
    bot.send_message(message.from_user.id, 'Приготовьтесь ко второму вопросу!')
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Подгружаю тестирование...')
    time.sleep(2)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Почему бы и нет?', 'Нецелесообразно')
        file = open("D:/PROG/try1/filez/slide7.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.reply_to(message, 'Вопрос номер 2', reply_markup=markup)

        bot.register_next_step_handler(msg, beginner_test_p3)

    except Exception as e:
        bot.reply_to(message, 'oooops')

    print(answer1, '---- answer1')


def beginner_test_p3(message):
    global answer2
    global num_answer2
    global wrong_answ2
    answer2 = message.text
    num_answer2 = 0
    if answer2 == 'Почему бы и нет?':
        wrong_answ2 = True
        print(num_answer2, '-- num_answer2')
        print(wrong_answ2, '--- wrong_answer2')
        file = open("D:/PROG/try1/filez/slide19.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Ай! Кажется, Вы выбрали не совсем хороший вариант!')
        time.sleep(2)
        bot.send_message(
            message.from_user.id, 'Видите ли, это может привести к утечке информации или чему-нибудь похуже :(')
        time.sleep(3)
        file = open("D:/PROG/try1/filez/slide8.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(
            message.from_user.id, 'Но не волнуйтесь, мы вам предоставим пройти этот тест до конца! Вы же начали его проходить ради этого, не так ли?')
        time.sleep(2)
    else:
        num_answer2 += 1
        print(num_answer2, '--- num_answer2')
        file = open("D:/PROG/try1/filez/slide8.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Отлично! Еще один вопрос позади, едем далее :)')
        time.sleep(1)

    bot.send_message(message.from_user.id, 'Подгружаю тестирование...')
    time.sleep(1)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Ну, раз руководитель требует...',
                   'По ссылке не перейду, отправлю жалобу на автора письма')
        file = open("D:/PROG/try1/filez/slide9.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.reply_to(message, 'Вопрос номер 3', reply_markup=markup)

        bot.register_next_step_handler(msg, beginner_test_p4)

    except Exception as e:
        bot.reply_to(message, 'oooops')

    print(answer2, ' ---- ans2')


def beginner_test_p4(message):
    global answer3
    global num_answer3
    global wrong_answ3
    answer3 = message.text
    num_answer3 = 0
    if answer3 == 'Ну, раз руководитель требует...':
        wrong_answ3 = True
        print(num_answer3, '--- num_answer3')
        print(wrong_answ3, '---wrng3')
        file = open("D:/PROG/try1/filez/slide20.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(
            message.from_user.id, 'А что, если там вирус!? Сейчас существует много людей, желающих получить информацию, помните об этом!')
        time.sleep(3)
        file = open("D:/PROG/try1/filez/slide10.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Это еще не конец! Нужно дойти до конца')
        time.sleep(1)

    else:
        num_answer3 += 1
        print(num_answer3, '---num_answer3')
        file = open("D:/PROG/try1/filez/slide10.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Прекрасный ответ! Я в Вас не сомневался :)')
        time.sleep(1)

    bot.send_message(message.from_user.id, 'Подгружаю тестирование...')
    time.sleep(2)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Почему бы и да, все так делают',
                   'Нет, воспользуюсь другим, более безопасным способом передачи данных')
        file = open("D:/PROG/try1/filez/slide12.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.reply_to(message, 'Вопрос номер 4', reply_markup=markup)

        bot.register_next_step_handler(msg, beginner_test_p5)

    except Exception as e:
        bot.reply_to(message, 'oooops')

    print(answer3, '--asn3')


def beginner_test_p5(message):
    global answer4
    global num_answer4
    global wrong_answ4
    answer4 = message.text
    num_answer4 = 0
    if answer4 == 'Почему бы и да, все так делают':
        wrong_answ4 = True
        print(num_answer4, '---num_answer4')
        print(wrong_answ4, '-wrng asn4')
        file = open("D:/PROG/try1/filez/slide22.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(
            message.from_user.id, 'К сожалению, такое поведение может привести к утечке информации, не стоит так делать.')
        time.sleep(3)

        file = open("D:/PROG/try1/filez/slide16.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Остался последний вопрос, поднажмите!')
        time.sleep(2)

    else:
        num_answer4 += 1
        print(num_answer4, '---num_answer4')
        file = open("D:/PROG/try1/filez/slide16.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Отличная работа! Остался последний вопрос!')
        time.sleep(2)

    bot.send_message(message.from_user.id, 'Подгружаю тестирование...')
    time.sleep(1)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Да, это просто флешка', 'Нет, небезопасно')
        file = open("D:/PROG/try1/filez/slide15.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.reply_to(message, 'Вопрос номер 5', reply_markup=markup)

        bot.register_next_step_handler(msg, beginner_test_p6)

    except Exception as e:
        bot.reply_to(message, 'oooops')

    print(answer4, '-ans4')


def beginner_test_p6(message):
    global answer5
    global num_answer5
    global wrong_answ5
    answer5 = message.text
    num_answer5 = 0
    if answer5 == 'Да, это просто флешка':
        wrong_answ5 = True
        print(num_answer5, '---- num_answer5')
        print(wrong_answ5, '--- wrng ans 5')
        file = open("D:/PROG/try1/filez/slide23.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         'Это не так! На флешке может быть вредоносное ПО!')
        time.sleep(4)
        file = open("D:/PROG/try1/filez/slide16.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(
            message.from_user.id, 'В любом случае наш тест подошел к концу, с чем Вас и поздравляем!')
        time.sleep(3)
        bot.send_message(
            message.from_user.id, 'Хорошо Вы прошли этот тест, или нет - нам скоро предстоит узнать')
        time.sleep(3)

    else:
        num_answer5 += 1
        print(num_answer5, '---num_answer5')
        file = open("D:/PROG/try1/filez/slide18.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)

        bot.send_message(message.from_user.id, 'Вы прошли тестирование!')
        time.sleep(3)
        bot.send_message(
            message.from_user.id, 'Хорошо Вы прошли этот тест, или нет - нам скоро предстоит узнать')
        time.sleep(3)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Узнать результаты!')
        msg = bot.reply_to(
            message, 'Осталось только проанализировать ваши ответы...', reply_markup=markup)
        bot.register_next_step_handler(msg, count_begin_answers)
        time.sleep(3)

    except Exception as e:
        bot.reply_to(message, 'oooops')

    print(answer5, ' ans5')


def count_begin_answers(message):
    print('counting beginning results')
    begin_counter = 0
    begin_counter = num_answer1 + num_answer2 + \
        num_answer3 + num_answer4 + num_answer5
    print(begin_counter, 'OTVET')
    bot.send_message(message.chat.id, 'Провожу обработку данных...')
    time.sleep(3)
    bot.send_message(
        message.chat.id, f'Вы набрали баллов в колличестве {begin_counter} единиц!')
    time.sleep(2)
    bot.send_message(
        message.chat.id, 'Это значит, что мы можем Вас наградить Вашим первым достижением!')
    if begin_counter == 1 or begin_counter == 0:
        file = open("D:/PROG/try1/filez/slide6.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)

        bot.send_message(
            message.from_user.id, 'Вы - маленький ниндзя - Вам предстоит многому научиться!')

    elif begin_counter == 2:
        file = open("D:/PROG/try1/filez/slide11.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)

        bot.send_message(
            message.from_user.id, 'Вы - ниндзя - вокруг Вас еще есть знания, которые Вы должны впитать в себя')

    elif begin_counter == 3:
        file = open("D:/PROG/try1/filez/slide14.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)

        bot.send_message(
            message.from_user.id, 'Вы - опытный ниндзя - Вы почти в совершенстве владете навыками по безопасности!')

    elif begin_counter == 4:
        file = open("D:/PROG/try1/filez/slide17.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)

        bot.send_message(
            message.from_user.id, 'Невероятно! Вы являетесь ниндзя-мастером. Давно я не наблюдал такого. Вы просто восхитительны!')

    time.sleep(3)
    bot.send_message(
        message.chat.id, 'Благодарю Вас за участие в данном тестировании!')
    bot.send_message(message.chat.id, 'Однако, это лишь начало нашего пути')
    time.sleep(4)
    bot.send_message(
        message.chat.id, 'Это тестирование было создано для того, чтобы выявить у вас "слабые места", от которых я помогу Вам избавиться')
    time.sleep(4)
    bot.send_message(
        message.chat.id, 'Для этого нужно пройти небольшой курс обучения, не бойтесь - будет достаточно весело и познавательно :)')
    time.sleep(2)
    bot.send_message(
        message.chat.id, 'Чтобы начать обучение - напишите /course')

    user_id = message.from_user.id

    db_answers(user_id=user_id, answer1=answer1, answer2=answer2,
               answer3=answer3, answer4=answer4, answer5=answer5, begin_counter=begin_counter)


def course_intro(message):
    file = open("D:/PROG/try1/filez/course/second.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.from_user.id,
                     'Данный курс состоит из четырех пунктов, о которых я Вам сейчас расскажу')
    time.sleep(6)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Начать')
        msg = bot.reply_to(
            message, 'Предлагаю начать прямо сейчас, что скажете?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_fishing1)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_fishing1(message):
    bot.send_message(message.from_user.id,
                     'И первая тема, это...')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/fishing/slide20.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Мне уже не терпится начать :)')
    time.sleep(1)
    bot.send_message(message.from_user.id,
                     'Поэтому, усаживайтесь поудобнее. Я приступаю к загрузке курса по фишингу...')
    time.sleep(5)
    file = open("D:/PROG/try1/filez/course/fishing/slide21.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(20)
    bot.send_message(message.from_user.id,
                     'Меня так бесят иногда эти злоумышленники, которые котиков кидают мне на почту - иногда так хочется нажать на ссылку с надписью "Открыть фото милых котиков"')
    time.sleep(8)
    bot.send_message(message.from_user.id,
                     'Однако, безопасность - превыше всего!')
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Что-то я заговорился. Подгружаю курс...')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/fishing/slide22.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Да, конечно')
        msg = bot.reply_to(
            message, 'Я Вас не слишком сильно гоню? Успеваете? Мы просто к очень важному подошли, хочу убедиться в том, что у Вас все в порядке', reply_markup=markup)

        bot.register_next_step_handler(msg, course_fishing2)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_fishing2(message):
    bot.send_message(message.from_user.id,
                     'Отлично! Тогда, продолжаю подгружать курс...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/fishing/slide23.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(15)
    bot.send_message(message.from_user.id,
                     'Эх, помню, мне рассказывал Levitas Guardian Bot об одной истории...')
    time.sleep(5)
    bot.send_message(message.from_user.id,
                     'Точно, я же ее могу рассказать Вам! Прочитайте, достаточно интересная:')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/fishing/slide24.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(30)
    bot.send_message(message.from_user.id,
                     'Да, и такое бывает. Именно поэтому важно быть бдительным и соблюдать правила безопасности!')
    time.sleep(3)
    bot.send_message(message.from_user.id,
                     'Кстати, вот мы и прошли тему фишинга. Быстро, не так ли?')
    time.sleep(2)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Валяй, на все отвечу')
        msg = bot.reply_to(
            message, 'Чтобы я смог убедиться в том, что Вы усвоили тему, я бы хотел задать у Вас один вопрос', reply_markup=markup)

        bot.register_next_step_handler(msg, course_fishing3)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_fishing3(message):
    time.sleep(1)
    file = open("D:/PROG/try1/filez/course/fishing/slide25.jpg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=4, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Открою, посмотрю содержимое, перейду по ссылочкам', 'Перешлю системному администратору, пусть тоже посмотрит',
                   'Посмотрю и сразу удалю', 'Сообщю специалисту компании по ИБ, либо удалю сообщение')
        msg = bot.reply_to(
            message, 'Сейчас и проверим!', reply_markup=markup)

        bot.register_next_step_handler(msg, course_fishing_count)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_fishing_count(message):
    global course_fishing_answer
    global course_fish
    course_fishing_answer = message.text
    if course_fishing_answer == 'Сообщю специалисту компании по ИБ, либо удалю сообщение':
        course_fish = 1
        print('fishing course passed!')
        bot.send_message(message.from_user.id,
                         'Вы прекрасно усвоили материал!')
        time.sleep(3)
    else:
        course_fish = 0
        print('fishing course failed')
        bot.send_message(message.from_user.id,
                         'Кажется, Вы были не достаточно внимательны')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Но ничего страшного! Я просто Вам напомню, что нужно делать, для повышения безопасности как своей, так и своих коллег')
        time.sleep(3)
        bot.send_message(message.from_user.id,
                         'Провожу откат курса по фишингу до 50%...')
        time.sleep(3)
        file = open("D:/PROG/try1/filez/course/fishing/slide23.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(15)
        bot.send_message(message.from_user.id,
                         'Надеюсь, Вы все запомнили :) ')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Ведь у меня есть некоторые новости для Вас....')
        time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Вы прошли 25% обучающего курса, а это прекрасные новости!')
    time.sleep(3)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Всегда готов!')
        msg = bot.reply_to(
            message, 'Ну что, готовы дальше грызть гранит науки?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_paroli1)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_paroli1(message):
    bot.send_message(message.from_user.id,
                     'Следущая тема - это...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/paroli/slide12.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Это одна из моих любымих тем, столько рассказать могу :)')
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Загружаю курс "Пароли_и_учетные_записи_v5.9" ...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/paroli/slide13.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    file = open("D:/PROG/try1/filez/course/paroli/slide14.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(15)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Что-то такое было')
        msg = bot.reply_to(
            message, 'Разве я не говорил, что использую разные пароли на всех почтах?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_paroli2)

    except Exception as e:
        bot.reply_to(message, 'oooops')
    time.sleep(1)


def course_paroli2(message):
    time.sleep(1)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Но это ты тут начинаешь отвлекать меня, а не я тебя')
        msg = bot.reply_to(
            message, 'Так, не отвлекаемся! Мы почти прошли половину курса!', reply_markup=markup)

        bot.register_next_step_handler(msg, course_paroli3)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_paroli3(message):
    bot.send_message(message.from_user.id, 'Кхехехе, подгружаю курс...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/paroli/slide15.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    bot.send_message(message.from_user.id,
                     'Вспомнилась мне тут конечно одна неприятная история...')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/paroli/slide16.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(15)
    bot.send_message(message.from_user.id,
                     'Вот именно поэтому у меня паролей много и они уникальны, так я еще их иногда меняю!')
    time.sleep(4)
    bot.send_message(message.from_user.id,
                     'Не хочу, чтобы кто-то проник в меня, жутко только лишь от таких мыслей становится...')
    time.sleep(4)
    bot.send_message(message.from_user.id,
                     'Кстати, время вопросов!')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/paroli/slide17.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=4, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Tr0ub4dor&32_13213hfkegm3HksGR_',
                   '88005553535andrey', 'correcthorsebatterystaple', 'admin1')
        msg = bot.reply_to(
            message, 'Ну, что думаешь?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_paroli_count)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_paroli_count(message):
    global course_paroli_answer
    global course_paroli
    course_paroli_answer = message.text
    if course_paroli_answer == 'Tr0ub4dor&32_13213hfkegm3HksGR_':
        course_paroli = 1
        print('paroli course passed!')
        bot.send_message(message.from_user.id,
                         'Прекрасная работа!')
        time.sleep(3)
    else:
        course_paroli = 0
        print('paroli course failed')
        bot.send_message(message.from_user.id,
                         'Это промах!')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'На всякий случай, совершу откат по курсу и напомню Вам, что такое безопасный пароль')
        time.sleep(3)
        bot.send_message(message.from_user.id,
                         'Провожу откат курса до 50%...')
        time.sleep(3)
        file = open("D:/PROG/try1/filez/course/paroli/slide15.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(10)
        bot.send_message(message.from_user.id,
                         'Провожу откат курса до 75%...')
        file = open("D:/PROG/try1/filez/course/paroli/slide15.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(15)
        bot.send_message(message.from_user.id,
                         'Думаю, все понятно :) ')
        time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Кстати, позади нас находится 50% курса, что не может не радовать!')
    time.sleep(3)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Заводи!')
        msg = bot.reply_to(
            message, 'Едем далее?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_peredacha1)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_peredacha1(message):
    bot.send_message(message.from_user.id,
                     'Активирую доступ к следующей части курса, которая называется...')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/peredacha/slide28.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(3)
    bot.send_message(message.from_user.id,
                     'Ох, помню один сотрудник вставил флешку, которую нашел на улице, в компьютер с моим старым другом, которого звали Friend Guardian Bot')
    time.sleep(7)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Все в порядке?', 'Скучаешь по нему?',
                   'Как ни крути, он просто бот. Кстати, запустишь курс?')
        msg = bot.reply_to(
            message, 'Давно не слыхал от него новостей...', reply_markup=markup)

        bot.register_next_step_handler(msg, course_peredacha2)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_peredacha2(message):
    time.sleep(3)
    bot.send_message(message.from_user.id, 'Да...')
    time.sleep(4)
    bot.send_message(message.from_user.id,
                     'Перезагрузка безопасной прошивки произошла успешно. Загружаю курс...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/peredacha/slide29.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    file = open("D:/PROG/try1/filez/course/peredacha/slide30.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    bot.send_message(message.from_user.id,
                     'Сотрудники всегда должны быть бдительными, не забывай это!')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/peredacha/slide31.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(5)
    bot.send_message(message.from_user.id,
                     'Возможно, ты знаешь такой бренд одежды, как H&M. У меня там есть один информатор - Clothes Guardian Bot. Он мне одну историю рассказал...')
    time.sleep(7)
    file = open("D:/PROG/try1/filez/course/peredacha/slide32.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(20)
    bot.send_message(message.from_user.id,
                     'Забавный факт - мы успели пройти почти 75% курса за столь короткий промежуток времени. Я считаю - это успех')
    time.sleep(5)
    try:
        file = open("D:/PROG/try1/filez/course/peredacha/slide33.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Перешлю без вопросов - это же сотрудник компании',
                   'Скажу, что передам данные только по защищенному каналу связи')
        msg = bot.reply_to(
            message, 'А теперь, по классике, закрепляем', reply_markup=markup)

        bot.register_next_step_handler(msg, course_peredacha_count)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_peredacha_count(message):
    global course_peredacha_answer
    global course_peredacha
    course_peredacha_answer = message.text
    if course_peredacha_answer == 'Скажу, что передам данные только по защищенному каналу связи':
        course_peredacha = 1
        print('peredacha course passed!')
        bot.send_message(message.from_user.id,
                         'Да Вы схватываете все на лету!')
        time.sleep(3)
    else:
        course_peredacha = 0
        print('peredacha course failed')
        bot.send_message(message.from_user.id,
                         'Это неверный ответ!')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Взгляните еще раз на рекомендации к этой части курса:')
        time.sleep(3)
        bot.send_message(message.from_user.id,
                         'Провожу откат курса до 50%...')
        time.sleep(3)
        file = open("D:/PROG/try1/filez/course/peredacha/slide30.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(10)
        bot.send_message(message.from_user.id,
                         'Провожу откат курса до 75%...')
        file = open("D:/PROG/try1/filez/course/peredacha/slide31.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(5)
        bot.send_message(message.from_user.id,
                         'Надеюсь, усвоили :) ')
        time.sleep(2)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Запускай')
        msg = bot.reply_to(
            message, 'У нас осталась последняя остановка, и мы успешно завершим курс. Готовы?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_phys1)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_phys1(message):
    bot.send_message(message.from_user.id,
                     'Итак, мы добрались до последней части курса, надеюсь, Вы не сильно утомились :)')
    time.sleep(3)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Несомненно!')
        msg = bot.reply_to(
            message, 'Не утомились же? Есть еще порох в пороховницах?', reply_markup=markup)

        bot.register_next_step_handler(msg, course_phys2)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_phys2(message):
    bot.send_message(message.from_user.id,
                     'Загружаю заключительную часть курса...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/phys/slide3.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/phys/slide4.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(8)
    bot.send_message(message.from_user.id,
                     'Такие обычно в очках пытаются зайти :)')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/course/phys/slide5.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(8)
    bot.send_message(message.from_user.id,
                     'Даже, если попросили выйти на секунду! Никогда не знаешь, что может произойти...')
    time.sleep(4)
    file = open("D:/PROG/try1/filez/course/phys/slide6.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    file = open("D:/PROG/try1/filez/course/phys/slide7.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(10)
    bot.send_message(message.from_user.id,
                     'Как Вы могли заметить, все части курса переплетены друг с другом. Именно поэтому нужо запомнить все, что я говорил сегодня')
    time.sleep(6)
    bot.send_message(message.from_user.id,
                     'Недавно в соседней компании случилось происшествие, стоит ознакомиться...')
    time.sleep(4)
    file = open("D:/PROG/try1/filez/course/phys/slide8.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(15)
    bot.send_message(message.from_user.id,
                     'Осталось удостовериться, что вы все усвоили')
    time.sleep(3)
    try:
        file = open("D:/PROG/try1/filez/course/phys/slide9.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Посмотрю, что на флешке, когдай дойду до рабочего компьютера',
                   'Сообщу ответственному за ИБ о флешке', 'Проверю флешку дома')
        msg = bot.reply_to(
            message, 'Вопрос перед Вами', reply_markup=markup)

        bot.register_next_step_handler(msg, course_phys_count)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_phys_count(message):
    global course_phys_answer
    global course_phys
    print(message.text)
    course_phys_answer = message.text
    if course_phys_answer == 'Сообщу ответственному за ИБ о флешке':
        course_phys = 1
        print('otvet =', course_phys_answer)
        print('phys course passed!')
        bot.send_message(message.from_user.id,
                         'Вы правильно ответили на данный вопрос!')
        time.sleep(3)
    elif course_phys_answer != 'Сообщу ответственному за ИБ о флешке':
        print(f'{course_phys_answer} ne ravno Сообщу ответственному за ИБ о флешке')
        course_phys = 0
        print('phys course failed')
        bot.send_message(message.from_user.id,
                         'Ну нет, это совсем не то!')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Без паники, вы просто переутомились, сейчас я Вам все напомню...')
        time.sleep(3)
        bot.send_message(message.from_user.id,
                         'Провожу откат курса до 75%...')
        time.sleep(3)
        file = open("D:/PROG/try1/filez/course/phys/slide7.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        time.sleep(10)
        bot.send_message(message.from_user.id,
                         'Тут, на самом деле, ничего сложного. Смотрите, чтобы любобытство не взяло над вами верх :) ')
        time.sleep(2)
    bot.send_message(message.from_user.id, 'У меня для Вас хорошие новости...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/end.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.from_user.id,
                     'Вы прошли наш курс!!! Вы просто потрясающий человек!')
    time.sleep(3)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('А ну, обработай')
        msg = bot.reply_to(
            message, 'Осталось подсчитать Ваши результат и сделать выводы', reply_markup=markup)

        bot.register_next_step_handler(msg, course_count)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def course_count(message):
    print('counting course results')
    course_counter = 0
    course_counter = course_fish + course_paroli + \
        course_peredacha + course_phys
    print(course_counter, 'ammount of points')
    bot.send_message(message.chat.id, 'Провожу обработку данных...')
    time.sleep(2)
    bot.send_message(
        message.chat.id, f'Вы набрали баллов в колличестве {course_counter} единиц!')
    time.sleep(1)
    bot.send_message(
        message.chat.id, 'Вы, несомненно, прошли долгий путь, но на то он и путь ниндзя, чтобы быть тернистым.')
    time.sleep(3)
    bot.send_message(message.chat.id,
                     'Теперь, когда Вы прошли курс, вы сможете спокойно принять участи в нашем итоговом тесте, по результатам которого вы будете оценены либо как ответственный сотрудник, который ознакомлен с правилами кибербезопасности, либо как сотрудник, которому нужно восполнить пробелы в знаниях по основным правилам безопасности')

    user_id = message.from_user.id

    db_course_answers(user_id=user_id, c_answer1=course_fish, c_answer2=course_paroli,
                      c_answer3=course_peredacha, c_answer4=course_phys, course_counter=course_counter)

    print('success!')

    time.sleep(6)
    bot.send_message(
        message.chat.id, 'Для того, чтобы пройти тест, напишите /finaltest')


def final_test_p1(message):
    time.sleep(2)
    bot.send_message(
        message.chat.id, 'Загружаю первые вопросы...')
    time.sleep(4)
    bot.send_message(
        message.chat.id, 'Открываю первую тему, под названием')
    time.sleep(1)
    file = open("D:/PROG/try1/filez/course/fishing/slide20.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(3)
    file = open("D:/PROG/try1/filez/tests/fishing_test/slide26.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Посмотрю без вопросов - это же сотрудник компании компании',
                   'Спрошу у отправителя лично, он ли отправил сообщение?', 'Отправлю ответ вежливым отказом')
        msg = bot.reply_to(
            message, '1 вопрос по теме фишинг', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p2)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p2(message):

    global final_test_1c_1q_answer
    global final_test_1c_1q_num
    final_test_1c_1q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_1c_1q_answer == 'Посмотрю без вопросов - это же сотрудник компании компании':
        final_test_1c_1q_num = 0
    elif final_test_1c_1q_answer == 'Спрошу у отправителя лично, он ли отправил сообщение?':
        final_test_1c_1q_num = 1
    elif final_test_1c_1q_answer == 'Отправлю ответ вежливым отказом':
        final_test_1c_1q_num = 1
    print(final_test_1c_1q_num, '- points for 1st fishing answ')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/fishing_test/slide27.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Скажу об этом ответственному специалисту или удалю сообщение',
                   'Перейду по ссылке', 'Отправлю ответ с угрозой или оскорблением')
        msg = bot.reply_to(
            message, '2 вопрос во теме фишинг', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p3)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p3(message):
    user_id = message.from_user.id
    global final_test_1c_2q_answer
    global final_test_1c_2q_num
    global final_test_1c_count
    final_test_1c_count = 0
    final_test_1c_2q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_1c_2q_answer == 'Перейду по ссылке':
        final_test_1c_2q_num = 0
    elif final_test_1c_2q_answer == 'Скажу об этом ответственному специалисту или удалю сообщение':
        final_test_1c_2q_num = 1
    elif final_test_1c_2q_answer == 'Отправлю ответ с угрозой или оскорблением':
        final_test_1c_2q_num = 1
    print(final_test_1c_2q_num, '- points for 2nd fishing answ')
    print(final_test_1c_1q_num, final_test_1c_2q_num)
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Считаю, сколько вы набрали баллов...')
    time.sleep(1)
    final_test_1c_count = final_test_1c_1q_num + final_test_1c_2q_num
    print(final_test_1c_count, '-fishing test')
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Продолжить')
        msg = bot.reply_to(
            message, 'Первую тему мы прошли - впереди еще 3!', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p4)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p4(message):
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Загружаю следущую тему...')
    time.sleep(3)
    file = open("D:/PROG/try1/filez/course/paroli/slide12.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/paroli_test/slide18.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=4, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Тот же, что и везде', 'Сгенерирую уникальный пароль в специальной программе',
                   'Один из личных паролей с измененным окончанием', '12345')
        msg = bot.reply_to(
            message, 'Первый вопрос по теме "Пароли и учетные записи"', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p5)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p5(message):
    global final_test_2c_1q_answer
    global final_test_2c_1q_num
    final_test_2c_1q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_2c_1q_answer == 'Тот же, что и везде':
        final_test_2c_1q_num = 0
    elif final_test_2c_1q_answer == 'Сгенерирую уникальный пароль в специальной программе':
        final_test_2c_1q_num = 1
    elif final_test_2c_1q_answer == 'Один из личных паролей с измененным окончанием':
        final_test_2c_1q_num = 1
    elif final_test_2c_1q_answer == '12345':
        final_test_2c_1q_num = 0
    print(final_test_2c_1q_num, '- points for 1st pwd answ')
    print(final_test_2c_1q_num)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/paroli_test/slide19.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=4, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Пароль длиной более 13 символов', 'Включающий символы кириллицы',
                   'Включающий от Департамента департаментов ИБ', 'Любой пароль можно подобрать')
        msg = bot.reply_to(
            message, 'Второй вопрос второй темы', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p6)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p6(message):
    global final_test_2c_2q_answer
    global final_test_2c_2q_num
    global final_test_2c_count
    final_test_2c_count = 0
    final_test_2c_2q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_2c_2q_answer == 'Пароль длиной более 13 символов':
        final_test_2c_2q_num = 0
    elif final_test_2c_2q_answer == 'Включающий символы кириллицы':
        final_test_2c_2q_num = 0
    elif final_test_2c_2q_answer == 'Включающий от Департамента департаментов ИБ':
        final_test_2c_2q_num = 0
    elif final_test_2c_2q_answer == 'Любой пароль можно подобрать':
        final_test_2c_2q_num = 1
    print(final_test_2c_2q_num, '- points for 2nd pwd answ')
    print(final_test_2c_1q_num, final_test_2c_2q_num)
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Считаю, сколько вы набрали баллов...')
    time.sleep(1)
    final_test_2c_count = final_test_2c_1q_num + final_test_2c_2q_num
    print(final_test_2c_count, '-pwd test')
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Продолжить')
        msg = bot.reply_to(
            message, 'Вторую тему мы прошли - впереди еще 2!', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p7)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p7(message):
    time.sleep(2)
    bot.send_message(message.from_user.id, 'Открываю тему №3')
    file = open("D:/PROG/try1/filez/course/peredacha/slide28.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/peredacha_test/slide34.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Скажу ему, что данное действие нарушает требования ИБ компании',
                   'Перешлю, так как это сказал сделать начальник')
        msg = bot.reply_to(
            message, 'Сосредоточтесь, дышите глубоко...', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p8)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p8(message):
    global final_test_3c_1q_answer
    global final_test_3c_1q_num
    final_test_3c_1q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_3c_1q_answer == 'Перешлю, так как это сказал сделать начальник':
        final_test_3c_1q_num = 0
    elif final_test_3c_1q_answer == 'Скажу ему, что данное действие нарушает требования ИБ компании':
        final_test_3c_1q_num = 1
    print(final_test_3c_1q_num, '- points for 1st peredacha answ')
    print(final_test_3c_1q_num)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/peredacha_test/slide35.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Ему же, наверное, начальник сказал так сделать', 'Ничего страшного',
                   'Нельзя передавать служебную информацию по незащищенным каналам связи!')
        msg = bot.reply_to(
            message, 'Второй вопрос темы №3', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p9)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p9(message):
    global final_test_3c_2q_answer
    global final_test_3c_2q_num
    global final_test_3c_count
    final_test_3c_count = 0
    final_test_3c_2q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_3c_2q_answer == 'Ему же, наверное, начальник сказал так сделать':
        final_test_3c_2q_num = 0
    elif final_test_3c_2q_answer == 'Ничего страшного':
        final_test_3c_2q_num = 0
    elif final_test_3c_2q_answer == 'Нельзя передавать служебную информацию по незащищенным каналам связи!':
        final_test_3c_2q_num = 1
    print(final_test_3c_2q_num, '- points for 2nd peredacha answ')
    print(final_test_3c_1q_num, final_test_3c_2q_num)
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Считаю, сколько вы набрали баллов...')
    time.sleep(1)
    final_test_3c_count = final_test_3c_1q_num + final_test_3c_2q_num
    print(final_test_3c_count, '-peredacha test')
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Поднажмем!')
        msg = bot.reply_to(
            message, 'Осталось пройти последнюю тему!', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p10)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p10(message):
    time.sleep(2)
    bot.send_message(message.from_user.id, 'Открываю финальную часть теста...')
    file = open("D:/PROG/try1/filez/course/phys/slide3.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/phys_test/slide10.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)

    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Объясню сотруднику, что материальные документы нужно уничтожать в шредере',
                   'Не стану обращать внимание на такие мелочи')
        msg = bot.reply_to(
            message, 'Достаточно интересный вопрос. Как бы поступил порядочный сотрудник?', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p11)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p11(message):
    global final_test_4c_1q_answer
    global final_test_4c_1q_num
    final_test_4c_1q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_4c_1q_answer == 'Не стану обращать внимание на такие мелочи':
        final_test_4c_1q_num = 0
    elif final_test_4c_1q_answer == 'Объясню сотруднику, что материальные документы нужно уничтожать в шредере':
        final_test_4c_1q_num = 1
    print(final_test_4c_1q_num, '- points for 1st phys answ')
    print(final_test_4c_1q_num)
    time.sleep(2)
    file = open("D:/PROG/try1/filez/tests/phys_test/slide11.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Пущу за ПК, пусть работает', 'Запрошу его документы и пущу за ПК',
                   'Запрошу его документы, согласую со своим непосредственным руковводителем и пущу за ПК')
        msg = bot.reply_to(
            message, 'Финальный вопрос! Не торопитесь!', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p12)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p12(message):
    global final_test_4c_2q_answer
    global final_test_4c_2q_num
    global final_test_4c_count
    final_test_4c_count = 0
    final_test_4c_2q_answer = message.text
    time.sleep(1)
    bot.send_message(message.from_user.id, 'Обрабатываю...')
    time.sleep(2)
    if final_test_4c_2q_answer == 'Пущу за ПК, пусть работает':
        final_test_4c_2q_num = 0
    elif final_test_4c_2q_answer == 'Запрошу его документы и пущу за ПК':
        final_test_4c_2q_num = 0
    elif final_test_4c_2q_answer == 'Запрошу его документы, согласую со своим непосредственным руковводителем и пущу за ПК':
        final_test_4c_2q_num = 1
    print(final_test_4c_2q_num, '- points for 2nd phys answ')
    print(final_test_4c_1q_num, final_test_4c_2q_num)
    time.sleep(2)
    bot.send_message(message.from_user.id,
                     'Считаю, сколько вы набрали баллов...')
    time.sleep(1)
    final_test_4c_count = final_test_4c_1q_num + final_test_4c_2q_num
    print(final_test_4c_count, '-phys test')
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Продолжить???')
        msg = bot.reply_to(
            message, 'Кажется, что-то происходит...', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p13)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p13(message):
    time.sleep(1)
    bot.send_message(message.from_user.id,
                     '@@@@@ ВНИМАНИЕ, АКТИВИРОВАН ПРОТОКОЛ НОМЕР 59 @@@@@')
    time.sleep(2)
    bot.send_message(message.from_user.id, 'Что происходит?')
    time.sleep(1)
    file = open("D:/PROG/try1/filez/slide23.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(1)
    file = open("D:/PROG/try1/filez/slide22.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(1)
    file = open("D:/PROG/try1/filez/slide21.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(1)
    file = open("D:/PROG/try1/filez/slide20.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    time.sleep(1)
    file = open("D:/PROG/try1/filez/slide19.jpeg", 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.from_user.id,
                     'Нет времени на раздумие - меня пытаются взломать - скорее, нужно выбрать правильный код безопасности, чтобы спасти меня и прогресс!')
    time.sleep(3)
    try:
        markup = types.ReplyKeyboardMarkup(
            row_width=3, resize_keyboard=True, one_time_keyboard=True)
        markup.add('Jhfu24^$^&*@hhS3CURYty_COd3_59_59_59_59_59',
                   'password', '123456789')
        msg = bot.reply_to(
            message, 'К@к0й Kkk0д б3#о%аzNостИ пр@вил#н$й!?!?!?!?', reply_markup=markup)

        bot.register_next_step_handler(msg, final_test_p14)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def final_test_p14(message):
    global final_test_count
    user_id = message.from_user.id
    final_test_count = 0
    final_test_count = final_test_1c_count + final_test_2c_count + \
        final_test_3c_count + final_test_4c_count
    print(final_test_count)
    db_final_answers(user_id=user_id, final_fishing=final_test_1c_count, final_paroli=final_test_2c_count,
                     final_peredacha=final_test_3c_count, final_phys=final_test_4c_count, final_count=final_test_count)
    print('added to database successfully!')
    global choice
    choice = message.text
    if choice == 'Jhfu24^$^&*@hhS3CURYty_COd3_59_59_59_59_59':
        bot.send_message(message.from_user.id,
                         'Код введен успешно... Обновляю базу... Активирую безопасный режим...')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Фух, это было близко...')
        time.sleep(2)
        bot.send_message(message.from_user.id,
                         'Ну ладно, на самом деле, это была последняя проверка - и Вы ее успешно прошли!')
        file = open("D:/PROG/try1/filez/tests/slide37.jpeg", 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.from_user.id,
                         f'Я Вас искренне поздравляю, Вы прошли все испытания! Ваши баллы будут подсчитаны и уже на результатах будут делаться выводы Вашим руководителем - какой Вы сотрудник. Набрали вы баллов в количистве {final_test_count} единиц!')
    else:
        bot.send_message(
            message.from_user.id, 'Код введен неверно! Принудительное завершение рабооты...')
        time.sleep(5)
        bot.send_message(message.from_user.id,
                         'Неплохоя я Вас разыграл, не так ли?')
        bot.send_message(message.from_user.id, 'На самом деле это была последняя проверка. К сожалению, вы ее не прошли. Не беспокойтесь, Вам просто нужно поработать над собой, чтобы не ошибаться в стрессовых ситуациях!')
        time.sleep(7)
        bot.send_message(message.from_user.id,
                         f'Я Вас искренне поздравляю, Вы прошли все испытания! Ваши баллы будут подсчитаны и уже на результатах будут делаться выводы Вашим руководителем - какой Вы сотрудник. Набрали вы баллов в количистве {final_test_count} единиц!')
    time.sleep(7)
    bot.send_message(
        message.from_user.id, 'Благодарю Вас за проведенное со мной время, было очень весело! Если вам нужно что-нибудь еще, напишите /help')
    time.sleep(2)
    file = open("D:/PROG/try1/filez/readyLogoWithTextAndLampslogo2.png", 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.from_user.id,
                     'Еще раз напоминаю, что Вас вводил в курс кибербезопасности Ninja Guardian Bot, спасибо за все!')

    # res_fish = cursor.execute(
    #     'SELECT c_answer1 FROM course_answers WHERE user_id=user_id').fetchone()
    # for res1 in res_fish:
    #     print(res1)
    #     if res1 == 0:
    #         bot.send_message(
    #             message.from_user.id, 'Так как во время курса вы ошиблись в тестовом задании, я Вам предоставляю возможность ответить по-другому на этот раз')
    #         time.sleep(5)
    #         try:
    #             file = open(
    #                 "D:/PROG/try1/filez/tests/fishing_test/slide25.jpeg", 'rb')
    #             bot.send_photo(message.chat.id, file)
    #             markup = types.ReplyKeyboardMarkup(
    #                 row_width=4, resize_keyboard=True, one_time_keyboard=True)
    #             markup.add('Открою, посмотрю содержимое, перейду по ссылочкам', 'Перешлю системному администратору, пусть тоже посмотрит',
    #                        'Посмотрю и сразу удалю', 'Сообщю специалисту компании по ИБ, либо удалю сообщение')
    #             msg = bot.reply_to(
    #                 message, '3 вопрос во теме фишинг', reply_markup=markup)

    #             bot.register_next_step_handler(msg, final_test_p4)

    #         except Exception as e:
    #             bot.reply_to(message, 'oooops')
    #     else:
    #         pass

    # def final_test_p228(message):
    #     global final_test_1c_3q_answer
    #     global final_test_1c_3q_num
    #     final_test_1c_3q_answer = message.text
    #     final_test_1c_3q_answer = 0
    #     time.sleep(1)
    #     bot.send_message(message.from_user.id, 'Обрабатываю...')
    #     time.sleep(3)
    #     if final_test_1c_3q_answer == 'Открою, посмотрю содержимое, перейду по ссылочкам':
    #         final_test_1c_3q_num = 0
    #     elif final_test_1c_3q_answer == 'Перешлю системному администратору, пусть тоже посмотрит':
    #         final_test_1c_3q_num = 0
    #     elif final_test_1c_3q_answer == 'Сообщю специалисту компании по ИБ, либо удалю сообщение':
    #         final_test_1c_3q_num = 10
    #     elif final_test_1c_3q_answer == 'Посмотрю и сразу удалю':
    #         final_test_1c_3q_num = 0
    #     print(final_test_1c_3q_num, '- points for 3rd fishing answ')
    #     time.sleep(3)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Провожу обработку данных...')
        time.sleep(3)
        bot.send_message(
            call.message.chat.id, 'Готово! Теперь, попрошу Вас пройти наш простенький тест, напишите /test :)')
        user_id = call.message.chat.id
        db_table_val(user_id=user_id, name=name, surname=surname,
                     sex=sex, age=age, position=position)
    # elif call.data == 'male':
    #     # sex4 = 'male'
        # get_sex(message=swap)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Не хотите - как хотите...')

# @bot.message_handler(func=lambda c:True, content_types=['text'])#этот блок выполнится если юзер отправит боту сообщение
# def info_message(message):
#     bot.edit_message_reply_markup(message.chat.id, message_id = message.message_id-1, reply_markup = '')# удаляем кнопки у последнего сообщения


bot.polling(none_stop=True, interval=0)

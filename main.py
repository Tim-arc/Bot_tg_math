import math
import telebot
from telebot import types

bot = telebot.TeleBot("1682156942:AAE6aMvManvYkoXUQOi4tIk0yHRxPbqc53E")

@bot.message_handler(commands=['start'])
def start(message):
    print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
    key = types.InlineKeyboardMarkup()
    btn_instruction = types.InlineKeyboardButton(text="Инструкция", callback_data='yes')
    btn_func = types.InlineKeyboardButton(text="Команды", callback_data='func')
    key.add(btn_func, btn_instruction)
    bot.send_message(message.chat.id, "Добро пожаловать в Калькулятор " + str(message.chat.first_name),
                     reply_markup=key)


@bot.callback_query_handler(func=lambda call: True)
def inline(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id,
                         "Введите сначала команду, затем числа через пробел. Вот пример: \n /+ 1 1 "
                         "\n Десятичную часть отделять точкой! \n"
                         "Для площади вводить в том порядке, как написано в описание команды")
    elif call.data == 'func':
        bot.send_message(call.message.chat.id,
                         "/+ - сложение \n /- - вычитание \n /* - умножение \n // - деление \n  /sqr - "
                         "квадратный корень \n /! - факториал \n /pow - возведение числа в степень \n "
                         "/gip - находит гипотенузу по двум катетам \n /cat - находит катет по гипотенузе и катету \n"
                         "/tcos - теорема косинусов \n /s1 - площади треуголника через сторону и высоту к ней \n "
                         "/s2 - через две стороны и сиинус угла между ними \n /s3 - через три стороны \n"
                         "/s4  - через полупериметр и радиус вписанной окружности \n"
                         "/s5 - через три стороны и  радиус описанной окружности")
    else:
        key = types.InlineKeyboardMarkup()
        btn_start = types.InlineKeyboardButton(text="Начать", callback_data='yes')
        key.add(btn_start)
        bot.send_message(call.message.chat.id, "Добро пожаловать в Калькулятор", reply_markup=key)


@bot.message_handler(commands=['+'])
def sum(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(float(arr[1]) + float(arr[2])))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")


@bot.message_handler(commands=['-'])
def sub(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(float(arr[1]) - float(arr[2])))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")


@bot.message_handler(commands=['*'])
def mul(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(float(arr[1]) * float(arr[2])))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")


@bot.message_handler(commands=['/'])
def div(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(float(arr[1]) / float(arr[2])))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")


@bot.message_handler(commands=['sqr'])
def sqr(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(math.sqrt(float(arr[1]))))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")


@bot.message_handler(commands=['!'])
def fac(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(math.factorial(float(arr[1]))))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['pow'])
def pow(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(math.pow(float(arr[1]), float(arr[2]))))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['gip'])
def gip(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        n = math.sqrt((float(arr[1])**2 + float(arr[2])**2))
        if float(arr[1]) + float(arr[2]) > n and n + float(arr[1]) > float(arr[2]) and n + float(arr[2]) > float(arr[1]):
            bot.send_message(message.chat.id, str(n))
        else:
            bot.send_message(message.chat.id, str(message.chat.first_name) + ", прости, но треугольника с такими сторанами не бывает(")
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['cat'])
def cat(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        if arr[1] > arr[2]:
            bot.send_message(message.chat.id, str(math.sqrt((float(arr[1]) ** 2 - float(arr[2]) ** 2))))
        elif arr[2] > arr[1]:
            bot.send_message(message.chat.id, str(math.sqrt((float(arr[2]) ** 2 - float(arr[1]) ** 2))))
        else:
            bot.send_message(message.chat.id, "Это херня какая-то(")
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['tcos'])
def tcos(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        if float(arr[3]) == 1:
            bot.send_message(message.chat.id, "Дурачок, косинус равен единице?")
        elif math.fabs(float(arr[3])) > 1:
            bot.send_message(message.chat.id, "Косинус больше 1, все ясно с тобой")
        else:
            bot.send_message(message.chat.id, str(math.sqrt(float(arr[1])**2 + float(arr[2])**2 - float(arr[1])*float(arr[2])*float(arr[3]))))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['s1'])
def s1(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        bot.send_message(message.chat.id, str(float(arr[1]) * float(arr[2]) * 0.5))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['s2'])
def s2(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        if float(arr[3]) == 1:
            bot.send_message(message.chat.id, "Ну вот как синус равен нулю?")
        elif math.fabs(float(arr[3])) > 1:
            bot.send_message(message.chat.id, "Больше единицы, рил?")
        else:
            bot.send_message(message.chat.id, str(float(arr[1]) * float(arr[2]) * float(arr[3]) * 0.5))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['s3'])
def s3(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        p = (float(arr[1]) + float(arr[2]) + float(arr[3])) * 0.5
        if float(arr[1]) + float(arr[2]) > float(arr[3]) and float(arr[3]) + float(arr[1]) > float(arr[2]) and float(arr[3]) + float(arr[2]) > float(arr[1]):
            bot.send_message(message.chat.id, str(math.sqrt(p*(p - float(arr[1])) * (p - float(arr[2])) * (p - float(arr[3])))))
        else:
            bot.send_message(message.chat.id, str(message.chat.first_name) + ", прости, но треугольника с такими сторанами не бывает(")
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['s4'])
def s4(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        p = (float(arr[1]) + float(arr[2]) + float(arr[3])) * 0.5
        bot.send_message(message.chat.id, str(float(p * float(arr[4]))))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler(commands=['s5'])
def s5(message):
    try:
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        arr = str(message.text)
        arr = arr.split(' ')
        p = (float(arr[1]) * float(arr[2]) * float(arr[3]))
        bot.send_message(message.chat.id, str(float(p / (4 * float(arr[4])))))
    except BaseException:
        bot.send_message(message.chat.id, "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

@bot.message_handler()
def other(message):
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        bot.send_message(message.chat.id, "Это явно не моя команда( \n " + str(message.chat.first_name) + " введи start")

bot.polling(none_stop=True, interval=0, timeout=0)
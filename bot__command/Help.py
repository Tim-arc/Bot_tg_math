from bot__command.Command import Command


class Help(Command):
    def execute(self,  send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            send_func(
                             "/sum - сложение \n"
                             "/sub - вычитание \n"
                             "/mul - умножение \n"
                             "/div - деление \n"
                             "/sqr - квадратный корень \n "
                             "/fac - факториал \n"
                             " /pow - возведение числа в степень\n "
                             "/gip - находит гипотенузу по двум катетам \n"
                             "/cat - находит катет по гипотенузе и катету \n"
                             "/tcos - теорема косинусов \n"
                             "/s1 - площади треуголника через сторону и высоту к ней \n "
                             "/s2 - через две стороны и сиинус угла между ними \n"
                             "/s3 - через три стороны \n"
                             "/s4  - через полупериметр и радиус вписанной окружности \n"
                             "/s5 - через три стороны и  радиус описанной окружности")
            send_func(
                             "Введите сначала команду, затем числа через пробел. Вот пример: \n /+ 1 1 "
                             "\n Десятичную часть отделять точкой! \n"
                             "Для площади вводить в том порядке, как написано в описание команды")
        except BaseException:
            send_func( "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "help"

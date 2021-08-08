from bot__command.Command import Command


class Start(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            send_func(
                             "Добро пожаловать в Калькулятор " + str(message.chat.first_name) + ".  \n "
                                                                                                "Для дополнительной информации введите /help")
        except BaseException:
            send_func( "Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "start"

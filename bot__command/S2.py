from bot__command.Command import Command
import math

class S2(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            if float(arr[3]) == 1:
                send_func("Ну вот как синус равен нулю?")
            elif math.fabs(float(arr[3])) > 1:
                send_func( "Больше единицы, рил?")
            else:
                send_func(str(float(arr[1]) * float(arr[2]) * float(arr[3]) * 0.5))
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "s2"

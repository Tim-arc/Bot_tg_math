from bot__command.Command import Command
import  math

class Gip(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            n = math.sqrt((float(arr[1])**2 + float(arr[2])**2))
            if float(arr[1]) + float(arr[2]) > n and n + float(arr[1]) > float(arr[2]) and n + float(arr[2]) > float(arr[1]):
                send_func(message.chat.id, str(n))
            else:
                send_func(str(message.chat.first_name) + ", прости, но треугольника с такими сторанами не бывает(")
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "gip"
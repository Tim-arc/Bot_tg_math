from bot__command.Command import Command
import math

class S3(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            p = (float(arr[1]) + float(arr[2]) + float(arr[3])) * 0.5
            if float(arr[1]) + float(arr[2]) > float(arr[3]) and float(arr[3]) + float(arr[1]) > float(arr[2]) and float(arr[3]) + float(arr[2]) > float(arr[1]):
                send_func( str(math.sqrt(p*(p - float(arr[1])) * (p - float(arr[2])) * (p - float(arr[3])))))
            else:
                send_func(str(message.chat.first_name) + ", прости, но треугольника с такими сторанами не бывает(")
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "s3"
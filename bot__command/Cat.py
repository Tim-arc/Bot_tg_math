from bot__command.Command import Command
import  math

class Cat(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            if arr[1] > arr[2]:
                send_func(str(math.sqrt((float(arr[1]) ** 2 - float(arr[2]) ** 2))))
            elif arr[2] > arr[1]:
                send_func(str(math.sqrt((float(arr[2]) ** 2 - float(arr[1]) ** 2))))
            else:
                send_func("Это херня какая-то(")
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "cat"
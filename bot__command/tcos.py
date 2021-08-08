from bot__command.Command import Command
import  math

class Tcos(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            if float(arr[3]) == 1:
                send_func("Дурачок, косинус равен единице?")
            elif math.fabs(float(arr[3])) > 1:
                send_func("Косинус больше 1, все ясно с тобой")
            else:
                send_func(str(math.sqrt(float(arr[1])**2 + float(arr[2])**2 - float(arr[1])*float(arr[2])*float(arr[3]))))
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "tcos"
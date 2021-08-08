from bot__command.Command import Command

class S4(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            p = (float(arr[1]) + float(arr[2]) + float(arr[3])) * 0.5
            send_func(str(float(p * float(arr[4]))))
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "s4"
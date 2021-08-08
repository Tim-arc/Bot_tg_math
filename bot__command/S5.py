from bot__command.Command import Command

class S5(Command):
    def execute(self, send_func, message):
        try:
            print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
            arr = str(message.text)
            arr = arr.split(' ')
            p = (float(arr[1]) * float(arr[2]) * float(arr[3]))
            send_func(str(float(p / (4 * float(arr[4])))))
        except BaseException:
            send_func("Ну ты и чмо " + str(message.chat.first_name) + ", мб интсрукцию чекнешь")

    def get_name(self):
        return "s5"
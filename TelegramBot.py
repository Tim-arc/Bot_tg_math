from bot__command.Fac import Fac
from bot__command.Div import Div
from bot__command.Gip import Gip
from bot__command.Mul import Mul
from bot__command.Pow import Pow
from bot__command.Sqr import Sqr
from bot__command.Sub import Sub
from bot__command.S1 import S1
from bot__command.S2 import S2
from bot__command.S3 import S3
from bot__command.S4 import S4
from bot__command.S5 import S5
from bot__command.tcos import Tcos
from bot__command.Cat import Cat
from bot__command.Start import Start
from bot__command.Help import Help
from bot__command.Sum import Sum
import yaml
from bot__command.Command import Command
from telebot import TeleBot


class TelegramBot(TeleBot):
    def __init__(self, token):
        super().__init__(token=token)
        self.commands = {}
        self.register_command(Sum())
        self.register_command(Sub())
        self.register_command(Cat())
        self.register_command(Tcos())
        self.register_command(S5())
        self.register_command(S4())
        self.register_command(S3())
        self.register_command(S2())
        self.register_command(S1())
        self.register_command(Sqr())
        self.register_command(Pow())
        self.register_command(Mul())
        self.register_command(Div())
        self.register_command(Gip())
        self.register_command(Fac())
        self.register_command(Start())
        self.register_command(Help())

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command

    def other(self, send_func, message):
        print('%s (%s): %s' % (message.chat.first_name, message.chat.username, message.text))
        send_func(
                         "Это явно не моя команда( \n " + str(message.chat.first_name) + " введи start")








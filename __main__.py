from TelegramBot import TelegramBot
import yaml

if __name__ == '__main__':
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        token = data['token']

    tg_bot = TelegramBot(token)

    @tg_bot.message_handler()
    def on_message(message):
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            prefix = data['prefix']
            users_id = data['white_list_ids']
            if str(message.chat.id) in users_id:
                text = message.text
                if not text.startswith(prefix):
                    return
                text = text[len(prefix):]

                splited_args = text.split()
                cmd = splited_args[0]
                if cmd not in tg_bot.commands:
                    return

                tg_bot.commands[cmd].execute(lambda msg: tg_bot.send_message(message.chat.id, msg), message)


    tg_bot.polling(none_stop=True, interval=0, timeout=0)
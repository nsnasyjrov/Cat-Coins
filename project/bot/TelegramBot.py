import os
from telebot import TeleBot

from project.BL.players_bl import PlayerBL

class TelegramGameBot:
    def __init__(self):
        self.bot = TeleBot(os.getenv('API_TOKEN'))
        self.register_handlers()

    def register_handlers(self):

        @self.bot.message_handler(commands=['start'])
        def start(msg):
            response = PlayerBL.add_user_bl(msg)
            self.bot.send_message(msg.chat.id, response)

        @self.bot.message_handler(func=lambda msg: True)
        def default_message(msg):
            self.bot.send_message(msg.chat.id,
                                  "Котёночек, ты ввел что-то не то😳🙈 \nВведи /help,"
                                  f"чтобы получить список доступных команд")

    def run_bot(self):
        print("Бот запускается...")
        self.bot.polling()

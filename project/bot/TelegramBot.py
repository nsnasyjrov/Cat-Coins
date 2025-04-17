import os
from telebot import TeleBot

class TelegramGameBot:
    def __init__(self):
        self.bot = TeleBot(os.getenv('API_TOKEN'))
        self.register_handlers()

    def register_handlers(self):

        @self.bot.message_handler(commands=['start'])
        def start(msg):
            self.bot.send_message(msg.chat.id, "Привет, я бот-помощник по игре Cat & Coins!")

    def run(self):
        print("Бот запускается...")
        self.bot.polling()
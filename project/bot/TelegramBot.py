import os
from telebot import TeleBot

from project.BL.players_bl import PlayerBL

class TelegramGameBot:
    def __init__(self):
        self.bot = TeleBot(os.getenv('API_TOKEN'))
        self.register_handlers()

    def register_handlers(self):
        self.register_basic_handlers()
        self.register_help_handlers()

    def register_basic_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start(msg):
            response = PlayerBL.add_user_bl(msg)
            self.bot.send_message(msg.chat.id, response)
        @self.bot.message_handler(commands=['help'])
        def help_message(msg):
            self.bot.send_message(msg.chat.id,
                                  "Список доступных комманд: \n1. /join - начать играть\n2. /top вывести список лидеров"
                                  "\n3. /support - написать в поддержку"
                                  "")

        # @self.bot.message_handler(func=lambda msg: True)
        # def default_message(msg):
        #     self.bot.send_message(msg.chat.id,
        #                           "Котёночек, ты ввел что-то не то😳🙈 \nВведи /help,"
        #                           f"чтобы получить список доступных команд")

    def register_help_handlers(self):
        @self.bot.message_handler(commands=['top'])
        def show_top_of_player(msg):
            top_players = PlayerBL.get_top_players()

            if not top_players:
                self.bot.send_message(msg.chat.id, "Список игроков пуст:(")
            else:
                self.bot.send_message(msg.chat.id, f"Список лучших игроков: \n{top_players}")

        @self.bot.message_handler(commands=['support'])
        def show_support_of_player(msg):
            self.bot.send_message(msg.chat.id, "Ссылка для связи с тех. поддержкой:\nhttps://t.me/pgzero_sup ⚙️💻")

    def run_bot(self):
        print("Бот запускается...")
        self.bot.polling()

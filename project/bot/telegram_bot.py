import telebot
from handlers import main
from project.flask_server.config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

if __name__ == '__main__':
    main(bot)
from os import getenv
from threading import Thread

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.bot.TelegramBot import TelegramGameBot
from project.database.db_utils import create_tables

def create_app():
    app = Flask(__name__)
    create_tables()

    def run_bot():
        bot = TelegramGameBot()
        bot.run_bot()

    Thread(target=run_bot).start()

    return app
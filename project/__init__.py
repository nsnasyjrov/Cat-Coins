from os import getenv
from threading import Thread

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.bot.TelegramBot import TelegramGameBot
from project.database.db_utils import create_tables

db = SQLAlchemy()
db_path = getenv('DATABASE_PATH')

def create_app():
    app = Flask(__name__)
    create_tables()

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    def run_bot():
        bot = TelegramGameBot()
        bot.run_bot()

    Thread(target=run_bot).start()

    return app
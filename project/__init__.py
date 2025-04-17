from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project.database.db_utils import create_tables

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    create_tables()

    db_path = r'C:\Users\WorkProfile\PycharmProjects\pgzero_game\project\database\database.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
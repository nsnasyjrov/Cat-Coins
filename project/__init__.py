from flask import Flask, Blueprint

from project.bot.TelegramBot import TelegramGameBot
from project.flask_server.database.db_utils import create_tables
from project.flask_server.routes import all_routes_blueprint

app_platform = Blueprint('app_platform', __name__)
app_platform.register_blueprint(all_routes_blueprint)

def create_app():
    app = Flask(__name__)


    create_tables()

    # def run_bot():
    #     bot = TelegramGameBot()
    #     bot.run_bot()
    #
    # Thread(target=run_bot).start()

    app.register_blueprint(app_platform, url_prefix='/api')

    return app
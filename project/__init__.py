from flask import Flask, Blueprint
from project.flask_server.database.db_utils import create_tables
from project.flask_server.routes import all_routes_blueprint

app_platform = Blueprint('app_platform', __name__)
app_platform.register_blueprint(all_routes_blueprint)

def create_app():
    app = Flask(__name__)
    create_tables()

    app.register_blueprint(app_platform)
    return app
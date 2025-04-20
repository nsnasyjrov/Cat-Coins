from flask import Blueprint

from project.flask_server.routes.player_routes import player_routes

all_routes_blueprint = Blueprint('all_routes', __name__)

all_routes_blueprint.register_blueprint(player_routes)
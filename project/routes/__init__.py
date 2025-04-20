from flask import Blueprint

from project.routes.game_routes import game_routes

all_routes_blueprint = Blueprint('all_routes', __name__)

all_routes_blueprint.register_blueprint(game_routes)
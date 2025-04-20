from flask import Blueprint, request, jsonify

from project.BL.players_bl import PlayerBL

game_routes = Blueprint('game_routes', __name__)

@game_routes.route('/join', methods=["POST"])
def join():
    data = request.get_json()
    result = PlayerBL.add_user_bl(data["user_id"], data["username"])
    return jsonify(result)



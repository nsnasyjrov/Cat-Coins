from flask import Blueprint, request, jsonify

from project.flask_server.BL.players_bl import PlayerBL
from project.flask_server.BL.validators import validate_coordinate

player_routes = Blueprint('game_routes', __name__)

#GET /state — отдать состояние игрового мира (для отрисовки в Pgz) TODO
#GET /about — страница с твоим описанием (HTML) TODO

@player_routes.route('/join', methods=["POST"])
def join():
    try:
        data = request.get_json()

        if not data or "chat_id" not in data:
            return jsonify({"error": "Не указаны или указаны некорректно поля"}), 400

        chat_id = data["chat_id"]
        username = data.get("username", "Котёночек")

        response = PlayerBL.add_user_bl(chat_id, username)
        if response["status"] == "success":
            return jsonify(response), 201
        elif response["status"] == "already_exists":
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as e:
        return jsonify({"error": f"Ошибка при добавлении пользователя: {e}"})


@player_routes.route('/move', methods=["POST"])
def move():
    try:
        data = request.get_json()
        chat_id = data["chat_id"]
        direction = validate_coordinate(data["direction"])

        if not chat_id or not direction:
            return jsonify({"status": "error", "message": "Поля заполнены некорректно или не заполнены в принципе"}), 400

        player_coord = PlayerBL.get_coordinate(chat_id)

        if player_coord["status"] == "error":
            return jsonify(player_coord), 400

        response = PlayerBL.coordinate_change(direction, chat_id)
        if response["status"] == "success":
            return jsonify(response), 201
        else:
            return jsonify(response), 400
    except Exception as e:
        return jsonify({"error": f"Ошибка при изменении координат пользователя: {e}"})

@player_routes.route('/top', methods=["GET"])
def top():
    res = PlayerBL.get_top_players()

    if not res:
        return {"message": "Список игроков недоступен!"}, 200

    return {"success": res}, 200

@player_routes.route('/my_profile', methods=["POST"])
def my_profile():
    data = request.get_json()
    res = PlayerBL.get_player_info(data["chat_id"])

    if "success" in res:
        return jsonify(res), 200
    else:
        return jsonify(res), 400
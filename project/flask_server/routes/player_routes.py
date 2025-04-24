from flask import Blueprint, request, jsonify

from project.flask_server.BL.players_bl import PlayerBL

player_routes = Blueprint('game_routes', __name__)

@player_routes.route('/join', methods=["POST"])
def join():
    try:
        data = request.get_json()

        if not data or "chat_id" not in data:
            return jsonify({"error": "Не указаны поля"}), 400

        chat_id = data["chat_id"]
        username = data.get("username", "Котёночек")

        response, status_code = PlayerBL.add_user_bl(chat_id, username)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({"error": f"Ошибка при добавлении пользователя: {e}"})

@player_routes.route('/top', methods=["GET"])
def top():
    res = PlayerBL.get_top_players()

    if not res:
        return {"message": "Список игроков недоступен!"}, 200

    return {"success": res}, 200

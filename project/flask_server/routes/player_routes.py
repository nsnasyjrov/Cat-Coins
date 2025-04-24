from flask import Blueprint, request, jsonify

from project.flask_server.BL.players_bl import PlayerBL
from project.flask_server.BL.validators import validate_coordinate
from project.flask_server.DAL.players_dal import PlayerDAL

player_routes = Blueprint('game_routes', __name__)

#POST /join — регистрация игрока
#POST /move — действие игрока (движение)
#GET /state — отдать состояние игрового мира (для отрисовки в Pgz)
#GET /top — таблица лидеров (HTML)
#GET /about — страница с твоим описанием (HTML)

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
        else:
            return jsonify(response), 400
    except Exception as e:
        return jsonify({"error": f"Ошибка при добавлении пользователя: {e}"})


@player_routes.route('/move', methods=["POST"])
def move():
    try:
        data = request.get_json()
        # chat_id в отличие от username по-умолчанию уникален, поэтому лучше его юзать
        chat_id = data["chat_id"]
        direction = validate_coordinate(data["direction"])

        print(f"Направление: {direction}\nЧат: {chat_id}")

        if not chat_id or not direction:
            return jsonify({"status": "error", "message": "Поля заполнены некорректно или не заполнены в принципе"}), 400

        response, player_coord = PlayerBL.get_coordinate(chat_id)

        if player_coord is None:
            return jsonify(response), 400

        PlayerBL.coordinate_change(direction, chat_id)

        return jsonify({"status": "success",
                        "message": response["message"], }), 201
    except Exception as e:
        print(f"Произошла ошибка при передаче координат: {e}")

@player_routes.route('/top', methods=["GET"])
def top():
    res = PlayerBL.get_top_players()

    if not res:
        return {"message": "Список игроков недоступен!"}, 200

    return {"success": res}, 200

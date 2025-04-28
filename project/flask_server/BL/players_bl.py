from project.flask_server.DAL.players_dal import PlayerDAL
from project.flask_server.BL.validators import validate_register

class PlayerBL:
    @staticmethod
    def add_user_bl(chat_id, username):
        validation_result = validate_register(chat_id)

        if validation_result["status"] == "success":
            PlayerDAL.add_player_dal(chat_id, username)
            return {"status": "success", "message": validation_result["message"], "chat_id": chat_id, "username": username}
        else:
            return {"status": validation_result["status"], "message": validation_result["message"]}

    @staticmethod
    def get_top_players():
        players = PlayerDAL.return_top_players()
        if not players:
            return None

        return "\n".join(
            [f"{i + 1}. {username} — {coins_collected} " for i, (username, coins_collected) in enumerate(players)])

    @staticmethod
    def get_coordinate(chat_id: int):
        player_coord = PlayerDAL.get_coordinate(chat_id)

        if not player_coord:
            return {"status": "error",
                    "message": "Игрока с таким chat_id нет или он не найден в базе данных"}

        return {"status": "success",
                "message": "Координаты успешно переданы"}

    @staticmethod
    def coordinate_change(direction: str, chat_id: int) -> dict:
        player_coord = PlayerDAL.get_coordinate(chat_id)

        if not player_coord:
            return {"status": "error", "message": "Игрок с таким chat_id не найден"}

        x, y = player_coord["x"], player_coord["y"]

        if direction == "left":
            x -= 32
        if direction == "right":
            x += 32
        if direction == "up":
            y += 32
        if direction == "down":
            y -= 32

        success = PlayerDAL.coordinate_change(chat_id, x, y)

        if success:
            return {"status": "success", "message": "Координаты успешно изменены"}
        else:
            return {"status": "error", "message": "Не получилось изменить координаты"}
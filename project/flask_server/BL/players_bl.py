from project.flask_server.DAL.players_dal import PlayerDAL
from project.flask_server.BL.validators import validate_register

class PlayerBL:
    @staticmethod
    def add_user_bl(chat_id, username):
        validation_result = validate_register(chat_id)

        if validation_result["status"] == "success":
            PlayerDAL.add_player_dal(chat_id, username)
            return validation_result["message"], 201
        else:
            return validation_result["message"], 400

    @staticmethod
    def get_top_players():
        players = PlayerDAL.return_top_players()
        if not players:
            return None

        return "\n".join(
            [f"{i + 1}. {username} — {coins_collected} " for i, (username, coins_collected) in enumerate(players)])




from project.flask_server.DAL.players_dal import PlayerDAL

class PlayerBL:
    @staticmethod
    def add_user_bl(chat_id, username):
        count = PlayerDAL.check_player_exists(chat_id)

        if count == 0:
            PlayerDAL.add_player_dal(chat_id, username)




    @staticmethod
    def get_top_players():
        players = PlayerDAL.return_top_players()
        if not players:
            return None

        return "\n".join(
            [f"{i + 1}. {username} — {coins_collected} " for i, (username, coins_collected) in enumerate(players)])
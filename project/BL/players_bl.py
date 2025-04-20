from project.DAL.players_dal import PlayerDAL

class PlayerBL:
    @staticmethod
    def add_user_bl(msg):
        count = PlayerDAL.check_player_exists(msg.chat.id)
        username = PlayerBL.user_first_message_validate(msg)

        if count > 0:
            return "Привет, я снова рад тебя видеть, котоигрок! 🐱✨"
        try:
            PlayerDAL.add_player_dal(username, msg.chat.id, 16, 16)
            return "Ты успешно зарегистрирован в игре Cat & Coins! 🐾 Добро пожаловать!"
        except Exception as e:
            print(f"Произошла в бизнес-логике: {e}")
            return "Упс... что-то пошло не так при регистрации. Попробуй ещё раз позже 😿"

    @staticmethod
    def user_first_message_validate(msg):
        username = msg.chat.username
        first_name = msg.from_user.first_name

        if username is not None:
            return username
        elif first_name is not None:
            return first_name
        else:
            return "Котёночек"
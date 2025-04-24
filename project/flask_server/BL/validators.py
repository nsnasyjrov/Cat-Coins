from project.flask_server.DAL.players_dal import PlayerDAL


def validate_register(chat_id) -> dict:
    count = PlayerDAL.check_player_exists(chat_id)

    if count < 0:
        return {"status": "error", "message": "Ошибка при проверке ID"}
    elif count == 0:
        return {"status": "success", "message": "Регистрация возможна"}
    else:
        return {"status": "fail", "message": "Такой пользователь уже существует"}
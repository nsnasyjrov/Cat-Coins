from project.flask_server.DAL.players_dal import PlayerDAL

def validate_register(chat_id) -> dict:
    count = PlayerDAL.check_player_exists(chat_id)

    if count > 0:
        return {"status": "error", "message": "Пользователь уже существует в базе данных!"}
    elif count == 0:
        return {"status": "success", "message": "Пользователь успешно создан!"}
    else:
        return {"status": "fail", "message": "Ошибка"}

def validate_coordinate(direction: str):
    allowed_directions = {"up", "down", "left", "right"}
    if direction in allowed_directions:
        return direction
    return None
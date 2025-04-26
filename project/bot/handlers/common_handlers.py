import requests
from ...flask_server.config import API_URL

def register_common_handlers(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        payload = {
            "chat_id": message.chat.id,
            "username": message.from_user.username
        }

        try:
            response = requests.post(f'{API_URL}/join', json=payload)
            if response.status_code == 201:
                print("Получилось сделать /api/join")
            else:
                print("Не получилось сделать подключение")
        except Exception as e:
            print(f"Ошибка при подключении: {e}")
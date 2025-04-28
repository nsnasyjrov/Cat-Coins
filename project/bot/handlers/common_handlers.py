import requests

from ..utils.bot_utils import TelegramBotUtils
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
                TelegramBotUtils.send_message(bot,
                                              message.chat.id,
                                              "Привет) Ты успешно зарегистрирован в чат-боте, скоро мы начнем играть!",
                                              None)
                TelegramBotUtils.mainmenu_buttons(bot, message.chat.id)
            elif response.status_code == 200:
                TelegramBotUtils.send_message(bot,
                                              message.chat.id,
                                              "Привет)\n Я тебя помню! Ты снова хочешь поиграть?)")
                TelegramBotUtils.mainmenu_buttons(bot, message.chat.id)
        except Exception as e:
            print(f"Ошибка при подключении: {e}")
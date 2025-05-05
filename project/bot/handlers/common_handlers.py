import requests

from ..utils.bot_utils import TelegramBotUtils
from ..utils.converters.response_converter import ResponseConverter
from ..utils.telegram_constants import MAIN_MENU_BUTTONS
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

    @bot.message_handler(func=lambda message: message.text == MAIN_MENU_BUTTONS[0])
    def handle_my_profile(message):
        payload = {
            "chat_id": message.chat.id,
        }

        raw_res = requests.post(f'{API_URL}/my_profile', json=payload)

        if raw_res.status_code == 200:
            TelegramBotUtils.send_message(bot, message.chat.id, ResponseConverter.response_my_profile(raw_res))
        else:
            # убрать после
            TelegramBotUtils.send_message(bot, message.chat.id, "Не нашел по тебе информации")
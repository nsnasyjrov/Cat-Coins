from telebot import types

from project.bot.utils.telegram_constants import MAIN_MENU_BUTTONS

class TelegramBotUtils:
    @staticmethod
    def send_message(bot, chat_id, text, reply_markup=None):
        try:
            bot.send_message(chat_id, text, reply_markup=reply_markup)
        except Exception as e:
            print(f"TelegramBot(send_message): {e}")

    @staticmethod
    def mainmenu_buttons(bot, chat_id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [types.KeyboardButton(text) for text in MAIN_MENU_BUTTONS]
        markup.add(*buttons[:4])
        markup.add(*buttons[4:])
        TelegramBotUtils.send_message(bot, chat_id, "Выбери действие:", markup)
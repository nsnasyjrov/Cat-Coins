from telebot import types

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
        markup.add(
            types.KeyboardButton('Мой профиль💬'),
            types.KeyboardButton('Лучшие игроки🏆'),
            types.KeyboardButton('Помощь🆘'),
            types.KeyboardButton('Играть🐈')
        )
        markup.add(types.KeyboardButton('🏠 Главное меню'), types.KeyboardButton('🚪 Выйти'))
        TelegramBotUtils.send_message(bot, chat_id, "Тестовое сообщение", markup)
from project.bot.handlers.common_handlers import register_common_handlers

def register_handlers(bot):
    register_common_handlers(bot)
    #register_movement_handlers(bot)

def main(bot):
    print("Бот запустился")
    register_common_handlers(bot)
    bot.infinity_polling()
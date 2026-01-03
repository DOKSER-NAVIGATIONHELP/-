import telebot

TOKEN = "8512649228:AAH1JddLJxcRuGhNlCbzVAV9rDo0e6ggb1c"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "<b>Чтобы начать пользоваться комментариями для продажи,</b>\n"
        "<b>необходимо сперва выставить товар в боте @botosos_bot!</b>"
    )


@bot.message_handler(commands=['pytz'])
def pytz(message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        return  # молча игнор

    user = args[1]

    text = (
        "📩 <b>Сообщение по сделке #E873</b>\n\n"
        f"Пожалуйста, отправь {user} подарок, хочу сюрприз устроить, и скрин как забирает.\n"
        "— <i>@Anonim</i>"
    )

    bot.send_message(message.chat.id, text)


bot.infinity_polling()

from utelegram import Bot

TOKEN = "TU_TOKEN"

bot = Bot(TOKEN)

def enviar_mensaje(texto):
    try:
        bot.send_message("TU_CHAT_ID", texto)
    except:
        print("Error enviando mensaje")
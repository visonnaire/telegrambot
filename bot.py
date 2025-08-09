import telebot

bot = telebot.TeleBot("8106333316:AAGRYGiNOaGPV7Y5DU7Iy5EaEcAKpqbLzgw")

bot.remove_webhook()  # Retire webhook la si li te aktive deja

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Bonjou! Mwen se asistan envestisman ou. Ekri /help pou wè sa mwen ka fè.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/start - Kòmanse bot la\n/help - Jwenn èd\n/info - Plis enfòmasyon sou bot la")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Bot sa a ede w dekouvri opòtinite envestisman sou entènèt.")

bot.polling()

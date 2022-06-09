from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


async def hi(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')



app = ApplicationBuilder().token("5471122376:AAFyp6IS0HUKVwEsYo7_qlroHQc5T8Y8Nw0").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("yandex", yandex_command))
print('server start')
app.run_polling()


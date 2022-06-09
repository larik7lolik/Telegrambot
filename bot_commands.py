from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Hi, my dear {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/yandex')

async def time_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()    # /sum 123 4587
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')

async def yandex_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_html(f'https://yandex.ru/')
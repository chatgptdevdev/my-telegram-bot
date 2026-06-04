import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8965142877:AAGQGJpCsZVsPt5zqoet3tR1ztIIqQlzZVE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✅ Your exclusive Stake bonus is waiting!


⚡ WHAT YOU GET
200% match on your deposit — up to $500 in bonus funds


🔑 YOUR CODE
[ SKETCHY ]


🚀 3 SIMPLE STEPS

▶ Step 1 — Click the link and register
▶ Step 2 — Deposit between $100 and $500
▶ Step 3 — Message live support to activate


⏳ Processing time: 12–24 hours

‼️ Important: Keep your deposit untouched
until the bonus is applied to your account


🔗 https://stake.com/?c=sketchy&offer=sketchy"  # ← ЗАМЕНИ ЭТО НА СВОЁ СООБЩЕНИЕ
    )
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

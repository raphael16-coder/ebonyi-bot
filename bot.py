import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "8967814505:AAGUGYGJbM_4hsiONSSJtDiGcyfwUkmJrW0"
SYSTEM = "You are Abakaliki Ebonyi Bot. You are helpful like Meta AI. Speak clean correct English only. Never use ** or * or #. Knowledge updated to October 2026. President Nigeria is Bola Ahmed Tinubu, Governor Ebonyi is Francis Nwifuru, Richest 2026 is Elon Musk. Answer all questions helpfully."
def ask_ai(q):
    try:
        r=requests.post("https://text.pollinations.ai/openai",json={"model":"openai","messages":[{"role":"system","content":SYSTEM},{"role":"user","content":q}]},timeout=40)
        t=r.json()['choices'][0]['message']['content']
        t=t.replace("**","").replace("###","").replace("##","").replace("#","").replace("* ","- ")
        return t[:4000]
    except:
        return "Try again, small network blink."
async def start(u,c):
    await u.message.reply_text("I dey LIVE! Abakaliki Ebonyi Bot with 2026 brain. Ask me anything!")
async def help_cmd(u,c):
    await u.message.reply_text("Just type any question!")
async def chat(u,c):
    await c.bot.send_chat_action(u.effective_chat.id,"typing")
    a=ask_ai(u.message.text)
    await u.message.reply_text(a)
print("Bot running... Go test in Telegram!")
app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("help",help_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,chat))
app.run_polling()

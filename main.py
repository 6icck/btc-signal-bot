import time
import random
from datetime import datetime
from telegram import Bot

BOT_TOKEN = "TON_BOT_TOKEN"
CHANNEL_ID = "@TON_CANAL"

bot = Bot(token=BOT_TOKEN)

def generate_signal():
    levels = ["🟥 Faible", "🟨 Moyen", "🟩 Fiable"]
    level = random.choice(levels)
    entry_price = round(random.uniform(60000, 65000), 2)
    take_profit = entry_price + round(random.uniform(500, 1000), 2)
    stop_loss = entry_price - round(random.uniform(300, 600), 2)
    leverage = random.choice(["5x", "10x", "20x"])
    duration = random.choice(["15min", "1h", "4h"])

    signal = f"""
📢 *Signal BTC avec effet levier*
Niveau: {level}
Direction: 📈 Achat
Effet levier: {leverage}

🎯 Entrée: ${entry_price}
✅ TP: ${take_profit}
❌ SL: ${stop_loss}

⏱️ Durée: {duration}
🕐 Heure: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC
    """
    return signal

while True:
    signal = generate_signal()
    bot.send_message(chat_id=CHANNEL_ID, text=signal, parse_mode='Markdown')
    time.sleep(3600)

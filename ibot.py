from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from deep_translator import GoogleTranslator
from trans import trans
import requests

TOKEN = "8313646879:AAHY3hqp2H31fzT9ltEt8tUFsmdmWNCI9Eo"  # <-- замени на свой токен


def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    syn_response = requests.get(f"https://api.datamuse.com/words?rel_syn={word}")
    if syn_response.status_code == 200:
        synonyms = [item['word'] for item in syn_response.json()[:5]]

    ant_response = requests.get(f"https://api.datamuse.com/words?rel_ant={word}")
    if ant_response.status_code == 200:
        antonyms = [item['word'] for item in ant_response.json()[:5]]

    return synonyms, antonyms


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправь мне текст на русском, "
        "и я переведу его на английский, покажу транслитерацию, синонимы и антонимы."

import os

API_ID = int(os.environ.get("API_ID", "38751960"))
API_HASH = os.environ.get("API_HASH", "4e8f828046a30ec70899b523bd763fa9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8767524865:AAEgszK65_wNdTM2J67Yw8I0SLH6E1DQCdY")
CUSTOM_CAPTION = os.environ.get(
    "CUSTOM_CAPTION",
    "<b>{file_caption}</b>\n\n<b>JOIN 💎 : @Senpai_jiro</b>"
)
ADMINS = list(map(int, os.environ.get("ADMINS", "7754709357").split()))

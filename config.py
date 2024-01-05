#Code by KA18 the @legend580 💛❤️

import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6100891233:AAHo_OjnFWTdY_JewRdcqphxASAcAK1IHVg") #ajhhsa
    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872747581:AAH7_XPCOCEVfbgUhepjJWlcOmj8wjDTjBk") #jn_url

    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1061576483").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATES_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001512853438")

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001512853438"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))
    
    #Port
    PORT = os.environ.get("PORT", "8080")

    START_TEXT = """<b>🤗 Hello {}

    ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ.
    Sᴇɴᴅ ᴍᴇ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴀɴᴅ I ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀs ᴀ ғɪʟᴇ/ᴠɪᴅᴇᴏ.
    Usᴇ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇ</b>"""


    PROGRESS_BAR = """<b>\n
    ╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
    ┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
    ┣⪼ ⏳️ Dᴏɴᴇ : {0}%
    ┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
    ┣⪼ ⏰️ Eᴛᴀ: {4}
    ╰━━━━━━━━━━━━━━━➣ </b>"""
    

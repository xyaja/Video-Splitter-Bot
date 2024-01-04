#Coded by KA18 the @legend580 💛❤️

import os, shutil
from pyrogram import Client, types
from plugins.stuff import parts_handler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@Client.on_callback_query()
async def button(bot, update):
    
    if update.data == "close":
        await update.message.delete(True)
        if os.path.isdir(parts_handler.file_folder):
            shutil.rmtree(parts_handler.file_folder)
    else:
        pass

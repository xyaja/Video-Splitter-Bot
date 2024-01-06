#Coded by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import os
import shutil
import time
from datetime import datetime

from config import Config
from plugins.thumb import *
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram.types import InputMediaPhoto
from plugins.database.database import db
from PIL import Image

async def upload(bot, update, download_directory, description, width, height, duration):
    if (await db.get_upload_as_doc(update.from_user.id)) is False:
        thumbnail = await Gthumb01(bot, update, duration, download_directory)
        await bot.send_document(
            chat_id=update.chat.id,
            document=download_directory,
            thumb=thumbnail,
            caption=description)
    else:
        thumbnail = await Gthumb02(bot, update, duration, download_directory)
        await bot.send_video(
            chat_id=update.chat.id,
            video=download_directory,
            caption=description,
            duration=duration,
            width=width,
            height=height,
            supports_streaming=True,
            thumb=thumbnail)

    #deleting thumbnail aftre the splitted parts upload
    if os.path.exists(thumbnail):
        os.remove(thumbnail)

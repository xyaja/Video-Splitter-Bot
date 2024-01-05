#Coded by KA18 the @legend580 💛❤️

import os, shutil
from config import Config
from pyrogram import Client, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@Client.on_callback_query()
async def button(bot, update):
    
    if update.data == "close":
        await update.message.delete(True)

    elif update.data == "home":
        await update.message.edit_text(
            text=Config.START_TEXT.format(update.from_user.mention),
            reply_markup=Config.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Config.HELP_TEXT,
            reply_markup=Config.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Config.ABOUT_TEXT,
            reply_markup=Config.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    #elif update.data == "showThumbnail":
        #thumbnail = await db.get_thumbnail(update.from_user.id)
        #if not thumbnail:
            #await update.answer("You didn't set any custom thumbnail!", show_alert=True)
        #else:
            #await update.answer()
            #await bot.send_photo(update.message.chat.id, thumbnail, "Custom Thumbnail",
                               #reply_markup=types.InlineKeyboardMarkup([[
                                   #types.InlineKeyboardButton("Delete Thumbnail",
                                                              callback_data="deleteThumbnail")
                               #]]))
    #elif update.data == "deleteThumbnail":
        #await db.set_thumbnail(update.from_user.id, None)
        #await update.answer("Okay, I deleted your custom thumbnail. Now I will apply default thumbnail.", show_alert=True)
        #await update.message.delete(True)
    #elif update.data == "setThumbnail":
        #await update.message.edit_text(
            #text=Translation.TEXT,
            #reply_markup=Translation.BUTTONS,
            #disable_web_page_preview=True
        #)
    else:
        pass

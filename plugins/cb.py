#Coded by KA18 the @legend580 💛❤️

import os, shutil
from config import Config
from pyrogram import Client, types
from plugins.settings.setting import OpenSettings
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.database import db
import logging
from plugins.stuff import auth_user_id
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

    elif update.data == "OpenSettings":
        await update.answer()
        await OpenSettings(update.message)
    elif update.data == "showThumbnail":
        thumbnail = await db.get_thumbnail(update.from_user.id)
        if not thumbnail:
            await update.answer("You didn't set any custom thumbnail!", show_alert=True)
        else:
            await update.answer()
            await bot.send_photo(update.message.chat.id, thumbnail, "Custom Thumbnail",
                               reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("Delete Thumbnail",
                                                              callback_data="deleteThumbnail")
                               ]]))
    elif update.data == "deleteThumbnail":
        await db.set_thumbnail(update.from_user.id, None)
        await update.answer("Okay, I deleted your custom thumbnail. Now I will apply default thumbnail.", show_alert=True)
        await update.message.delete(True)
    elif update.data == "setThumbnail":
        await update.message.edit_text(
            text=Config.TEXT,
            reply_markup=Config.BUTTONS,
            disable_web_page_preview=True
        )

    elif update.data == "triggerUploadMode":
        await update.answer()
        upload_as_doc = await db.get_upload_as_doc(update.from_user.id)
        if upload_as_doc:
            await db.set_upload_as_doc(update.from_user.id, False)
        else:
            await db.set_upload_as_doc(update.from_user.id, True)
        await OpenSettings(update.message)
      
    elif update.data == "addauthuser":
        auth_id = auth_user_id(bot, update)
        await update.answer()
        addauth = await db.get_auth_user(auth_id)
        if addauth:
            await update.message.edit_text(
            text= f"<b>The Given [User](tg://user?id={auth_id}) Is Already an Auth User...!!\nClick Confirm To Remove From An Auth Users List.👇</b>",
            reply_markup=Config.AUTH_DELETE_BUTTONS,
            disable_web_page_preview=True)
        else:
            await db.set_auth_user(auth_id, True)
            await update.message.edit_text(text = f"<b>New User Added🎉.\nUser - [UserLink](tg://user?id={auth_id})</b>")
            await bot.send_message(chat_id = auth_id, text = "<b>Now Your An Authorised User🎉.\nEnjoy Our Service....!!</b>")

    elif update.data == "deleteauthuser":
        auth_id = auth_user_id(bot, update)
        await update.answer()
        await update.message.edit_text(
            text= f"<b>The Given [User](tg://user?id={auth_id}) Is Removed From an Auth User...!!</b>", disable_web_page_preview=True)
        await db.set_auth_user(auth_id, False)
        await bot.send_message(chat_id = auth_id, text = "<b>ɴᴏᴡ ʏᴏᴜʀ ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ᴀɴ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴜꜱᴇʀ.\nʏᴏᴜ ɴᴇᴇᴅ ʙᴜʏ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ꜰʀᴏᴍ [Kannadiga 💛❤️](https://t.me/legend580) ᴛᴏ ʙᴇᴄᴏᴍᴇ ᴀɴ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴜꜱᴇʀ.</b>")
          
    else:
        pass

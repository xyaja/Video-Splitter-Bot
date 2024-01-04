#Coded by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import subprocess
from split import split_parts

@Client.on_message(filters.command('start') & filters.private )
async def start_command(client: Client, message: Message):
    await message.reply_text("hello buddy ......",quote=True)
        
@Client.on_message(filters.private & filters.video)
async def doc(bot, update):
    file = getattr(update, update.media.value)
    filename = file.file_name
    file_folder = f'{DOWNLOAD_LOCATION}{file.file_name.split('_')[0]}{random_char(5)}'
    file_path = f'{file_folder}/{file.file_name.split('.')[0]}.mp4'
    logger.info(file_path)
    output_folder = f'{file_path}/Parts'
    logger.info(f"folder :-{output_folder} ")
    video_length = file.file_size
    logger.info(f"vidlenght :-{video_length} ")
    parts = 2
    if file.file_size > 2000 * 1024 * 1024:
         return await update.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")

    ms = await update.reply_text(text=f"Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....") 
    
    try:
       logger.info('starting download')
       #path = await bot.download_media(message=update, file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time())) 
       await bot.download_media(message=update, file_name=file_path) 
    except Exception as e:
       return await ms.edit(e)
    logger.info('download complete') 
    await ms.edit(text="DL complete")
    #ffmpeg = "ffmpeg/fffmpeg.exe"
    duration = 0
    if os.path.isfile(file_path):
        logger.info("no issues")
        try:
            await ms.edit(text="Starting to split")
            await split_parts(file_path, parts)
            await ms.edit(text="Starting successfully completed..!")
        except:
            await ms.edit(text="somthing went wrong")
    else:
        logger.info("issues found, passing to sub process")
        await ms.edit(text="process excuted somthing wrong")



def random_char(y): #generate random characters for location(path)
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

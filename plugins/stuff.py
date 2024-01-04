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

@Client.on_message(filters.command('start') & filters.private )
async def start_command(client: Client, message: Message):
    await message.reply_text("hello buddy ......",quote=True)
        
@Client.on_message(filters.private & filters.video)
async def doc(bot, update):
    file = getattr(update, update.media.value)
    filename = file.file_name
    file_path = f"downloads/{file.file_name.split('_')[0]}/{file.file_name.split('.')[0]}.mp4"
    logger.info(file_path)
    output_folder = f"downloads/{file.file_name.split('_')[0]}/Parts"
    logger.info(f"folder :-{output_folder} ")
    video_length = file.file_size
    logger.info(f"vidlenght :-{video_length} ")
    parts = 2
    if file.file_size > 2000 * 1024 * 1024:
         return await update.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")

    ms =   await update.reply_text(text=f"Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....") 
    
    try:
       logger.info('starting download')
       #path = await bot.download_media(message=update, file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time())) 
       path = await bot.download_media(message=update, file_name=file_path) 
    except Exception as e:
       return await ms.edit(e)
    logger.info('download complete')       
    duration = 0
    await ms.edit(text="DL complete")
    
    ffmpeg = "ffmpeg/fffmpeg.exe"
    if os.path.isfile(file_path):
        logger.info("no issues")
        await ms.edit(text="starting to split")
        # parts = 4
        duration_per_part = video_length / parts
        acodec="copy"
        vcodec="copy"
        extra=""
        try:
            for i in range(parts):
                logger.info("split start")
                start_time = i * duration_per_part
                logger.info(f"start_time :- {start_time}")
                output_file = os.path.join(output_folder, f"{file.file_name.split('_')[0]}_part_{i+1:02d}.mp4")
                logger.info(f"output_file dire :-{output_file} ")
                # split_cmd = [ffmpeg, "-i", file_path, "-vcodec", vcodec,"-acodec", acodec, "-y"] + shlex.split(extra)
                # split_args += ["-ss", str(start_time), "-t", str(duration_per_part), output_file]
                # subprocess.check_output(split_cmd + split_args)
                
                command_to_exec = ["ffmpeg", "-i", file_path, "-ss", start_time, "-t", duration_per_part, "-c copy", output_file]
                process = await asyncio.create_subprocess_exec(*command_to_exec, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                logger.info("split start2....")
                stdout, stderr = await process.communicate()
                logger.info("split start3......")
                e_response = stderr.decode().strip()
                t_response = stdout.decode().strip()
        except:
            await ms.edit(text="somthing went wrong")
    else:
        logger.info("issues found, passing to sub process")
        await ms.edit(text="process excuted somthing wrong")

#Coded by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from moviepy.video.io.VideoFileClip import VideoFileClip
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import math
import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import subprocess
from config import Config
import random, string, sys
import os
import shutil

@Client.on_message(filters.command('start') & filters.private )
async def start_command(client: Client, message: Message):
    await message.reply_text("hello buddy ......",quote=True)
        
@Client.on_message(filters.command("sp") & filters.private)
async def parts_handler(bot, update):
    user_id = update.from_user.id
    cmd = update.command
    replied = update.reply_to_message
    logger.info(f"Length :- {len(cmd)}")
    if not replied:
        return await update.reply('Reply to any video/file to split.')
    if len(cmd) == 1:
        return await update.reply(text = "You need to reply a /sp command along with split size to any video\n Example: <code>/sp 5</code>")
    elif len(cmd) == 2:
        file = getattr(replied, replied.media.value)
        #try:
        parts = int(cmd[1].strip())
        await splitter(bot, update, parts, file, replied)
        #except:
            #await update.reply(text = "You need to reply a /sp command along with integer value{numbers}\n Example: <code>/sp 5</code>")

async def splitter(bot, update, parts, file, replied):
    filename = file.file_name
    fn = str(file.file_name.split("_")[0])
    file_folder = f'{Config.DOWNLOAD_LOCATION}/{fn}{str(random_char(5))}'
    file_path = f'{file_folder}/{file.file_name.split(".")[0]}.mp4'
    logger.info(file_path)
    output_folder = f'{file_path}/Parts'
    logger.info(f"folder :-{output_folder} ")
    video_length = file.file_size
    logger.info(f"vidlenght :-{video_length} ")
    #parts = 5
    if file.file_size > 2000 * 1024 * 1024:
        await update.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")

    ms = await update.reply_text(text=f"Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....") 
    
    try:
    	logger.info('starting download')
    	await bot.download_media(message = replied , file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
    except Exception as e:
    	return await ms.edit(e)
    logger.info('download complete') 
    await ms.edit(text="DL complete")

    if os.path.isfile(file_path):
        logger.info("no issues")
        await ms.edit(text="Starting to split")
        loc,d = await split_parts(file_path, parts, file_folder)
        for i in range(parts):
            await ms.delete()
            mg = await bot.send_message(chat_id = update.chat.id, text=f"Uploading Part{i+1} video..!")
            await bot.send_video(chat_id = update.chat.id, video = loc + "/part" + str(i+1) + ".mp4", supports_streaming = True, duration=d, width = 640, height = 360, caption = f'<b>{fn}_Part{i+1}.mp4</b>')
            await mg.delete()

        shutil.rmtree(file_folder)
        logger.info("Floder deleted successfully...!")

#generate random characters for location(path)
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

# splitting given video into equal parts
async def split_parts(file_path, parts, file_folder):
    video = VideoFileClip(file_path)
    video_length = video.duration
    logger.info(f"video_length :- {video_length}")
    duration_per_part = video_length / parts
    d = int(duration_per_part)
    output_folder = os.makedirs(f'{file_folder}/Parts')
    output_folder = f'{file_folder}/Parts'
    for i in range(parts):
        logger.info("splitting started")
        start_time = i * duration_per_part
        output_file = os.path.join(output_folder, f"part{i+1}.mp4")
        cmd = f"ffmpeg -i {file_path} -ss {start_time} -t {duration_per_part} -c copy {output_file}"
        process = await asyncio.create_subprocess_exec(
        *cmd,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        logger.info(e_response)
        t_response = stdout.decode().strip()
        #subprocess.check_output(cmd, shell=True)
    return output_folder,d

PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "ᴅ, ") if days else "") + \
        ((str(hours) + "ʜ, ") if hours else "") + \
        ((str(minutes) + "ᴍ, ") if minutes else "") + \
        ((str(seconds) + "ꜱ, ") if seconds else "") + \
        ((str(milliseconds) + "ᴍꜱ, ") if milliseconds else "")
    return tmp[:-2] 

def humanbytes(size):    
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'ʙ'

def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time

async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:        
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["⬢" for i in range(math.floor(percentage / 5))]),
            ''.join(["⬡" for i in range(20 - math.floor(percentage / 5))])
        )            
        tmp = progress + PROGRESS_BAR.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),            
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",               
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="close")]])                                               
            )
        except:
            pass

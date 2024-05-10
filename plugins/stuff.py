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
from plugins.upload import upload
from plugins.database.add import add_user_to_database
from plugins.database.database import db

@Client.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await db.is_user_exist(id):
        try:
          await db.add_user(id)
          await client.send_message(
          Config.LOG_CHANNEL,
             f"<b>#𝐍𝐞𝐰𝐔𝐬𝐞𝐫: \n\n᚛› 𝐈𝐃 - {message.from_user.id} \n᚛› 𝐍𝐚𝐦𝐞 - [{message.from_user.first_name}](tg://user?id={message.from_user.id})</b>"
          )
        except:
          pass
    await message.reply_text(text = Config.START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True, 
        reply_markup=Config.START_BUTTONS, quote=True)

@Client.on_message(filters.command('users') & filters.private & filters.user(Config.OWNER_ID))
async def get_users(client: Client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=Config.WAIT_MSG)
    users = await db.total_users_count()
    await msg.edit(f"{users} users are using this bot")

@Client.on_message(filters.command('users_name') & filters.user(Config.OWNER_ID))
async def list_users(bot, message):
    raju = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        # if user['ban_status']['is_banned']:
        #     out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        pass
        # with open('users.txt', 'w+') as outfile:
        #     outfile.write(out)
        # await message.reply_document('users.txt', caption="List Of Users")
      
@Client.on_message(filters.command('help') & filters.private)
async def help_command(client: Client, message: Message):
    await message.reply_text(text = Config.HELP_TEXT,
        disable_web_page_preview=True, reply_markup=Config.HELP_BUTTONS, quote=True)

@Client.on_message(filters.command('about') & filters.private)
async def about_command(client: Client, message: Message):
    await message.reply_text(text = Config.ABOUT_TEXT,
        disable_web_page_preview=True, reply_markup=Config.ABOUT_BUTTONS, quote=True)

@Client.on_message(filters.command('addauth') & filters.private & filters.user(Config.OWNER_ID))
async def add_auth(bot, update):
    global auth_id
    auth_id = 1
    cmd = update.command
    if len(cmd) == 1:
        await update.reply(text = "Invalid Syntax send the command properly.\nExample: <code>/addauth 1061576483</code>")
    elif len(cmd) == 2:
        try:
            auth_id = int(cmd[1].strip())
            #Config.AUTH_USERS.append(auth_id)
            await update.reply_text(text = f"<b>Do You Want To Add The Given [User](tg://user?id={auth_id}) To An Auth User.\nClick Below Button Confirm 👇</b>",
                                      disable_web_page_preview=True, reply_markup=Config.AUTH_ADD_BUTTONS, quote=True)
        except:
            await update.reply(text = "Invalid User ID, please chech again and resend.")
  
@Client.on_message(filters.command("sp") & filters.private)
async def parts_handler(bot, update):
    user_id = update.from_user.id
    if (await db.get_auth_user(user_id)) is False and not user_id in Config.AUTH_USERS:
        return await update.reply_text(
          text = Config.NOT_AUTH.format(update.from_user.mention),
          disable_web_page_preview=True, quote=True
        )
    user_id = update.from_user.id
    cmd = update.command
    replied = update.reply_to_message
    if not replied:
        return await update.reply('Reply to any video/file to split.')
    if len(cmd) == 1:
        return await update.reply(text = "You need to reply a /sp command along with split size to any video\n Example: <code>/sp 5</code>")
    elif len(cmd) == 2:
        file = getattr(replied, replied.media.value)
        try:
            parts = int(cmd[1].strip())
            await splitter(bot, update, parts, file, replied)
        except Exception as e:
            await update.reply(text = f"You need to reply a /sp command along with integer value{numbers}\n Example: <code>/sp 5</code>\n {e}")

async def splitter(bot, update, parts, file, replied):
    filename = file.file_name
    fn = str(file.file_name.split("_")[0])
    file_folder = f'{Config.DOWNLOAD_LOCATION}/{fn}{str(random_char(5))}'
    file_path = f'{file_folder}/{file.file_name.split(".")[0]}.mp4'
    output_folder = f'{file_path}/Parts'
    video_length = file.file_size
    # if file.file_size > 2000 * 1024 * 1024:
    #     return await update.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")
    ms = await update.reply_text(text=f"Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ....")
    try:
      file_copy = update.reply_to_message
      await bot.download_media(message = replied , file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
      post_message = await file_copy.copy(chat_id = Config.DB_CHANNEL, caption = f"{filename}\nUser - {update.from_user.mention}\nUserId = <code>{update.from_user.id}</code>\nParts - {parts}" , disable_notification=True)
      # post_message = await bot.copy_message(chat_id = Config.DB_CHANNEL, from_chat_id = update.from_user.id, message_id = update.reply_to_message, caption = f"{file_path}\nUser - {update.from_user.mention}\nUserId = {update.from_user.id}", disable_notification=True)
    except Exception as e:
    	return await ms.edit(e," and ",post_message)
    await ms.edit(text="DL complete")

    if os.path.isfile(file_path):
        await ms.edit(text=f"Starting to split {parts} parts.....!!")
        loc,d = await split_parts(file_path, parts, file_folder, fn)
        width = 640
        height = 360
        for i in range(parts):
            await ms.delete()
            mg = await bot.send_message(chat_id = update.chat.id, text=f"<b>Uploading Part{i+1}....!</b>")
            download_directory = loc + "/" + fn+"_Part"+str(i+1) + ".mp4"
            description = f'<b>{fn}_Part{i+1}.mp4</b>'
            await upload(bot, update, download_directory, description, width, height, d)
            await mg.delete()

        #deleting folder aftre the splitted parts upload
        shutil.rmtree(file_folder)

#generate random characters for location(path)
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

# splitting given video into equal parts
async def split_parts(file_path, parts, file_folder, fn):
    video = VideoFileClip(file_path)
    video_length = video.duration
    duration_per_part = video_length / parts
    d = int(duration_per_part)
    output_folder = os.makedirs(f'{file_folder}/Parts')
    output_folder = f'{file_folder}/Parts'
    for i in range(parts):
        start_time = str(i * d)
        dd=str(d)
        output_file = os.path.join(output_folder, fn + "_Part" + str(i+1) + ".mp4")
        
        #One type of command execution - it will print on terminal
        #cmd = f"ffmpeg -i {file_path} -ss {start_time} -t {duration_per_part} -c copy {output_file}"
        #subprocess.check_output(cmd, shell=True)
        
        #Another type of command execution - it will not print on terminal
        command = [
        "ffmpeg",
        "-i",
        file_path,
        "-ss",
        start_time,
        "-t",
        dd,
        "-c", "copy",
        output_file 
        ]
        
        process = await asyncio.create_subprocess_exec(
            *command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
    
    return output_folder,d

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
        tmp = progress + Config.PROGRESS_BAR.format( 
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

@Client.on_message(filters.private & filters.command('broadcast') & filters.user(Config.OWNER_ID))
async def send_text(client: Client, message: Message):
    if message.reply_to_message:
        prit(message.reply_to_message)
        query = await db.full_userbase()
        print(query)
        broadcast_msg = message.reply_to_message
        print(broadcast_msg)
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(Config.REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

def auth_user_id(bot, update):
    user_id = auth_id
    return user_id

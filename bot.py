#Code by KA18 the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from config import Config

from pyrogram import Client as JNbot
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    JNbot = Ntbot(
        "VS Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins)
    JNbot.run()




# import logging
# import os
# from pyrogram import Client

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# bot = Client("Bot", api_id= 3393749, api_hash= "a15a5954a1db54952eebd08ea6c68b71", bot_token= "5872747581:AAH7_XPCOCEVfbgUhepjJWlcOmj8wjDTjBk")

# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="""
#     first upload a video and then you have 4 options.\n\
#     1: /four_part for splitting the video you have sent into 4 equal parts\n\
#     2: /three_part for splitting the video you have sent into 4 equal parts\n\
#     3: /two_part for splitting the video you have sent into 4 equal parts\n\
#     4: and a number to split the given video in customize parts, press /help for more information on how the bot works\n\
#     programmer: @Erfan_Owl121""")



# def help(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="First you need to send a video and then use the commands(/four_part,/three_part, /two_part)\n\
#     If you want to customize the time, you have to send the time that you want the video to be splitted(in second).")



# def download_video(update: Update, context):
#     """Download the video that the user sent."""
#     file_id = update.message.video.file_id
    
#     video_file = context.bot.get_file(file_id)
    
#     video_file.download("video.mp4")
    
#     update.message.reply_text('Video downloaded successfully!')


# def main():
#     """Start the bot."""
#     updater = Updater(token, use_context=True)

#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("help", help))

#     dp.add_handler(CommandHandler('four_part', four_part))
#     dp.add_handler(CommandHandler('three_part', three_part))
#     dp.add_handler(CommandHandler('two_part', two_part))
#     dp.add_handler(MessageHandler(Filters.text, two_custome_part))



#     dp.add_handler(MessageHandler(Filters.video, download_video))


#     updater.start_polling()
#     logger.info("Bot started.")

#     updater.idle()

# if __name__ == '__main__':
#     main()

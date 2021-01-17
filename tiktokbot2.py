import telebot
import tiktok2 as tk 
import time 

TOKEN = ''
tb = telebot.TeleBot(TOKEN)
chat_id = ''

@tb.message_handler(func=lambda message: True)
def send_video(message):
    tb.send_chat_action(message.chat.id, 'upload_video')
    arg = str(message.text)
    tk.mainline(arg)
    video = open('out.mp4', 'rb')
    #tb.send_video(message.chat.id, video, reply_to_message_id=message.message_id)
    tb.send_video(message.chat.id, video)
    video.close()

tb.polling()

while True:
    time.sleep(0)


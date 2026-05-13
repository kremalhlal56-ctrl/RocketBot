import telebot
import requests
import yt_dlp
import os

# توكن البوت الخاص بك
API_TOKEN = '8826770286:AAGuTLioU2TrKkbDHzTt6ThHXKxv_E8039k'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في بوت الصاروخ للتحميل! 🚀\nأرسل رابط فيديو تيك توك الآن.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    if 'tiktok.com' in message.text:
        msg = bot.reply_to(message, "🚀 جاري معالجة الفيديو...")
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4',
            'quiet': True,
            'no_warnings': True
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([message.text])
            
            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video, caption="تم التحميل بواسطة بوت الصاروخ 🚀")
            
            os.remove('video.mp4')
            bot.delete_message(message.chat.id, msg.message_id)
            
        except Exception as e:
            bot.edit_message_text("حدث خطأ أثناء التحميل، تأكد من أن الحساب عام وليس خاصاً.", message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, "عذراً، أرسل رابط تيك توك صحيح.")

bot.polling()

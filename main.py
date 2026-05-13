import telebot
import requests

# مفتاح البوت من تلجرام
CH_TOKEN = "8826770286:AAGuTLioU2TrKkbDHzTt6ThHXKxv_E8039k"

# مفتاح RapidAPI الخاص بك
RAPID_API_KEY = "a633d09fdbmsh7dfce5a83af7405p1c8b1ajsnddecdfd0d28e"

bot = telebot.TeleBot(CH_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في بوت الصاروخ للتحميل! 🚀\nأرسل رابط فيديو تيك توك الآن.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if "tiktok.com" in url:
        bot.reply_to(message, "جاري معالجة الفيديو... 🚀")
        api_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/v1/posts"
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }
        try:
            response = requests.get(api_url, headers=headers, params={"url": url})
            video_link = response.json()['data']['play']
            bot.send_video(message.chat.id, video_link, caption="تم التحميل بواسطة الصاروخ 🚀")
        except:
            bot.reply_to(message, "حدث خطأ، تأكد من الرابط.")
    else:
        bot.reply_to(message, "أرسل رابط تيك توك صحيح.")

bot.polling()

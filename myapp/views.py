from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
import json ,requests
import telebot

# Create your views here.
bot=telebot.TeleBot('請輸入你的token!!!')

class UpdateBot(APIView):
    def post(self,request):
        json_string=request.body.decode('UTF-8')
        update=telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        
        return Response({'code':200})


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hi')
    
    user=User()
    user.user_id=message.chat.id
    user.save()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


'''
# filter on a specific message
#無法跟上面的echo_all 共用
@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")
'''
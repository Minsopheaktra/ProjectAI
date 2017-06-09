from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

channel_access_token = 'AtDHenhT50Lsq5UrOQFviXVpaV2vJNWgM/571eraT8x+dwElMZE4tSI3ssjdOFJZfp6pecTqIRtyx4fQFTw4wwRHRmZcgo+n8oJn1MKQGr1HqpR5q3uo3Hxiy9qkpozuqwe2wWYSPBWvDSbuw7XkegdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)


def send2line(to, message):
    try:
        line_bot_api.push_message(to, TextSendMessage(text=message))
    except LineBotApiError as e:
        print("Error api")

# 'Uff558f7354df1711368b767a1f588b75'
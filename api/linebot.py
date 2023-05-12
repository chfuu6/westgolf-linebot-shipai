from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselColumn,
                            CarouselTemplate, MessageAction, URIAction, ImageCarouselColumn, ImageCarouselTemplate,
                            ImageSendMessage, FlexSendMessage)
import os
from api.func import *

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = Flask(__name__)


# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.message.text == '教練介紹':
        line_bot_api.reply_message(event.reply_token, coach_info())
    if event.message.text == '門市資訊':
        line_bot_api.reply_message(event.reply_token, store_info())
    if event.message.text == '課程預約':
        line_bot_api.reply_message(event.reply_token, reservation('resevation'))
    if event.message.text == '指定教練':
        line_bot_api.reply_message(event.reply_token, reservation('specify'))
    if event.message.text == '不指定教練':
        line_bot_api.reply_message(event.reply_token, reservation('not specify'))



if __name__ == "__main__":
    app.run()

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselColumn,
                            CarouselTemplate, MessageAction, URIAction, ImageCarouselColumn, ImageCarouselTemplate,
                            ImageSendMessage)
import os

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

    image_carousel_columns = [
        ImageCarouselColumn(
            image_url='https://jimmy2130.github.io/WestGolf/images/GaryLuCrop.jpg',
            action=MessageAction(label='Button 1', text='Button 1 pressed')
        ),
        ImageCarouselColumn(
            image_url='https://jimmy2130.github.io/WestGolf/images/VincentLu.jpg',
            action=MessageAction(label='Button 2', text='Button 2 pressed')
        ),
        ImageCarouselColumn(
            image_url='https://jimmy2130.github.io/WestGolf/images/KaiChan.jpg',
            action=MessageAction(label='Button 3', text='Button 3 pressed')
        )
    ]

    image_fee = ImageSendMessage(original_content_url='https://imgur.com/a/xyH9XrP')

    image_carousel_template = ImageCarouselTemplate(columns=image_carousel_columns)
    template_message = TemplateSendMessage(
        alt_text='Image Carousel template',
        template=image_carousel_template
        )

    if event.message.text == '教練介紹':
        line_bot_api.reply_message(event.reply_token, template_message)
    if event.message.text == '費用介紹':
        line_bot_api.reply_message(event.reply_token, image_fee)


if __name__ == "__main__":
    app.run()

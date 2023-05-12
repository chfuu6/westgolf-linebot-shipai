from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselColumn,
                            CarouselTemplate, MessageAction, URIAction, ImageCarouselColumn, ImageCarouselTemplate,
                            ImageSendMessage, FlexSendMessage)
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
            image_url='https://i.imgur.com/DrFIHA1.jpeg',
            action=URIAction(uri='https://i.imgur.com/DrFIHA1.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/jHR50KF.jpeg',
            action=URIAction(uri='https://i.imgur.com/jHR50KF.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/uqLFtAR.jpeg',
            action=URIAction(uri='https://i.imgur.com/uqLFtAR.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/Sy2MTkQ.jpeg',
            action=URIAction(uri='https://i.imgur.com/Sy2MTkQ.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/doKPQdf.jpeg',
            action=URIAction(uri='https://i.imgur.com/doKPQdf.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/rvz8BId.jpeg',
            action=URIAction(uri='https://i.imgur.com/rvz8BId.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/W2n8LN5.jpeg',
            action=URIAction(uri='https://i.imgur.com/W2n8LN5.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/t2svPXe.jpeg',
            action=URIAction(uri='https://i.imgur.com/t2svPXe.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/CHTkxjH.jpeg',
            action=URIAction(uri='https://i.imgur.com/CHTkxjH.jpeg')
        )
    ]

    image_fee = ImageSendMessage(
                    original_content_url='https://i.imgur.com/KDwuzWN_d.webp?maxwidth=760&fidelity=grand',
                    preview_image_url='https://i.imgur.com/KDwuzWN_d.webp?maxwidth=760&fidelity=grand')
    
    flex_storeInfo = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "石牌門市",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "電話",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": "2828-7313",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "地址",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": "台北市北投區承德路七段223之2號",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "營業時間",
                        "size": "sm",
                        "color": "#aaaaaa",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": "週一至週五 09:30-22:00",
                        "size": "sm",
                        "flex": 5,
                        "color": "#666666",
                        "offsetStart": "14px"
                    },
                    {
                        "type": "text",
                        "text": "週六、週日 08:00-19:00",
                        "size": "sm",
                        "flex": 5,
                        "color": "#666666",
                        "offsetStart": "14px"
                    }
                    ],
                    "spacing": "sm"
                }
                ]
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "CALL",
                "uri": "https://linecorp.com"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "WEBSITE",
                "uri": "https://linecorp.com"
                }
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "margin": "sm"
            }
            ],
            "flex": 0
        }
    }
    flex_message = FlexSendMessage(alt_text='門市資訊', contents=flex_storeInfo)
    
    businessHours = '西鈞高爾夫推廣中心\n\
網址：https://jimmy2130.github.io/WestGolf/index.html\n\n\
石牌門市\n\
電話：2828-7313\n\n\
地址：台北市北投區承德路七段223之2號\n\
Line ID：@278cpcwm (要加@)\n\
營業時間：\n\
週一至週五 08:00-22:00\n\
週六、週日 08:00-19:00\n\n\
碧潭門市\n\
電話：2212-6041\n\n\
地址：新北市新店區溪洲路121號\n\
Line ID：@298yqvcd (要加@)\n\
營業時間：\n\
週一至週五 09:30-22:00\n\
週六、週日 08:00-19:00'

    reservation = '感謝您的訊息\n\
課程預約方式：\n\n\
指定教練，請留下\n\
1、指定教練的姓名，2、自己的聯絡電話，3、預約上課的日期、時段。\n\
小編會聯繫教練，快速地回覆您的訊息。\n\n\
不指定教練，請留下\n\
1、自己的聯絡電話，2、預約上課的日期、時段。\n\
小編會盡速為您安排'

    text_businessHours = TextSendMessage(text=businessHours)
    text_reservation = TextSendMessage(text=reservation)
    image_carousel_template = ImageCarouselTemplate(columns=image_carousel_columns)
    template_message = TemplateSendMessage(
        alt_text='教練介紹',
        template=image_carousel_template
        )

    if event.message.text == '教練介紹':
        line_bot_api.reply_message(event.reply_token, template_message)
    # if event.message.text == '費用介紹':
    #     line_bot_api.reply_message(event.reply_token, image_fee)
    if event.message.text == '門市資訊':
        line_bot_api.reply_message(event.reply_token, flex_message)
    if event.message.text == '課程預約':
        line_bot_api.reply_message(event.reply_token, text_reservation)


if __name__ == "__main__":
    app.run()

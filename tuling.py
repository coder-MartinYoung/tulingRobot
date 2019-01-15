# coding = utf8
import requests
import itchat
from random import randint
# 去图灵机器人官网注册后会生成一个apikey，可在个人中心查看
#KEY = '503260c96f354343930d7d887d0ca3dd'
reply_pic = ['我还看不懂图片呐！兄die','宝宝我还看不懂图片呢QAQ','别发图片，我看不懂！','发文字我才能陪你说话哦！']
reply_yuyin = ['我还听不懂语音呐！兄die','宝宝我还听不懂语音呢QAQ','别发语音，我没法听啦！','发文字我才能和你说话哦！']
with open('.\key.txt','r',encoding='utf-8') as f:
    KEY = str(f.read())
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'   : KEY,
        'info'   : msg,   # 这是要发送出去的信息
        'userid'  : 'wechat-rebot',  #这里随意写点什么都行
    }
    try:
        # 发送一个post请求
        r = requests.post(apiUrl, data =data).json()
        # 获取文本信息，若没有‘Text’ 值，将返回Nonoe
        return r.get('text')
    except:
        return
# 通过定义装饰器加强函数 tuling_reply(msg) 功能，获取注册文本信息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 设置一个默认回复，在出现问题仍能正常回复信息
    defaultReply = 'I received: ' +msg['Text']
    reply = get_response(msg['Text'])
    # a or b 表示，如有a有内容，那么返回a，否则返回b
    return reply or defaultReply

@itchat.msg_register('Picture')
def tuling_reply_Pictrue(msg):
    randNum = randint(0,3)
    return reply_pic[randNum]

@itchat.msg_register('Video')
def tuling_reply_Vedio(msg):
    pass

@itchat.msg_register('Recording')
def tuling_reply_Recording(msg):
    randNum = randint(0,3)
    return reply_yuyin[randNum]


# 使用热启动，不需要多次扫码
itchat.auto_login(hotReload=True)
itchat.run()

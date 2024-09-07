from flask import Flask, request
import requests as requests_lib
import json
import os

from groqEngine import GroqAI


channel_token = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')

ChannelAccessToken = channel_token

app = Flask(__name__)
@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "GET":
        return "GET METHOD", 200

    elif request.method == "POST":
    
        data = request.get_data().decode('utf-8')
        print('--------------------->', data)
        # data = json.loads(data)
        # print(data.get("msg"))


        return "This is POST method ", 200
    
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json # return in dict

    # got text in json
    text = data.get("events")[0].get("message").get("text")

    # get response from qroq
    text_res = GroqAI(text)
    
    # get reply token
    replyToken = data.get("events")[0].get("replyToken")

    # send message
    replyMessage(text_res, replyToken, ChannelAccessToken)

    return "received successfully", 200


def replyMessage(msg, replyToken, accessToken):
    url = "https://api.line.me/v2/bot/message/reply"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + accessToken
    }

    data = {
        "replyToken": replyToken,
        "messages": [
            {
                "type": "text",
                "text": msg
            }
        ]
    }

    res = requests_lib.post(url, headers=headers, data=json.dumps(data))

    return "reply message successfully", res.status_code
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
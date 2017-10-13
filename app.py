#!/usr/bin/env python

import os.path, sys
import time
from flask import Flask, request
import requests
import jarvis

app = Flask(__name__)


def reply(user_id, msg):
    print msg
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    try:
        data = request.json
        sender = data['entry'][0]['messaging'][0]['sender']['id']
        message = data['entry'][0]['messaging'][0]['message']['text']
        reply(sender, jarvis.do(message, sender))

    except:
        pass

    return "ok"

if __name__ == '__main__':
    app.run(debug=True)

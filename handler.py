import json
import os
import sys
import re

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def handle_message(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        message_id = str(data["message"]["message_id"])
        chat_id = data["message"]["chat"]["id"]
        response = None
        if "גרביל" in message:
            response = "זה לא ארבע גרביל"
        elif len(re.split(' |_', message)) != 4:
            response = "זה לא ארבע מילים"
        if response:
            data = {
                "text": response.encode("utf8"),
                "chat_id": chat_id,
                "reply_to_message_id": message_id
            }
            url = BASE_URL + "/sendMessage"
            requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
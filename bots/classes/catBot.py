import requests
import json
import os
from constants.urls import catPicURL
from bots.commonBot import CommonBot

class CatBot(CommonBot):
    def action(self):
        url = catPicURL
        cat_api = os.environ["CAT_API"]
        r  = requests.get(url, cat_api)
        parsed_json = json.loads(r.text)
        pic = parsed_json[0]['url']
        msg = pic
        return msg
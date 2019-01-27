import requests
import json
from constants.urls import catPicURL
from bots.commonBot import CommonBot

class CatBot(CommonBot):
    def action(self):
        url = catPicURL
        r  = requests.get(url)
        parsed_json = json.loads(r.text)
        pic = parsed_json['file']
        msg = pic
        return msg
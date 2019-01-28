import requests
import json
from constants.urls import dogPicURL
from bots.commonBot import CommonBot

class DogBot(CommonBot):
    def action(self):
        url = dogPicURL
        r = requests.get(url)
        parsed_json = json.loads(r.text)
        pic = parsed_json['url']
        msg = pic
        return msg
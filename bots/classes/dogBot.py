import requests
import json
from constants import urls
from bots import CommonBot

class CatBot(CommonBot):
    def action(self):
        url = dogPicURL
        r = requests.get(url)
        parsed_json = json.loads(r.text)
        pic = parsed_json['url']
        msg = pic
        return msg
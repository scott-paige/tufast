import requests
from constants import urls

class CatBot(CommonBot):
    def action(self):
        url = catPicURL
        r  = requests.get(url)
        parsed_json = json.loads(r.text)
        pic = parsed_json['file']
        msg = pic
        return msg
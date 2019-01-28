import requests
import json
from constants.urls import trumpQuoteURL
from bots.commonBot import CommonBot

class TrumpBot(CommonBot):
    def action(self):
        url = trumpQuoteURL
        headers = {'accept': 'application/hal+json',}
        r = requests.get(url, headers=headers)
        parsed_json = json.loads(r.text)
        quote = parsed_json['value']
        source = parsed_json['_embedded']['source'][0]['url']
        msg = '{}\n\n{}'.format(quote,source) 
        
        return msg
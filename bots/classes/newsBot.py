import requests
import json
from constants import urls
from bots import CommonBot

class NewsBot(CommonBot):
    r = requests.get(url)
            top_headlines = r.json()
            num_articles = top_headlines['totalResults']
            for x in range(num_articles):
                try:
                    if message.content == top_headlines['articles'][x]['title'] or message.content == top_headlines['articles'][x]['url']:
                        pass
                    else:
                        await client.send_message(message.channel,top_headlines['articles'][x]['title'])
                        await client.send_message(message.channel, top_headlines['articles'][x]['url'])
                except IndexError:
                    pass
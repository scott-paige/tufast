import requests
import json
import discord
from constants.urls import newsURL
from bots.commonBot import CommonBot

class NewsBot(CommonBot):
    def action(self):
        url = newsURL
        r = requests.get(url)
        top_headlines = r.json()
        num_articles = top_headlines['totalResults']
        articles = []
        try:
            for x in range(num_articles):
                articles.append((top_headlines['articles'][x]['title'], top_headlines['articles'][x]['url']))
        except IndexError:
            pass
        finally:
            return articles
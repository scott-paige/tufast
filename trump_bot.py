import discord
import requests
import json
import datetime
import os
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['TOKEN'], os.environ['NEWS_API'])

TOKEN = "{}".format(os.environ["TOKEN"])

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!trumpme') or message.content.startswith('!Trumpme'):
        url = 'https://api.tronalddump.io/random/quote'
        headers = {'accept': 'application/hal+json',}
        r = requests.get(url, headers=headers)
        parsed_json = json.loads(r.text)
        quote = parsed_json['value']
        source = parsed_json['_embedded']['source'][0]['url']
        msg = '{}\n\n{}'.format(quote,source) 
        await client.send_message(message.channel, msg)
    if message.content.startswith('!dog'):
        url = 'https://random.dog/woof.json'
        r = requests.get(url)
        parsed_json = json.loads(r.text)
        pic = parsed_json['url']
        msg = pic
        await client.send_message(message.channel, msg)
    if message.content.startswith('!cat'):
        url = 'https://aws.random.cat/meow'
        r  = requests.get(url)
        parsed_json = json.loads(r.text)
        pic = parsed_json['file']
        msg = pic
        await client.send_message(message.channel, msg)
    if message.content.startswith('!headlines'):
        url = ('https://newsapi.org/v2/top-headlines?'
                'country=us&'
                'apiKey={}'.format(os.environ['NEWS_API']))
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
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
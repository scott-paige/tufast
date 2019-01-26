import os
import discord
from dotenv import load_dotenv

from constants import commands
from bots.botFactory import BotFactory
from utils.getArgs import getArgs

load_dotenv()

DISCORD_TOKEN = os.getenv('TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    userMessage = list(map(lambda x: x.rstrip(), message.content.split('--')))
    command = userMessage[0]
    args = getArgs(userMessage)

    bot = BotFactory.createBot(command)

    bot.setArgs(args)
    bot.setChannel(message.channel)
    bot.setClient(client)

    response = bot.action()
    await bot.sendMessage(response)


@client.event
async def on_ready():
    print('%s Started' % client.user.name)

client.run(DISCORD_TOKEN)

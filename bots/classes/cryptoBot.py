import requests

from constants.urls import coinGeckoBaseURL
from bots.commonBot import CommonBot
from constants import params
from utils.createCryptoMessage import createCryptoMessage


class CryptoBot(CommonBot):
    def action(self):
        url = f'{coinGeckoBaseURL}{params.getAllCryptoCoinsForUSMarket}'
        response = requests.get(url).json()
        message = f'```diff\n{createCryptoMessage(response[:10])}```'
        return message

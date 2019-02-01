import constants.commands as commands
from bots.classes.dogBot import DogBot
from bots.classes.catBot import CatBot
from bots.classes.newsBot import NewsBot
from bots.classes.weatherBot import WeatherBot
from bots.classes.trumpBot import TrumpBot
from bots.classes.cryptoBot import CryptoBot

class BotFactory(object):
    @staticmethod
    def createBot(commandType):
            if commandType == commands.weather:
                return WeatherBot()
            if commandType == commands.trumpme:
                return TrumpBot()
            if commandType == commands.cat:
                return CatBot()
            if commandType == commands.dog:
                return DogBot()
            if commandType == commands.news:
                return NewsBot()
            if commandType == commands.crypto:
                return CryptoBot()

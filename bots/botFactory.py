import constants.commands as commands
from .weatherBot import WeatherBot

class BotFactory(object):
    @staticmethod
    def createBot(commandType):
            if commandType == commands.weather:
                return WeatherBot()


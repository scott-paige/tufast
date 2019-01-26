import constants.commands as commands
from .weatherBot import WeatherBot

class BotFactory(object):
    @staticmethod
    def createBot(commandType):
            if commandType == commands.weather:
                return weatherBot()
            if commandType == commands.trumpme:
                return trumpBot()
            if commandType == commands.cat:
                return catBot()
            if commandType == commands.dog:
                return dogBot()



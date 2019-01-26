import constants.commands as commands
from .weatherBot import WeatherBot

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



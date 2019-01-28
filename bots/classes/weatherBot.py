import requests

from bots.commonBot import CommonBot
from constants.urls import weatherBaseURL
from constants import params


class WeatherBot(CommonBot):
    def action(self):
        city = ' '.join(self._args)

        if city:
            url = f'{weatherBaseURL}{params.getWeatherByCity%city}'
        else:
            url = f'{weatherBaseURL}{params.getWeatherByGeolocation}'

        return requests.get(url).text

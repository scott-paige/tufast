import urllib.request as request

from .commonBot import CommonBot
from constants import urls

class WeatherBot(CommonBot):
    def action(self):
        city = ' '.join(self._args)

        if len(city):
            url = urls.weatherBaseURL + '/%s?format=4'%city
        else:
            url = urls.weatherBaseURL + '?format=1'

        return request.urlopen(url).read().decode('utf-8')

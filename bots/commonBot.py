import abc

class CommonBot(metaclass=abc.ABCMeta):
    def __init__(self):
        self._args = None
        self._client = None
        self._channel = None
    def setArgs(self, args):
        self._args = args
    def setClient(self, client):
        self._client = client
    def setChannel(self, channel):
        self._channel = channel
    @abc.abstractmethod
    def action(self):
        pass
    async def sendMessage(self, message):
        await self._client.send_message(self._channel, message)

import functools

from .getPrefix import getPrefix
from .formatCurrency import formatCurrency
from .formatPercentage import formatPercentage


def responseReducer(previous, current):
    obj = current.copy()
    name = obj['name']
    percentChange = obj['price_change_percentage_24h']
    price = obj['current_price']
    prefix = getPrefix(percentChange)
    formattedPrice = formatCurrency(price)
    formattedPercentChange = formatPercentage(percentChange)
    return previous + f'{prefix} {name} {formattedPrice} {formattedPercentChange} \n'


def createCryptoMessage(arr):
    return functools.reduce(responseReducer, arr, '')

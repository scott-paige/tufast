import os

weatherBaseURL = 'https://wttr.in'
trumpQuoteURL = 'https://api.tronalddump.io/random/quote'
catPicURL = 'https://aws.random.cat/meow'
dogPicURL = 'https://random.dog/woof.json'
newsURL = ('https://newsapi.org/v2/top-headlines?'
                'country=us&'
                'apiKey={}'.format(os.environ["NEWS_API"]))

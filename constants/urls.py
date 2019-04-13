import os
from dotenv import load_dotenv

load_dotenv()

weatherBaseURL = 'https://wttr.in'
trumpQuoteURL = 'https://api.tronalddump.io/random/quote'
catPicURL = 'https://api.thecatapi.com/v1/images/search'
dogPicURL = 'https://random.dog/woof.json'
newsURL = ('https://newsapi.org/v2/top-headlines?'
                'country=us&'
                f'apiKey={os.environ["NEWS_API"]}')
coinGeckoBaseURL = 'https://api.coingecko.com/api/v3'

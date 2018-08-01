TOKEN = "bot:Token"
NAME = "seed_bot"
WEBHOOK = False
## The following configuration is only needed if you setted WEBHOOK to True ##
IP = '0.0.0.0'
PORT = 443
URL_PATH = TOKEN # This is recommended for avoiding random people making fake updates to your bot
WEBHOOK_URL = f'https://example.com/{TOKEN}'
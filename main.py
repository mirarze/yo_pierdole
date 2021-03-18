from sys import argv
from bot import Bot

token = ''

try:
    token = argv[1]
except:
    print('No token!')
    raise

bot = Bot()
bot.run(token)

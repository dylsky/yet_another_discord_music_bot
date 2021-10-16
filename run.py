"""
based on https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d
"""
from time import sleep

import youtube_dl
import logging
import json

from discord import LoginFailure
from discord.ext import commands
from CogsColletion.music_cogs import MusicCogs


logging.basicConfig(filename='app.log', level=logging.INFO)


# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''
TOKEN = ''
with open('config.json') as json_data_file:
    config_token = json.load(json_data_file)['token']
    if config_token is not None:
        TOKEN = config_token

bot = commands.Bot(command_prefix='~', description='Yet another music bot.')
bot.add_cog(MusicCogs(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    logging.info('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

while True:
    try:
        bot.run(TOKEN)
    except LoginFailure as e:
        logging.error(e)
        raise
    except Exception as e:
        logging.error(e)
        sleep(10)


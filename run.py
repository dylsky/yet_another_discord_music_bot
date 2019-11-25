"""
based on https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d
"""

import youtube_dl
import json
from discord.ext import commands

# Silence useless bug reports messages
from music_commands import Music

youtube_dl.utils.bug_reports_message = lambda: ''
TOKEN = ''
with open('config.json') as json_data_file:
    config_token = json.load(json_data_file)['token']
    if config_token is not None:
        TOKEN = config_token

bot = commands.Bot(command_prefix='~', description='Yet another music bot.')
bot.add_cog(Music(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))


bot.run(TOKEN)

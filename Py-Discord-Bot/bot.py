import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Bot logged in')

client.load_extension('cogs.coggies')

client.run('MYKEYWASHERE:)<3')

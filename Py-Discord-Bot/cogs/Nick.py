 import discord
from discord.ext import commands


class Nick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.commands()
    async def nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick='nick')


def setup(client):
    client.add_cog(Nick(client))

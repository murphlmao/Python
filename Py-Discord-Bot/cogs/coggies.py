import discord
from discord.ext import commands
from discord.utils import get
from discord import Permissions

class Basics(commands.Cog):

    def __init__(self, client):
        self.client = client

# $Ping - Recieve the message 'Pong!'
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

# Purge Messages ($purge {default is 50} [Amount])
    @commands.command()
    async def purge(self, ctx, amount=50):
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=amount + 1):
            messages.append(message)

        await channel.delete_messages(messages)

# Nickname member ($nick @member [nickname])
    @commands.command()
    async def nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)

# Not sure if Shutdown is working - come back to this later
    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 221742540754386944:  # UserID
            print("shutdown")
            try:
                await self.client.logout()
            except Exception:
                print("EnvironmentError")
                self.client.clear()
        else:
            await ctx.send("No auth.")

# Spam message: ($spam [Amount] [Message])
    @commands.command(name='spam')
    async def spam(ctx, amount: int, *, message):
        for i in range(amount):
            await ctx.send(message)


def setup(client):
    client.add_cog(Basics(client))

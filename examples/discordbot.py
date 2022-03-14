"""
This is just an example;
"""

import animu
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
token = 'ANIMU API TOKEN'

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def test(ctx):
    client = animu.Client(token)
    object = await client.fact()
    await ctx.send(object.fact)
    

bot.run('DISCORD BOT TOKEN')
import discord
import json
import datetime
import requests
from discord.ext import commands
from discord_components import *
import os
import keep_alive

bot = commands.Bot(command_prefix='+')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot上線了!")
    await bot.change_presence(activity=discord.Game(name="我的作者:Man頭(´・ω・)"))

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(F'cogs.{extension}')
    await ctx.send(F'已讀取 {extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(F'cogs.{extension}')
    await ctx.send(F'已卸載 {extension}')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(F'cogs.{extension}')
    await ctx.send(F'已重新載入 {extension}')

for Filename in os.listdir('./cogs'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cogs.{Filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    my_secret = os.environ['TOKEN']
    bot.run(my_secret) 
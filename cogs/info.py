import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
import platform
import time
start_time = time.time()

class info(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info'])
    async def _info(self, ctx):
        #Uptime
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        guild = self.bot.get_guild(889054851496046632)
        #Emoji
        linux_emoji = discord.utils.get(guild.emojis, name="linux")
        heroku_emoji = discord.utils.get(guild.emojis, name="heroku")
        clock_emoji = discord.utils.get(ctx.message.guild.emojis, name="alarm_clock")
        #Embed
        embed = discord.Embed()
        embed = discord.Embed(title="鰻頭機器人#2692", description="", color=discord.Colour.random(), timestamp= datetime.datetime.utcnow())
        embed = discord.Embed(color=discord.Colour.random(), title="機器人狀態 :robot:", inline=True) 
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
        embed.add_field(name=f"{linux_emoji}"+"系統型號", value="{}".format(str(platform.system() + platform.release()), inline=False))
        embed.add_field(name=f"{heroku_emoji}"+"託管商", value="Heroku", inline=True)
        embed.add_field(name=f"{clock_emoji}"+"開機時間", value="{}".format(text), inline=True)
        embed.set_footer(text="本機器人使用Discord.py烹煮而成 (？", icon_url="https://cdn.discordapp.com/emojis/998817330689744947.webp?size=96&quality=lossless")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
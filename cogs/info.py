import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
import platform

class info(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info'])
    async def _info(self, ctx):
        guild = self.bot.get_guild(889054851496046632)
        emoji = discord.utils.get(guild.emojis, name="python")
        embed = discord.Embed()
        embed = discord.Embed(title="鰻頭機器人#2692", description="", color=discord.Colour.random(), timestamp= datetime.datetime.utcnow())
        embed = discord.Embed(color=discord.Colour.random(), title="機器人狀態 :robot:", inline=True) 
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
        embed.add_field(name="系統型號", value="{}".format(str(platform.system() + platform.release()), inline=False))
        embed.add_field(name=f"{emoji}" + "託管商", value="Heroku", inline=True)
        embed.set_footer(name="本機器人使用Discord.py烹煮而成 (？", icon_url="https://cdn.discordapp.com/attachments/980061083349970994/998817046022336562/763439936803569724.webp")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
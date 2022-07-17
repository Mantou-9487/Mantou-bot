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
        embed = discord.Embed()
        embed = discord.Embed(title="鰻頭機器人", description="", color=discord.Colour.random(), timestamp= datetime.datetime.utcnow())
        embed = discord.Embed(color=discord.Colour.random(), title="機器人狀態:robot:", timestamp= datetime.datetime.utcnow(), inline=True) 
        embed.add_field(name="系統型號", value="{}".format(str(platform.system() + platform.release()), inline=False))
        embed.add_field(name="查看延遲", value="Ping", inline=False)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
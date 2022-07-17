import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension


# 這邊可以使用Cog功能繼承基本屬性
class ping(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(aliases=['ping'])
    async def _ping(self, ctx):
        embed = discord.Embed()
        embed = discord.Embed(color=discord.Colour.random(), title="", description="", timestamp= datetime.datetime.utcnow()) 
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
        embed.add_field(name="Pong!", value=":ping_pong: | 延遲率為 {} 毫秒!".format(round(self.bot.latency*1000)), inline=True)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))
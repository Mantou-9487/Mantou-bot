import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension

# 這邊可以使用Cog功能繼承基本屬性
class invite(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('啟動main成功!')

    @commands.command(aliases=['invite'])
    async def _invite(self, ctx):
        embed=discord.Embed(title="已建立邀請連結", color=discord.Colour.random() ,timestamp= datetime.datetime.utcnow())
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(invite(bot))
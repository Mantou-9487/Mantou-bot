import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension

# 這邊可以使用Cog功能繼承基本屬性
class help(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        embed = discord.Embed()
        embed = discord.Embed(title="鰻頭機器人", description="指令前綴為 +", color=discord.Colour.random(), timestamp= datetime.datetime.utcnow())
        embed = discord.Embed(color=discord.Colour.random(), title="指令清單", timestamp= datetime.datetime.utcnow(), inline=True) 
        embed.add_field(name="邀請", value="invite", inline=False)
        embed.add_field(name="查看延遲", value="Ping", inline=False)
        embed.add_field(name="問機器人問題", value="question", inline=False)
        embed.add_field(name="音樂指令 (仍在測試)", value="p, play", inline=False)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
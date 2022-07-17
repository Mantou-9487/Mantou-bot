import discord
from discord.ext import commands
from core.classes import Cog_Extension

# 這邊可以使用Cog功能繼承基本屬性
class main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(main(bot))
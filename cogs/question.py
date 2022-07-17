from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension
import datetime
from numpy import random

class question(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['question'])
    async def _question(self, ctx, question):
        answer = ["從科學上的角度來說...是的", 
        "我覺得其實不行", "我不確定啦(#`Д´)ﾉ" ,
        "等我遇到紅翼大大在跟你說:D" ,
        "怎麼會有人連這問題都無法回答哩~"]
        l = random.choice(answer)
        embed = discord.Embed()
        embed = discord.Embed(color=discord.Colour.random(), title="問題系統 (?", description="", timestamp= datetime.datetime.utcnow()) 
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
        embed.add_field(name="你的問題為 {}".format(f'{question}'), value="{}".format(f'{l}'), inline=True)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(question(bot))
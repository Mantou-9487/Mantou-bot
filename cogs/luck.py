from discord.ext import commands
import discord
from core.classes import Cog_Extension
import datetime
from numpy import random
client = discord.Client()

class luck(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['luck'])
    async def _luck(self, ctx):
        answer = ["大吉","中吉","小吉"]
        l = random.choice(answer)
        embed = discord.Embed()
        embed = discord.Embed(color=discord.Colour.random(), title="運勢唬爛器", description="", timestamp= datetime.datetime.utcnow()) 
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
        embed.add_field(name=f"{ctx.author.mention}\n今日運勢" , value="||{}||".format(f'{l}'), inline=True)
        await ctx.channel.send(f"{ctx.author.mention}")
        await ctx.channel.send(embed=embed)
    
   
   

def setup(bot):
    bot.add_cog(luck(bot))
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension
import datetime

class event(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['setgame'])
    async def _setgame(self, ctx, game):
        if commands.is_owner:
                activity = discord.Streaming(platform="YouTube", name="{}".format(game), url="https://www.youtube.com/watch?v=1XJG00cYLFU")
                embed = discord.Embed()
                embed = discord.Embed(color=discord.Colour.random(), title="遊戲設定", description="", timestamp= datetime.datetime.utcnow()) 
                embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
                embed.add_field(name="你設定的遊戲為" , value="{}".format(game) , inline=True)
                await self.bot.change_presence(status=discord.Status.online, activity=activity)
                await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(event(bot))
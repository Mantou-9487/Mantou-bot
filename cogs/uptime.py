import discord, datetime, time
from discord.ext import commands
from core.classes import Cog_Extension

start_time = time.time()


class uptime(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['uptime'])
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Sponsored by altcointrain.com - Choo!!! Choo!!!")
        try:
            await self.bot.say(embed=embed)
        except discord.HTTPException:
            await self.bot.say("Current uptime: " + text)


def setup(bot):
    bot.add_cog(uptime(bot))
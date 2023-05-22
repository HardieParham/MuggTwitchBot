from twitchio.ext import commands

from ..config.twitch_config import config


"""Sub Cog for sub-only functions"""
class Sub(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot,
        self.token = config['BOT_TOKEN'],

    async def cog_check(self, ctx) -> bool | None:
        if ctx.message.author.is_subscriber == True:
            return True
        else:
            await ctx.send(f"Only Subscribers can use this command.")


    def prepare(bot: commands.Bot) -> None:
            bot.add_cog(Sub(bot))


    @commands.command(name = "subtest")
    async def admintest(self, ctx) -> None:
        await ctx.send("Hello Sub!")
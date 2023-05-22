from twitchio.ext import commands
from ..config.twitch_config import config


"""Follower Cog for follower-only functions"""
class Follower(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot,
        self.token = config['BOT_TOKEN'],

    async def cog_check(self, ctx) -> bool | None:
        if ctx.message.author.is_turbo == True:
            return True
        else:
            await ctx.send(f"Only Followers can use this command.")


    def prepare(bot: commands.Bot) -> None:
            bot.add_cog(Follower(bot))


    @commands.command(name = "followertest")
    async def admintest(self, ctx) -> None:
        await ctx.send("Hello Follower!")
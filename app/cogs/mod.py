from twitchio.ext import commands

from ..config.twitch_config import config


"""Mod Cog for mod-only functions"""
class Mod(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot,
        self.token = config['BOT_TOKEN'],

    async def cog_check(self, ctx) -> bool | None:
        if ctx.message.author.is_mod == True:
            return True
        else:
            await ctx.send(f"Only Moderators can use this command.")


    def prepare(bot: commands.Bot) -> None:
            bot.add_cog(Mod(bot))


    @commands.command(name = "modtest")
    async def admintest(self, ctx) -> None:
        await ctx.send("Hello Mod!")
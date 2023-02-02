from twitchio.ext import commands
from app.config import twitch_config

class Mod(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot,
        self.token = twitch_config.BOT_TOKEN,

    async def cog_check(self, ctx):
        if ctx.message.author.is_mod == True:
            return True
        else:
            await ctx.send(f"Only Moderators can use this command.")


    def prepare(bot: commands.Bot):
            bot.add_cog(Mod(bot))
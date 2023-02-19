from twitchio.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    async def cog_check(self, ctx):
        if ctx.message.author.name.lower() == "crazymugg":
            return True
        else:
            await ctx.send("Only Admins can use this command")

    def prepare(bot: commands.Bot):
            bot.add_cog(Admin(bot))


    @commands.command(name = "admintest")
    async def admintest(self, ctx):
        await ctx.send("Hello Admin!")


# TODO
# OBS Controls
# Spotify Controls
# TTS Controls
# Bot Controls

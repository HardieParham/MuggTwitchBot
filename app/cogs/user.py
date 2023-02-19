from twitchio.ext import commands
from app.config import twitch_config
from app.modules import spotify

class User(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot,
        self.token = twitch_config.BOT_TOKEN,

    # async def cog_check(self, ctx):
    #     if ctx.message.author.is_mod == True:
    #         return True
    #     else:
    #         await ctx.send(f"Only Moderators can use this command.")


    def prepare(bot: commands.Bot):
            bot.add_cog(User(bot))


    @commands.command(name = "test")
    async def admintest(self, ctx):
        await ctx.send("Hello There!")





    # General Commands
    @commands.command(name = "commands", aliases=["commandlist", "help", "idk"])
    async def commandlist(self, ctx):
        keys = self.command_list.keys()
        await ctx.send(keys - "dict_keys")


    @commands.command(name = "lurk")
    async def lurk(self, ctx):
        await ctx.send(f"{ctx.author.name} is going for a lurk! peepoLeave ")


    @commands.command(name = "unlurk")
    async def unlurk(self, ctx):
        await ctx.send(f"{ctx.author.name} is back from some zany adventures! peepoArrive ")


    @commands.command(name = "specs", aliases=["pc"])
    async def specs(self, ctx):
        await ctx.send(f"CPU: Intel i7-8700.           GPU: MSI GTX 1060 6GB.               RAM: 32GB (4x8).            HDD: 4TB HHD, 2-256GB SSD")


    @commands.command(name = "song")
    async def song(self, ctx):
        #sp.song()
        await ctx.send(spotify.song())
        print("worked")










    #ChatGuessr Commands
    @commands.command(name="cg")
    async def cg_command(self, ctx: commands.bot.Context):
        pass


    @commands.command(name="me")
    async def me_command(self, ctx: commands.bot.Context):
        pass


    @commands.command(name="best")
    async def best_command(self, ctx: commands.bot.Context):
        pass


    @commands.command(name="flag")
    async def flag_command(self, ctx: commands.bot.Context):
        pass
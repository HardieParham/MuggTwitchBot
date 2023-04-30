import time

from twitchio.ext import commands
from obswebsocket import requests

from app.config import twitch_config
from ..modules.obs import ws


class Vip(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot,
        self.token = twitch_config.BOT_TOKEN,

    async def cog_check(self, ctx):
        if ctx.message.author.is_vip == True:
            return True
        else:
            await ctx.send(f"Only VIP's can use this command.")


    def prepare(bot: commands.Bot):
            bot.add_cog(Vip(bot))


    @commands.command(name = "viptest")
    async def admintest(self, ctx):
        await ctx.send("Hello VIP!")


    @commands.command(name = "finland")
    async def finland(self, ctx):
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=True))
        time.sleep(2)
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))
import time

from twitchio.ext import commands
from obswebsocket import requests

from ..config.twitch_config import config
from ..modules.obs import ws


"""VIP Cog for VIP-only functions"""
class Vip(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot,
        self.token = config['BOT_TOKEN'],

    async def cog_check(self, ctx) -> bool | None:
        if ctx.message.author.is_vip == True:
            return True
        else:
            await ctx.send(f"Only VIP's can use this command.")


    def prepare(bot: commands.Bot) -> None:
            bot.add_cog(Vip(bot))


    @commands.command(name = "viptest")
    async def admintest(self, ctx) -> None:
        await ctx.send("Hello VIP!")


    @commands.command(name = "finland")
    async def finland(self, ctx) -> None:
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=True))
        time.sleep(2)
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))
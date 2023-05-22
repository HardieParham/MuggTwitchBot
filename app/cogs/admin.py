import logging
import time

from twitchio.ext import commands
from obswebsocket import requests

from ..modules.obs import ws


"""Admin Cog for admin-only functions"""
class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_check(self, ctx) -> bool | None:
        if ctx.message.author.name.lower() == "crazymugg":
            return True
        else:
            await ctx.send("Only Admins can use this command")

    def prepare(bot: commands.Bot) -> None:
            bot.add_cog(Admin(bot))


    @commands.command(name = "admintest")
    async def admintest(self, ctx) -> None:
        await ctx.send("Hello Admin!")



    # OBS Commands
    @commands.command(name = "reconnect")
    async def reconnect(self, ctx) -> None:
        try:
            ws.reconnect()
            await ctx.send("Reconnected OBS.")
        except:
            logging.warning('OBS failed to reconnect')
            await ctx.send("OBS failed to reconnect.")


    @commands.command(name = "disconnect")
    async def disconnect(self, ctx) -> None:
        try:
            ws.disconnect()
            await ctx.send("Disconnected OBS.")
        except:
            logging.warning('OBS failed to disconnect')
            await ctx.send("OBS failed to disconnect.")



    @commands.command(name = "finland2")
    async def test_finland(self, ctx) -> None:
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=True))
        time.sleep(2)
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


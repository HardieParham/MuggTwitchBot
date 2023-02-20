# Standard Imports
import logging

# External Imports
from twitchio.ext import commands

# Local Imports
#from app.modules.obs import Obs
from app.modules import spotify, tts, obs


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


    @commands.command(name = "reconnect")
    async def reconnect(self, ctx):
        try:
            obs.reconnect()
            await ctx.send("Reconnected OBS.")
        except:
            logging.warning('OBS failed to reconnect')
            await ctx.send("OBS failed to reconnect.")


    @commands.command(name = "disconnect")
    async def disconnect(self, ctx):
        try:
            obs.disconnect()
            await ctx.send("Disconnected OBS.")
        except:
            logging.warning('OBS failed to disconnect')
            await ctx.send("OBS failed to disconnect.")


    @commands.command(name = "artist")
    async def artist(self, ctx):
        text = spotify.artist()
        await ctx.send(f"{text}")


    @commands.command(name = "songlink")
    async def song_link(self, ctx):
        text = spotify.song_link()
        await ctx.send(f"{text}")


    @commands.command(name = "queue", aliases=['q',])
    async def song_queue(self, ctx):
        text = spotify.song_queue()
        await ctx.send(f"{text}")


    @commands.command(name = "spvolume")
    async def set_spotify_volume(self, ctx):
        volume=int(ctx.view.words[1])
        if volume > 0 and volume < 101:
            spotify.set_volume(volume)
            await ctx.send(f"Spotify volume has been set to {volume}%.")
        
        else:
            await ctx.send(f"Please specify a number between 0 and 100.")



    @commands.command(name = "say")
    async def say(self, ctx):
        q = ctx.message.content[4:]
        tts.speak(q)


    @commands.command(name = "ttsvolume")
    async def set_tts_volume(self, ctx):
        volume=int(ctx.view.words[1])
        if volume > 0 and volume < 101:
            tts.set_volume(volume)
            await ctx.send(f"tts volume has been set to {volume}%.")
        
        else:
            await ctx.send(f"Please specify a number between 0 and 100.")



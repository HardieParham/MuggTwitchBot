# Standard Imports
import logging
import time

# External Imports
from twitchio.ext import commands
from twitchio import Channel, User, Client
from obswebsocket import requests

# Local Imports
#from app.modules.obs import Obs
from app.modules import spotify, tts
from app.modules.obs import ws
from app.config import twitch_config


class User(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot,
        self.token = twitch_config.BOT_TOKEN,


    def prepare(bot: commands.Bot):
            bot.add_cog(User(bot))


    @commands.command(name = "test")
    async def admintest(self, ctx):
        await ctx.send("Hello There!")



    # Spotify Commands
    @commands.command(name = "sr")
    async def sr(self, ctx):
        query = ctx.message.content[3:]
        
        spotify.sp_search(query)
        await ctx.send(f"song added to queue!")


    @commands.command(name = "skip")
    async def skip(self, ctx):
        spotify.skip()
        await ctx.send(f"Song skipped!")


    @commands.command(name = "previous")
    async def previous(self, ctx):
        spotify.previous()
        await ctx.send(f"Reeling it back.")



    @commands.command(name = "song")
    async def song(self, ctx):
        await ctx.send(spotify.song())


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



    # TTS Commands
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





    @commands.command(name = "noot")
    async def noot(self, ctx):
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Noot', visible=True))
        time.sleep(9)
        ws.call(requests.SetSceneItemProperties(item='Noot', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))
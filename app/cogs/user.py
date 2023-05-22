import time

from twitchio.ext import commands
from twitchio import User
from obswebsocket import requests

from ..modules import spotify, tts
from ..modules.obs import ws
from ..config.twitch_config import config


"""User Cog for user-only functions"""
class User(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot,
        self.token = config['BOT_TOKEN'],


    def prepare(bot: commands.Bot) -> None:
            bot.add_cog(User(bot))


    @commands.command(name = "test")
    async def admintest(self, ctx) -> None:
        await ctx.send("Hello There!")


    @commands.command(name = "noot")
    async def noot(self, ctx):
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Noot', visible=True))
        time.sleep(9)
        ws.call(requests.SetSceneItemProperties(item='Noot', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))




    """Spotify Commands"""
    @commands.command(name = "sr")
    async def sr(self, ctx) -> None:
        query = ctx.message.content[3:]
        
        spotify.sp_search(query)
        await ctx.send(f"song added to queue!")


    @commands.command(name = "skip")
    async def skip(self, ctx) -> None:
        spotify.skip()
        await ctx.send(f"Song skipped!")


    @commands.command(name = "previous")
    async def previous(self, ctx) -> None:
        spotify.previous()
        await ctx.send(f"Reeling it back.")


    @commands.command(name = "song")
    async def song(self, ctx) -> None:
        await ctx.send(spotify.song())


    @commands.command(name = "artist")
    async def artist(self, ctx) -> None:
        text = spotify.artist()
        await ctx.send(f"{text}")


    @commands.command(name = "songlink")
    async def song_link(self, ctx) -> None:
        text = spotify.song_link()
        await ctx.send(f"{text}")


    @commands.command(name = "queue", aliases=['q',])
    async def song_queue(self, ctx) -> None:
        text = spotify.song_queue()
        await ctx.send(f"{text}")


    @commands.command(name = "spvolume")
    async def set_spotify_volume(self, ctx) -> None:
        volume=int(ctx.view.words[1])
        if volume > 0 and volume < 101:
            spotify.set_volume(volume)
            await ctx.send(f"Spotify volume has been set to {volume}%.")
        
        else:
            await ctx.send(f"Please specify a number between 0 and 100.")




    """TTS Commands"""
    @commands.command(name = "say")
    async def say(self, ctx) -> None:
        q = ctx.message.content[4:]
        tts.speak(q)


    @commands.command(name = "ttsvolume")
    async def set_tts_volume(self, ctx) -> None:
        volume=int(ctx.view.words[1])
        if volume > 0 and volume < 101:
            tts.set_volume(volume)
            await ctx.send(f"tts volume has been set to {volume}%.")
        
        else:
            await ctx.send(f"Please specify a number between 0 and 100.")




    """General Commands"""
    @commands.command(name = "commands", aliases=["commandlist", "help", "idk"])
    async def commandlist(self, ctx) -> None:
        keys = self.command_list.keys()
        await ctx.send(keys - "dict_keys")


    @commands.command(name = "lurk")
    async def lurk(self, ctx) -> None:
        await ctx.send(f"{ctx.author.name} is going for a lurk! peepoLeave ")


    @commands.command(name = "unlurk")
    async def unlurk(self, ctx) -> None:
        await ctx.send(f"{ctx.author.name} is back from some zany adventures! peepoArrive ")


    @commands.command(name = "specs", aliases=["pc"])
    async def specs(self, ctx) -> None:
        await ctx.send(f"CPU: Intel i7-8700.           GPU: MSI GTX 1060 6GB.               RAM: 32GB (4x8).            HDD: 4TB HHD, 2-256GB SSD")




    """ChatGuessr Commands"""
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
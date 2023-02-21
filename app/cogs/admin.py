# Standard Imports
import logging

# External Imports
from twitchio.ext import commands
from twitchio import Channel, User, Client

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



    # OBS Commands
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




    # Twitchio Commands TODO
    # @commands.command(name="addmod")
    # async def add_mod(self, ctx):
    #     for word in ctx.view.words:
    #         if ctx.view.words[word][0] == '@':
    #             so_user = ctx.view.words[word][1:]
    #             break
    #     await ctx.send(f"Check out {so_user} at www.twitch.tv/{so_user} ")


    # @commands.command(name="so")
    # async def shoutout(self, ctx):
    #     for word in ctx.view.words:
    #         if ctx.view.words[word][0] == '@':
    #             so_username = ctx.view.words[word][1:]
    #             break
    #     so_user = commands.Bot.get_channel(so_username)
    #     await ctx.send(f"Check out {so_user} at www.twitch.tv/{so_user} ")



# Active Extensions
# Ban, Userban
# Ban Event
# Bits Leaderboard
# Channel Emote
# Channel Info
# Chat Settings
# Chatter
# Clip, Video
# Custom Reward, redemption
# Follow Event
# Game
# Global Emote
# Goal
# Hype Train: Contribution, Event
# Poll
# Predictions
# SearchUser
# Stream
# Subscription Event
# Timeout
#
# User ->
# 
# add mod, add vip, and remove
# ban user
# announcement?
# create clip, poll, prediction
# edit channel description
# fetch followers, followercount
# fetch clips
# follow
# modify stream
# shoutout
# start commercial
# timeout user
# 
#  #
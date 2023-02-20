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
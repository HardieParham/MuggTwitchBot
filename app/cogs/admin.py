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
            ws.reconnect()
            await ctx.send("Reconnected OBS.")
        except:
            logging.warning('OBS failed to reconnect')
            await ctx.send("OBS failed to reconnect.")


    @commands.command(name = "disconnect")
    async def disconnect(self, ctx):
        try:
            ws.disconnect()
            await ctx.send("Disconnected OBS.")
        except:
            logging.warning('OBS failed to disconnect')
            await ctx.send("OBS failed to disconnect.")



    @commands.command(name = "finland2")
    async def test_finland(self, ctx):
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=True))
        time.sleep(2)
        ws.call(requests.SetSceneItemProperties(item='Finland', visible=False))
        ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


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

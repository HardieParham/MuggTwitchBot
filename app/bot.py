# Standard Imports
import logging
import os
import csv

# External Imports
import twitchio
from twitchio.ext import commands, routines

# Local Imports
import app.config.twitch_config as twitch_config
from app.cogs import admin, mod, vip, sub, follower, user
from app.modules import pubsub, spotify, tts, obs


class Twitchbot(commands.Bot):
    def __init__(self):
        super().__init__(
            nick = twitch_config.NICK,
            initial_channels = [twitch_config.CHANNEL],
            token = twitch_config.BOT_TOKEN,
            api_token = twitch_config.API_TOKEN,
            client_id = twitch_config.CLIENT_ID,
            prefix = twitch_config.PREFIX)

        self.channel = twitch_config.CHANNEL
        #self.user_token = twitch_config.USER_TOKEN2
        self.id = twitch_config.CHANNEL_ID
        self.http = "http://localhost:17563"
        self.modules = []


    async def event_ready(self):
        self.command_list = self.commands
        print(f'Logged in as | {self.nick}')


        # # # Modules appear to be outdated method. Loading Cogs is the new fad now
        #Loading Cogs
        try:
            admin.Admin.prepare(self)
            mod.Mod.prepare(self)
            vip.Vip.prepare(self)
            sub.Sub.prepare(self)
            follower.Follower.prepare(self)
            user.User.prepare(self)
            print('STATUS: Cogs Loaded')
        except:
            logging.warning("Modules were not loaded correctly")


        #Loading OBS
        try:
            obs.connect()
            print('STATUS: OBS Connected')
        except:
            logging.warning("Obs failed to load")


        #Loading Spotify
        try:
            spotify.connect()
            print('STATUS: Spotify Connected')
        except:
            logging.warning('Spotify failed to load')


        #Loading TTS
        try:
            tts.connect()
            print('STATUS: TTS Connected')
        except:
            logging.warning('TTS failed to load')


        #try:
        await pubsub.start()
        print('STATUS: Pubsub loop started')
        #except:
            #logging.warning('Pubsub failed to start')


    async def event_message(self, message):

        if message.echo != True:
            print('message recieved')
        #     data = [
        #     message.author,
        #     message.channel,
        #     message.content,
        #     message.echo,
        #     message.first,
        #     message.id,
        #     message.raw_data,
        #     message.tags,
        #     message.timestamp,
        #     ]
        #     for i in data:
        #         print(i)
            if message.content[0] == self._prefix:
                await self.handle_commands(message)


    async def event_join(self, channel, user):
        print(f"{user.name} joined.")

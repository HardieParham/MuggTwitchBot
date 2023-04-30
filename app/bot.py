# Standard Imports
import logging
import os
import csv
import re

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
        self.user_token = twitch_config.USER_TOKEN2
        self.id = twitch_config.CHANNEL_ID
        self.http = "http://localhost:17563"
        self.modules = []


    async def event_ready(self):
        self.command_list = self.commands
        print(f'Logged in as | {self.nick}')
        self.follower_update.start()


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
            # print('message recieved')
            # data = [
            # message.author,
            # message.channel,
            # message.content,
            # message.echo,
            # message.first,
            # message.id,
            # message.raw_data,
            # message.tags,
            # message.timestamp,
            # ]
            # for i in data:
            #     print(i)
            print(f"{message.author.name} - {message.content}")

            if message.content[0] == self._prefix:
                await self.handle_commands(message)


    async def event_join(self, channel, user):
        print(f"{user.name} joined.")


    async def event_part(self, user):
        print(f"{user.name} left.")


    @routines.routine(seconds=5)
    async def follower_update(self):
        script_path = os.path.dirname(__file__)
        log_path = 'data/lists/recentfollow.txt'
        abs_file_path = os.path.join(script_path, log_path)
        with open(abs_file_path, "r", encoding="utf-8") as q:
            old = q.read()
            q.close()
        follower_list = []
        users = (await twitchio.PartialUser.fetch_followers(self, token=self.user_token))
        for items in range(len(users)):
            x = str(users[items])
            result = re.search("name=(.*)> to_user", x)
            follower_list.append(result.group(1))
        recent = follower_list[0]
        #print(follower_list)
        if recent != old:
            with open(abs_file_path, "w", encoding="utf-8") as f:
                f.write(f"{recent}")
                f.close()
            await Twitchbot.new_follower()


    async def new_follower():
        print("neat")
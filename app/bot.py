import logging
import os
import re

import twitchio
from twitchio.ext import commands, routines

from .config.twitch_config import config
from .cogs import admin, mod, vip, sub, follower, user
from .modules import pubsub, spotify, tts, obs


class Twitchbot(commands.Bot):
    """
    creates an instance of a twitchio command bot.


    Parameters
    ------------
    None

    Returns
    --------
    None
    """
    def __init__(self) -> None:
        super().__init__(
            nick = config['NICK'],
            initial_channels = [config['CHANNEL']],
            token = config['BOT_TOKEN'],
            api_token = config['API_TOKEN'],
            client_id = config['CLIENT_ID'],
            prefix = config['PREFIX'])

        self.channel = config['CHANNEL']
        self.user_token = config['USER_TOKEN2']
        self.id = config['CHANNEL_ID']
        self.http = "http://localhost:17563"
        self.modules = []


    async def event_ready(self) -> None:
        self.command_list = self.commands
        print(f'Logged in as | {self.nick}')
        self.follower_update.start()


        """Loading Cogs"""
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


        """Loading OBS"""
        try:
            obs.connect()
            print('STATUS: OBS Connected')
        except:
            logging.warning("Obs failed to load")


        """Loading Spotify"""
        try:
            spotify.connect()
            print('STATUS: Spotify Connected')
        except:
            logging.warning('Spotify failed to load')


        """Loading TTS"""
        try:
            tts.connect()
            print('STATUS: TTS Connected')
        except:
            logging.warning('TTS failed to load')


        """Loading PubSub"""
        try:
            await pubsub.start()
            print('STATUS: Pubsub loop started')
        except:
            logging.warning('Pubsub failed to start')


    async def event_message(self, message) -> None:
        if message.echo != True:
            print(f"{message.author.name} - {message.content}")

            if message.content[0] == self._prefix:
                await self.handle_commands(message)


    async def event_join(self, channel, user) -> None:
        print(f"{user.name} joined.")


    async def event_part(self, user) -> None:
        print(f"{user.name} left.")


    """Routine to update the most recent follower. TODO Refactor this."""
    @routines.routine(seconds=5)
    async def follower_update(self) -> None:
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
        if recent != old:
            with open(abs_file_path, "w", encoding="utf-8") as f:
                f.write(f"{recent}")
                f.close()
            await Twitchbot.new_follower()


    async def new_follower():
        print("Thanks for the follow!")
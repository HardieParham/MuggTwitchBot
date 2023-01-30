
# Standard Imports
import logging

# External Imports
import twitchio
from twitchio.ext import commands, routines

# Local Imports
import app.config.twitch_config as twitch_config


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




    async def event_ready(self):
        try:
            self.load_module('cogs.admin')
            print("Admin cog has been loaded.")
        except:
            logging.warning("Admin module was not loaded correctly")
        
        try:
            self.load_module('cogs.mod')
            print("Mod cog has been loaded.")
        except:
            logging.warning("Mod module was not loaded correctly")

        try:
            self.load_module('cogs.sub')
            print("Sub cog has been loaded.")
        except:
            logging.warning("Sub module was not loaded correctly")

        try:
            self.load_module('cogs.user')
            print("User cog has been loaded.")
        except:
            logging.warning("User module was not loaded correctly")


        self.command_list = self.commands
        print(f'Logged in as | {self.nick}')

        # try:
        #     Obs.connect()
        # except:
        #     print("Obs failed to load")


    async def event_message(self, message):
        try:
            # - Logging 
            a = (f"{message.timestamp} - {message.author.name} - {message.content}")
            b = (f"{message.author.name} - {message.content}")
            print(a)
        except (AttributeError):
            pass


    @commands.command(name="cg")
    async def cg_command(self, ctx: commands.bot.Context):
        pass
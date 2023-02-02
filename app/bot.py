
# Standard Imports
import logging
import os

# External Imports
import twitchio
from twitchio.ext import commands, routines

# Local Imports
import app.config.twitch_config as twitch_config
from app.cogs import admin, mod, sub, user


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

        #Find Modules
        # for x in os.listdir(f'{os.path.dirname(os.path.abspath(__file__))}/cogs'):
        #     if x.endswith(".py"):
        #         file_name = x.removesuffix('.py')
        #         self.modules.append(file_name)
        
        try:
            admin.Admin.prepare(self)
            mod.Mod.prepare(self)
            sub.Sub.prepare(self)
            user.User.prepare(self)
        except:
            logging.warning("Modules were not loaded correctly")

        #Load Modules
        #for module in self.modules:
            #try:
                #file = str(f'./cogs/{module}')
                #self.load_module(file)
                #print("User cog has been loaded.")
            #except:
                #logging.warning(f"{module} module was not loaded correctly")



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

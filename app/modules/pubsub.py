# Standard Imports
import asyncio
import time

# External Imports
import twitchio
from twitchio.ext import pubsub
from obswebsocket import requests

# Local Imports
import app.config.twitch_config as twitch_config
import app.modules.spotify as spotify
from app.modules.obs import ws


my_token = twitch_config.BOT_TOKEN2
user_token = twitch_config.USER_TOKEN2
user_channel_id = int(twitch_config.CHANNEL_ID)
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)



@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    if event.reward.title == "Dab":
        print('Dab MF')


    elif event.reward.title == "Spotify Song Request":
        q = event.input
        try:
            spotify.sp_search(query=q)
            print("sucess!")

        except:
            print('Spotify search failed')





# Bits
# Bits Badge
# Channel Points
# Channel Subscriptions
# Moderation User Action



async def main():
    topics = [
        pubsub.channel_points(user_token)[user_channel_id],
        pubsub.bits(user_token)[user_channel_id],
        pubsub.whispers(user_token)[user_channel_id]
    ]
    await client.pubsub.subscribe_topics(topics)
    #print("PubSub Loop Started")
    await client.start()


# - - - Asyncio way to loop start - - - 
# async def start():
#     loop = asyncio.get_event_loop()
#     loop.create_task(main())


# - - - Quick Example way to loop start - - - 
async def start():
    client.loop.run_until_complete(await main())
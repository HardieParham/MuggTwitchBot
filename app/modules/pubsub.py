import twitchio
from twitchio.ext import pubsub
from obswebsocket import requests

from ..config.twitch_config import config
from ..modules.spotify import sp_search
from ..modules.obs import ws


"""Applying Configuration Settings""" 
my_token = config['BOT_TOKEN2']
user_token = config['USER_TOKEN2']
user_channel_id = int(config['CHANNEL_ID'])
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)


"""Function to handle channel point redemptions"""
@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage) -> None:
    if event.reward.title == "Dab":
        print('Dab MF')

    elif event.reward.title == "Spotify Song Request":
        q = event.input
        try:
            sp_search(query=q)
            print("sucess!")
        except:
            print('Spotify search failed')


async def main() -> None:
    topics = [
        pubsub.channel_points(user_token)[user_channel_id],
        pubsub.bits(user_token)[user_channel_id],
        pubsub.whispers(user_token)[user_channel_id]
    ]
    await client.pubsub.subscribe_topics(topics)
    await client.start()


async def start() -> None:
    client.loop.run_until_complete(await main())
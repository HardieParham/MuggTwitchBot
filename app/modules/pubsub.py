# Standard Imports
import asyncio
import time
import random

# External Imports
import twitchio
from twitchio.ext import pubsub
from obswebsocket import obsws, events, requests

# Local Imports
from app.config import twitch_config
#from app.modules.obs import Obs
from app.modules import spotify, tts, obs
from app.cogs.sub import Sub
#from playsound import playsound



my_token = twitch_config.BOT_TOKEN2
user_token = twitch_config.USER_TOKEN2
user_channel_id = twitch_config.CHANNEL_ID
#topic = pubsub.channel_points(user_token)[user_channel_id]
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)
ad_list = ["Ad-Refrigerators", "Ad-PizzaBall", "Ad-JonesBbq", "Ad-HhGregg", "Ad-HeadOn", "Ad-FruitEBars", "Ad-Contacts", "Ad-BigRed", "Ad-BBQueer"]



@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    #print("hi")
    #print(event)
    #print(event.reward)
    #Sprint(str(event.timestamp) + ": " + str(event.user.name) + ": " + str(event.reward.title) + ": " + str(event.input))
    #print(event.reward.cooldown)
    #print(event.channel_id)
    #print(event.input)
    #print(event.status)
    #print(event.timestamp)
    #print(event.user.name)

    # if event.reward.title == "Play a special advert":
    #     x=random.randint(0,8)
    #     ad=ad_list[x]
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item=f'{ad}', visible=True))
    #     time.sleep(11)
    #     Obs.ws.call(requests.SetSceneItemProperties(item=f'{ad}', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


    if event.reward.title == "Spotify Song Request":
        q = event.input
        await sp_search(query=q)
        print("failed")


    elif event.reward.title == "TTS":
        q = event.input
        obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        tts.speak(q)
        obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


    # elif event.reward.title == "Dab":
    #     #current = Obs.ws.call(requests.GetCurrentScene)
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
    #     playsound('D:\Code_Projects\CrazyMuggBotNew\sounds\Damn_Son.Wav')
    #     time.sleep(1)
    #     Obs.ws.call(requests.SetCurrentScene(scene_name="Main-Webcam"))
    #     time.sleep(3)
    #     Obs.ws.call(requests.SetCurrentScene(scene_name= "Aerial-Cam"))
    #     time.sleep(3)
    #     Obs.ws.call(requests.SetCurrentScene(scene_name= "Main-Display"))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


    # elif event.reward.title == "Unexpected":
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Unexpected', visible=True))
    #     time.sleep(8)
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Unexpected', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


    elif event.reward.title == "Noot":
        obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
        obs.ws.call(requests.SetSceneItemProperties(item='Noot', visible=True))
        time.sleep(9)
        obs.ws.call(requests.SetSceneItemProperties(item='Noot', visible=False))
        obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))

    # elif event.reward.title == "Pizza":
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Pizza', visible=True))
    #     time.sleep(15)
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Pizza', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


    # elif event.reward.title == "Bop":
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Pizza', visible=True))
    #     time.sleep(15)
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Pizza', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))

    # elif event.reward.title == "Soul":
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Soul', visible=True))
    #     time.sleep(15)
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Soul', visible=False))
    #     Obs.ws.call(requests.SetSceneItemProperties(item='Spotify', visible=True))


async def sp_search(query):
        q = query
        x = q.split("-")
        artist = x[0]
        song = x[1]
        spotify.play(artist = artist, track= song)


@client.event()
async def event_pubsub_chat_msg(event: pubsub.PubSubChatMessage):
    print("Hello")


async def main():
    topics = [
        pubsub.channel_points(token=user_token)[user_channel_id],
        pubsub.bits(user_token)[user_channel_id],
        pubsub.whispers(user_token)[user_channel_id]
    ]
    await client.pubsub.subscribe_topics(topics)
    print("PubSub Loop Started")
    await client.start()
    #print("no")


async def start():
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    # try:
    #     loop.run_forever()
    # except (AssertionError):
    #     pass




    # ##Pubsub Topics List
    # bits 
    # bits badge 
    # channel points 
    # channel Subscriptions
    # moderation user action 
    # whispers



    # ##EVentsub
    # Notification_follow
    # Notification_Subscription
    # Notification_Cheer
    # Notification_raid
    # Notification PollS
    # notifications Predictions


    ## Channel points 
    # Song request
    # Random Ad
    # Switch to Dab Cam?
    # Swith to workout cam?
    # TTS redemption

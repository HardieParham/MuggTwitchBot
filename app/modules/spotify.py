# Standard Imports
import logging

# External Imports
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

# Local Imports
from app.config import spotify_config


# - - - - - Applying Configuration Settings - - - - - 
client_id = spotify_config.client_id
client_secret = spotify_config.client_secret
device_name = spotify_config.device_name
redirect_uri = spotify_config.redirect_uri
scope = spotify_config.scope
username = spotify_config.username
auth_manager = SpotifyOAuth(
    client_id = client_id,
    client_secret = client_secret,
    redirect_uri = redirect_uri,
    scope = scope,
    username = spotify_config.username)


# - - - - - Connecting to Spotify - - - - - 
spotify = sp.Spotify(auth_manager = auth_manager)


# - - - - - Finding Device Name - - - - - 
devices = spotify.devices()
deviceID=[]
for d in devices['devices']:
    if d['name'] == spotify_config.device_name:
        deviceID = d['id']
        break


# - - - - - Getting Track uri from search - - - - - 
def get_track_uri(spotify: sp.Spotify, artist, track) -> str:
    #query = str(format:"artist:%@ track:%@", artist , track)
    query = f"artist: {artist} track: {track}"
    results = spotify.search(q=query, limit=1, type ="artist,track")
    #print(results)
    track_uri = results["tracks"]["items"][0]["uri"]
    return track_uri






# - - - - - Spotify Commands - - - - - 
def play(artist, track):
    device_id = deviceID
    uri = get_track_uri(spotify=spotify, artist=artist, track=track)
    spotify.add_to_queue(uri, device_id=device_id)

def skip():
    device_id = deviceID
    spotify.next_track(device_id=device_id)

def previous():
    device_id = deviceID
    spotify.previous_track(device_id=device_id)

def song():
    current = spotify.currently_playing()
    artist_name = current['item']['album']['artists'][0]['name']
    song_name = current['item']['name']
    string = f"{artist_name} - '{song_name}'"

    return string

    # info = spotify.current_user_playing_track()
    # track_name = 
    # print(f"{track_name}")

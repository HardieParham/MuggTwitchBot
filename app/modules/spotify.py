# Standard Imports
import logging

# External Imports
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

# Local Imports
from app.config import spotify_config


class Sp:
    def __init__(self):
        self.client_id = spotify_config.client_id
        self.client_secret = spotify_config.client_secret
        self.device_name = spotify_config.device_name
        self.redirect_uri = spotify_config.redirect_uri
        self.scope = spotify_config.scope
        self.username = spotify_config.username

        self.auth_manager = SpotifyOAuth(
            client_id = self.client_id,
            client_secret = self.client_secret,
            redirect_uri = self.redirect_uri,
            scope = self.scope,
            username = spotify_config.username)

        try:
            self.spotify = sp.Spotify(auth_manager = self.auth_manager)
        except:
            logging.warning('Spotify failed to load')



        self.devices = self.spotify.devices()
        self.deviceID=[]
        for d in self.devices['devices']:
            if d['name'] == spotify_config.device_name:
                self.deviceID = d['id']
                break


# - - - - - Finding Device Name - - - - - 
# devices = spotify.devices()
# deviceID=[]
# for d in devices['devices']:
#     if d['name'] == spotify_config.device_name:
#         deviceID = d['id']
#         break


# - - - - - Getting Track uri from search - - - - - 
    def get_track_uri(spotify: sp.Spotify, artist, track) -> str:
        #query = str(format:"artist:%@ track:%@", artist , track)
        query = f"artist: {artist} track: {track}"
        results = spotify.search(q=query, limit=1, type ="artist,track")
        #print(results)
        track_uri = results["tracks"]["items"][0]["uri"]
        return track_uri


    def play(self, artist, track):
        device_id = self.deviceID
        uri = self.get_track_uri(spotify=self.spotify, artist=artist, track=track)
        self.spotify.add_to_queue(uri, device_id=device_id)

    def skip(self):
        device_id = self.deviceID
        self.spotify.next_track(device_id=device_id)

    def previous(self):
        device_id = self.deviceID
        self.spotify.previous_track(device_id=device_id)

    def song(self):
        current = self.spotify.currently_playing()
        artist_name = current['item']['album']['artists'][0]['name']
        song_name = current['item']['name']
        string = f"{artist_name} - '{song_name}'"

        return string

        # info = spotify.current_user_playing_track()
        # track_name = 
        # print(f"{track_name}")

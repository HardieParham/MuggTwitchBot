import spotipy as sp

from ..config.spotify_config import spotify_config
from spotipy.oauth2 import SpotifyOAuth


"""Applying Configuration Settings""" 
device_name = spotify_config['DEVICE_NAME']
auth_manager = SpotifyOAuth(
    client_id = spotify_config['CLIENT_ID'],
    client_secret = spotify_config['CLIENT_SECRET'],
    redirect_uri = spotify_config['REDIRECT_URI'],
    scope = spotify_config['SCOPE'],
    username = spotify_config['USERNAME'],
    )


"""Connecting to Spotify and finding playing device"""
spotify = sp.Spotify(auth_manager = auth_manager) 
devices = spotify.devices()
deviceID=[]
for d in devices['devices']:
    if d['name'] == device_name:
        deviceID = d['id']
        break


def get_track_uri(spotify: sp.Spotify, artist: str, track: str) -> str:
    query = f"artist: {artist} track: {track}"
    results = spotify.search(q=query, limit=1, type ="artist,track")
    track_uri = results["tracks"]["items"][0]["uri"]
    return track_uri


def connect() -> bool | Exception:
    if spotify is not None:
        return True
    else:
        raise Exception('ModuleFailure')



"""Spotify commands for the Command Bot"""
def play(artist: str, track: str) -> None:
    tries = 0
    device_id = deviceID
    while tries < 5:
        try:
            uri = get_track_uri(spotify=spotify, artist=artist, track=track)
            break
        except:
            tries += 1
    spotify.add_to_queue(uri, device_id=device_id)


def skip() -> None:
    device_id = deviceID
    spotify.next_track(device_id=device_id)


def previous() -> None:
    device_id = deviceID
    spotify.previous_track(device_id=device_id)


def song() -> str:
    current = spotify.currently_playing()
    artist_name = current['item']['album']['artists'][0]['name']
    song_name = current['item']['name']
    string = f"{artist_name} - '{song_name}'"
    return string


def artist() -> str:
    current = spotify.currently_playing()
    artist_id = current['item']['album']['artists'][0]['id']
    artist = spotify.artist(artist_id)
    list = spotify.artist_top_tracks(artist_id)

    def song(id: str) -> str:
        song = list['tracks'][int(id)]['name']
        return song

    text = f"ARTIST: {artist['name']}. TOP SONGS: 1. {song(0)} 2. {song(1)} 3. {song(2)} 4. {song(3)} 5. {song(4)}"
    return text


def song_link() -> str:
    current = spotify.currently_playing()
    song_link = current['item']['external_urls']['spotify'] 
    return song_link


def song_queue() -> str:
    list = spotify.queue()
    num = int(len(list['queue']))
    
    def track(id: str) -> str:
        artist = list['queue'][int(id)]['album']['artists'][0]['name']
        song = list['queue'][int(id)]['name']
        return f"{artist} - '{song}'"

    if num == 0:
        text = 'There are no songs in the queue'
        return text

    elif num > 0 and num < 5:
        id = 0
        text = ''
        while id < num:
            text += f"{id+1}: {track(id)}.  "
            id += 1
        return text

    else:
        id = 0
        text = ''
        while id < 5:
            text += f"{id+1}: {track(id)}.  "
            id += 1
        text += f"and {num-id} more..."
        return text


def set_volume(num: int) -> None:
    spotify.volume(num)


def sp_search(query: str) -> None:
    x = query.split("-")
    artist = x[0]
    song = x[1]
    play(artist = artist, track= song)
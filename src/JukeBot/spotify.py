"""Enables Spotify search integration for JukeBot. Requires a separate set
of Spotify application tokens in order to function."""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import JukeBot
import json

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=JukeBot.config.SPOTIPY_CLIENT_ID,
                                                           client_secret=JukeBot.config.SPOTIPY_CLIENT_SECRET))


def track_or_playlist(url):
    return url.split("?")[0].split("/")[3:][0]


def playlist_info(url):
    info = sp.playlist(url, fields="name, images, external_urls")
    return {"title": info["name"],
            "web_url": info["external_urls"]["spotify"],
            "thumb": info["images"][0]["url"]}


def get_track_name(track_data):
    artists = "".join(f"{a['name']} " for a in track_data["artists"])
    title = track_data["name"]
    return(f"{artists}{title}".title())


def spotify_to_search(spotify_link):
    """Takes a Spotify link for a track or playlist and extracts the track
    names and artists. This will later be used to search YouTube.
    """
    link_type, link_id = spotify_link.split("?")[0].split("/")[3:]  # fucked
    if link_type != "track" and link_type != "playlist":
        return False
    if link_type == "track":
        track_info = sp.track(link_id)
        print(json.dumps(track_info, indent=4))
        return [get_track_name(track_info), track_info["album"]["images"][1]["url"]]
    if link_type == "playlist":
        track_list = []
        for track_info in sp.playlist_items(link_id, fields="items.track.artists, items.track.name, items.track.album")["items"]:
            print(json.dumps(track_info, indent=4))
            track_list.append([get_track_name(track_info["track"]), track_info["track"]["album"]["images"][1]["url"]])
        return track_list

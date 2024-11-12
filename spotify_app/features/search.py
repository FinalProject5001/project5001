
from spotify_app.authorization import get_auth_header, get_token
from requests import get
import json

# Search for artists, tracks, or albums
def search():
    def search_for_artist(token, artist_name, limit=50, offset=0):
        url = "https://api.spotify.com/v1/search"
        headers = get_auth_header(token)
        query = {"q": artist_name, "type": "artist", "limit": limit, "offset": offset}

        response = get(url, headers=headers, params=query)
        if response.status_code == 200:
            json_result = response.json()["artists"]["items"]
            if len(json_result) == 0:
                return []
            return json_result
        else:
            return {"error": response.status_code, "message":response.reason}

    def search_for_tracks(token, track_name, limit=50, offset=0):
        url = "https://api.spotify.com/v1/search"
        headers = get_auth_header(token)
        params = {"q": track_name, "type": "track", "limit": limit, "offset": offset}

        response = get(url, headers=headers, params=params)
        if response.status_code == 200:
            json_result = response.json()["tracks"]["items"]
            # The JSON response contains relevant information about tracks such as album, artist(s), etc.
            return json_result
        else:
            return {"error": response.status_code, "message": response.reason}


    def search_for_albums(token, album_name, limit=50, offset=0):
        url = "https://api.spotify.com/v1/search"
        headers = get_auth_header(token)
        params = {"q": album_name, "type": "album", "limit": limit, "offset": offset}

        response = get(url, headers=headers, params=params)
        if response.status_code == 200:
            json_result = response.json()["albums"]["items"]
            return json_result
        else:
            return {"error": response.status_code, "message": response.reason}

    return {
        "search_for_artist": search_for_artist,
        "search_for_tracks": search_for_tracks,
        "search_for_albums": search_for_albums
    }

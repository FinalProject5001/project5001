import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_top_tracks_by_country(country_name, client_id, client_secret):
    # Replace the following with your client_id and client_secret
    client_id = client_id
    client_secret = client_secret

    # Authentication
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Search for the Top 50 playlist of the country
    results = sp.search(q=f'Top 50 - {country_name}', type='playlist', limit=1)
    playlists = results['playlists']['items']

    if not playlists:
        print(f"Top 50 playlist for {country_name} not found.")
        return

    playlist_id = playlists[0]['id']

    # Get the tracks from the playlist
    tracks = sp.playlist_items(playlist_id, limit=10)
    top_tracks = tracks['items']

    # Output song information
    for idx, item in enumerate(top_tracks, 1):
        track = item['track']
        print(f"{idx}. {track['name']} - {', '.join(artist['name'] for artist in track['artists'])}")

if __name__ == "__main__":
    country = input("Please enter the country name (e.g., Global, USA, Japan): ")
    get_top_tracks_by_country(country, client_id, client_secret)

import os
import spotipy
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

while True:
    date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        is_date_format_correct = bool(datetime.strptime(date_input, "%Y-%m-%d"))
        if is_date_format_correct:
            break
    except ValueError:
        print("Oops! Look's like the date was not in the correct format! Try, again.")

html = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{date_input}/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
).text

soup = BeautifulSoup(html, "html.parser")
titles = [title_heading.getText().strip() for title_heading in soup.select(selector="ul li #title-of-a-story")]

spotify_auth = SpotifyOAuth(client_id=os.environ.get("CLIENT_ID"),
                            client_secret=os.environ.get("CLIENT_SECRET"),
                            redirect_uri="https://open.spotify.com/",
                            scope="playlist-modify-private",
                            cache_path=".cache")

sp = spotipy.Spotify(auth_manager=spotify_auth)

songs = []
for title_song in titles:
    result = sp.search(
        q=f"track:{title_song} year:{date_input.split("-")[0]}",
        type="track"
    )
    try:
        songs.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"The song: {title_song} could not be found.")

private_playlist = sp.user_playlist_create(
    user=sp.current_user()["id"],
    name=f"{date_input} Billboard 100",
    public=False)

sp.playlist_add_items(
    playlist_id=private_playlist["id"],
    items=songs)
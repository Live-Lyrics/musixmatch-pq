import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq

ua = UserAgent()


def get_url(artist, song, headers):
    resp = requests.get(f"https://www.musixmatch.com/search/{artist} - {song}", headers=headers)
    doc = pq(resp.text)
    url = doc(".title:first").attr("href")
    return url


def fetch_lyrics(artist, song):
    headers = {'User-Agent': ua.random}
    url = get_url(artist, song, headers)
    resp = requests.get(f"https://www.musixmatch.com{url}", headers=headers)

    doc = pq(resp.text)
    lyrics = []
    for i in doc("p.mxm-lyrics__content "):
        lyrics.append(i.text)
    return "".join(lyrics)

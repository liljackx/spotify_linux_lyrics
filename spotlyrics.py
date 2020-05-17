#!/usr/bin/env python3

import dbus
import time
from libs.api import Genius
from selenium import webdriver

TOKEN = ""

session = dbus.SessionBus()
genius = Genius(TOKEN)
driver = webdriver.Firefox()

def get_url(track_name, artist_name):
	song_url = genius.get_url_from_search(track_name, artist_name)
	return song_url

def read_spotify_data():
	spotifydbus = session.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
	spotifyinterface = dbus.Interface(spotifydbus, "org.freedesktop.DBus.Properties")
	metadata = spotifyinterface.Get("org.mpris.MediaPlayer2.Player", "Metadata")
	return metadata

def on_change():
	first = True
	oldsongname = ""
	while True:
		songname = read_spotify_data()['xesam:title']

		if oldsongname != songname:
			data = read_spotify_data()
			artist_name = data['xesam:artist'][0]
			title = data['xesam:title']

			song_url = get_url(title, artist_name)

			if first:
				driver.get(song_url)
			else:
				driver.refresh()
		
			print(f'Artist name: {artist_name}')
			print(f'Title: {title}')	
			oldsongname = songname


if __name__ == '__main__':
	
	on_change()

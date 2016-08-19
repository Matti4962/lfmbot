#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from keys import apikey
from keys import apisecret
from keys import lastfmu
from keys import lastfmp 
import os
import pylast
import sys

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm

try:
    API_KEY = os.environ[apikey]
    API_SECRET = os.environ[apisecret]
except KeyError:
    API_KEY = apikey
    API_SECRET = apisecret

try:
    lastfm_username = os.environ[lastfmu]
    lastfm_password_hash = os.environ[lastfmp]
except KeyError:
    # In order to perform a write operation you need to authenticate yourself
    lastfm_username = lastfmu
    # You can use either use the password, or find the hash once and use that
    lastfm_password_hash = pylast.md5(lastfmp)
    print(lastfm_password_hash)
    # lastfm_password_hash = "my_password_hash"


lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY, api_secret=API_SECRET,
    username=lastfm_username, password_hash=lastfm_password_hash)


# Windows cmd.exe cannot do Unicode so encode first
def print_it(text):
    print(text.encode('utf-8'))


def unicode_track_and_timestamp(track):
    unicode_track = unicode(str(track.track), 'utf8')
    return track.playback_date + "\t" + unicode_track


def print_track(track):
    print_it(unicode_track_and_timestamp(track))

TRACK_SEPARATOR = u" - "


def split_artist_track(artist_track):
    artist_track = artist_track.replace(u" – ", " - ")
    artist_track = artist_track.replace(u"“", "\"")
    artist_track = artist_track.replace(u"”", "\"")

    (artist, track) = artist_track.split(TRACK_SEPARATOR)
    artist = artist.strip()
    track = track.strip()
    print_it("Artist:\t\t'" + artist + "'")
    print_it("Track:\t\t'" + track + "'")

    # Validate
    if len(artist) is 0 and len(track) is 0:
        sys.exit("Error: Artist and track are blank")
    if len(artist) is 0:
        sys.exit("Error: Artist is blank")
    if len(track) is 0:
        sys.exit("Error: Track is blank")
 
    return (artist, track)

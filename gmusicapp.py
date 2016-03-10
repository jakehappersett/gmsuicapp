#!/usr/bin/env python
#version 0.1
#-*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *  # noqa
from getpass import getpass

from gmusicapi import Mobileclient
import pprint
import curses
def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2,2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def ask_for_credentials():
    """Make an instance of the api and attempts to login with it.
    Return the authenticated api.
    """

    # We're not going to upload anything, so the Mobileclient is what we want.
    api = Mobileclient()

    logged_in = False
    attempts = 0

    while not logged_in and attempts < 3:
        screen.clear()
	screen.border(0)
	screen.refresh()
	
	email = get_param('Email: ')
	password = get_param('Password: ')

        logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
        attempts += 1

    return api

def listartists():

        """list all the artists"""

        api = ask_for_credentials()

        if not api.is_authenticated():
                print("sorry, those credentials weren't accepted.")
                return
        print('Successfully logged in.')
        print()

        #load library
        print('Loading library...', end=' ')
        library = api.get_all_songs()
        print('done.')

        #artists  list
        artists_list = []
        artists = []

        #song list 
        song_list = []
        songs = []
        #song library
        for i in library:
                if i['song'] not in song_list:
                        song_list.append(i['song'])
        #artist library
        for i in library:
                if i['artist'] not in artists_list:
                        artists_list.append(i['artist'])
        #convert to ascii
        for i in artists_list:
                j = i.encode('ascii')
                artists.append(j)
        for i in song_list:
                j = i.encode('ascii')
                songs.append(j)
        artists_list.sort()
        pprint.pprint(artists)


#main 

x = 0

while x != ord('2'):
	screen = curses.initscr()
	
	screen.clear()
	screen.border(0)
	screen.addstr(2, 4, "1 - login")
	screen.addstr(4, 4, "2 - quit")
	screen.refresh()
	x = screen.getch()

	if x == ord('1'):
		listartists()
	elif x == ord('2'):
		curses.endwin()

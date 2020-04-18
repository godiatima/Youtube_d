#!/usr/bin/python3 

import webbrowser

url = 'http://www.youtube.com/'

# Linux
firefox_path = '/usr/local/bin/firefox'

webbrowser.get(firefox_path).open(url)
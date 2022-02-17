#(C) Grizz Co. Industries  - All rights reserved (C - GRIZZ CO. INDUSTRIES) - 2022
# (C)  - Haltmann Works Company (2099) - All rights reserved (C - HALTMANN WORKS COMPANY) - 2022
# (This is the hq haltmann grizz co figment ripper) by octo id software

print ("Welcome to the HQVipper1.0b.py")
print ("This is the hq haltmann grizz co figment ripper")
print ("by octo id software")
print ("")
 # use the google api to get youtube links
import urllib.request
import json
import time
import urllib.parse
import os
 
import urllib.parse as p
import re
import os
import pickle
import time
import sys
import argparse
import os

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

## import the google api

import google_auth_oauthlib.flow
import googleapiclient.errors
## write a gui app that will allow the user to enter the artist and track name and then rip the song
## use the google api to get youtube links
print("importing google api")   
## import the google api
 
## download the youtube url tracks of 2-10 songs of your choice
## use the google api to get youtube links
print('LOADING CLIENT SECRETS FILE')
os.system('python3 -m pip install --upgrade google-api-python-client')
os.system('python3 -m pip install --upgrade google-auth-httplib2')
### download the mp3 tracks and save them to your documents that you select from two songs of your choice
## verify if youtube-dl is there and if not install it
os.system('python3 -m pip install --upgrade youtube-dl')
DEF = os.path.expanduser("~")
print("")
print("")
## GET TOKEN OF RANDOM YOUTUBE id
## make a stsatement to check if ffmpeg and youtube-dl are installed
print("checking if youtube-dl is installed")
if os.system('youtube-dl --version') == 0:
    print("youtube-dl is installed")
else:
    print("youtube-dl is not installed")
    print("installing youtube-dl")
    os.system('python3 -m pip install --upgrade youtube-dl')
    print("youtube-dl installed")
print("")
print("Done")
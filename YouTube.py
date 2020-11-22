import os
from googleapiclient.discovery import build
import pandas as pd
youTubeApikey="AIzaSyDvLvhGHV2SKwLMY3Y3saDN4YRGgDa_JKs"
youtube=build( 'youtube', 'v3' ,developerKey=youTubeApikey )
stats = youtube.channels().list(part="snippet,contentDetails,statistics,brandingSettings,localizations", id ='UCPPZ8FnXyhvUy2RWrjPcjcg').execute()
print(stats['items'])
stats = youtube.channels().list(part="snippet,contentDetails,statistics,brandingSettings,localizations", id ='UCSTBpjukawEv6ZUmH6l-ibw').execute()
print(stats['items'])
stats = youtube.channels().list(part="snippet,contentDetails,statistics,brandingSettings,localizations", id ='UCc4ucYAsnKOXypwTXoo3PSg').execute()
print(stats['items'])



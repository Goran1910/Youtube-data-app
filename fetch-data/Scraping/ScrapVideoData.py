import requests
import json
import datetime
from Entity.Video import Video

class ScrapVideoData:
    def __init__(self, apiKey):    
        self.apiKey = apiKey
        self.limit = 50
        self.url = f'https://www.googleapis.com/youtube/v3/videos?key={self.apiKey}&maxResults={self.limit}'
        self.video = Video()
        
    def scrapDataSnippet(self, videoId):
        url = self.url + '&id=' + videoId + '&part=snippet'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        
        try:
            stavke = data['items']
        except:
            print('greska')
            
        snippet = stavke[0]['snippet']
        dateString = snippet['publishedAt']
        date = self._formatDate(dateString)
        
        self.video.setDate(date)
        self.video.setTitle(snippet['title'])
        self.video.setThumbnail(snippet['thumbnails']['standard']['url'])
        
        
        
    def scrapDataStatistics(self, videoId):
        url = self.url + '&id=' + videoId +'&part=statistics'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
    
        try:
            stavke = data['items']
        except:
            print('greska')
            
        stat = stavke[0]['statistics']
        self.video.setViews(int(stat['viewCount']))
        self.video.setLikes(int(stat['likeCount']))
        self.video.setDislikes(int(stat['dislikeCount']))
        self.video.setComments(int(stat['commentCount']))
        
    def scrapDataContentDetails(self, videoId):
        url = self.url + '&id=' + videoId + '&part=contentDetails'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
    
        try:
            stavke = data['items']
        except:
            print('greska')
            
        durationMessy = stavke[0]['contentDetails']['duration']
        duration = self._formatDuration(durationMessy)
        
        self.video.setDuration(duration)
        
    def _formatDate(self, dateString):
        componenets = dateString[:10].split('-')
        date = datetime.datetime(int(componenets[0]), int(componenets[1]), int(componenets[2]))
        return date
    
    def _formatDuration(self, durationMessy):
        seconds = 0
        print(durationMessy)
        durationMessy = durationMessy[2:]
        if durationMessy.find('H') != -1:
            durationMessy = durationMessy.split('H')
            seconds += int(durationMessy[0]) * 3600
            durationMessy = durationMessy[1]
            
        if durationMessy.find('M') != -1:
            durationMessy = durationMessy.split('M')
            seconds += int(durationMessy[0]) * 60
            durationMessy = durationMessy[1]
            
        if durationMessy.find('S') != -1:
            seconds += int(durationMessy.split('S')[0])
            
        return seconds
        
    def _getChannelName(self, channelId):
        url = f'https://www.googleapis.com/youtube/v3/channels?key={self.apiKey}&id={channelId}&part=snippet'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            stavke = data['items']
        except:
            print('greska')
            
        return stavke[0]['snippet']['title']
        
        
#%%
import datetime
date = datetime.datetime(1999, 10, 19)
print(date.strftime("%Y-%m-%d"))

        
    
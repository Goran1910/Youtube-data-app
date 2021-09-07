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
        
    def scrap_data_snippet(self, videoId):
        url = self.url + '&id=' + videoId + '&part=snippet'
        data = self._fetch_data(url)
        try:
            items = data['items']
        except:
            print('error video snippet')
            return
            
        snippet = items[0]['snippet']
        date_string = snippet['publishedAt']
        date = self._format_date(date_string)
        self.video.setDate(date)
        self.video.setTitle(snippet['title'])
        self.video.setThumbnail(snippet['thumbnails']['standard']['url'])
        
        
    def scrap_data_statistics(self, videoId):
        url = self.url + '&id=' + videoId +'&part=statistics'
        data = self._fetch_data(url)
        try:
            items = data['items']
        except:
            print('error video statistics')
            return
            
        stat = items[0]['statistics']
        self.video.setViews(int(stat['viewCount']))
        self.video.setLikes(int(stat['likeCount']))
        self.video.setDislikes(int(stat['dislikeCount']))
        self.video.setComments(int(stat['commentCount']))
        
    def scrap_data_content_details(self, videoId):
        url = self.url + '&id=' + videoId + '&part=contentDetails'
        data = self._fetch_data(url)
        try:
            items = data['items']
        except:
            print('error video content details')
            return
            
        duration_messy = items[0]['contentDetails']['duration']
        duration = self._format_duration(duration_messy)
        self.video.setDuration(duration)
        
        
    def _format_date(self, date_string):
        componenets = date_string[:10].split('-')
        date = datetime.datetime(int(componenets[0]), int(componenets[1]), int(componenets[2]))
        return date
    
    def _format_duration(self, duration_messy):
        seconds = 0
        duration_messy = duration_messy[2:]
        if duration_messy.find('H') != -1:
            duration_messy = duration_messy.split('H')
            seconds += int(duration_messy[0]) * 3600
            duration_messy = duration_messy[1]
            
        if duration_messy.find('M') != -1:
            duration_messy = duration_messy.split('M')
            seconds += int(duration_messy[0]) * 60
            duration_messy = duration_messy[1]
            
        if duration_messy.find('S') != -1:
            seconds += int(duration_messy.split('S')[0])
            
        return seconds
        
    def _get_channel_name(self, channelId):
        url = f'https://www.googleapis.com/youtube/v3/channels?key={self.apiKey}&id={channelId}&part=snippet'
        data = self._fetch_data(url)
        try:
            items = data['items']
        except:
            print('error video get channel name')
            return
            
        return items[0]['snippet']['title']
    
    def _fetch_data(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        return data
        
        
    
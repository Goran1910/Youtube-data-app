import requests
import json
from Entity.Channel import Channel

class ScrapChannelData:
    
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.base_url = f'https://www.googleapis.com/youtube/v3/channels?key={api_key}&id={channel_id}'
        self.channel = Channel()
        self.channel.id = channel_id
        
    def scrap_snippet_data(self):
        url = self.base_url + '&part=snippet'
        data = self._fetch_data(url)
        try:
            items = data['items']
        except:
            print('error channel snippet')
            return 
        snippet = items[0]['snippet']
        self.channel.title = snippet['title']
        self.channel.thumbnail_url = snippet['thumbnails']['high']['url']
        
    def scrap_statistics(self):
        url = self.base_url + '&part=statistics'
        data = self._fetch_data(url)
        try:
            items = data['items']
        except:
            print('error channel statistics')
            return
        statistics = items[0]['statistics']
        self.channel.subscriber_count = statistics['subscriberCount']
        self.channel.video_count = statistics['videoCount']
        
    def _fetch_data(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        return data
        
        
        
        
        
        
        
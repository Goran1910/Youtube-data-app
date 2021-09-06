from Scraping.ScrapVideoData import ScrapVideoData
from Entity.Playlist import Playlist
import requests
import json
import copy

class ScrapPlaylistData:
    
    def __init__(self, api_key, id, title, channel_title):
        self.api_key = api_key
        self.playlist = Playlist(title, id, '', channel_title)
        self.scrapVideoData = ScrapVideoData(api_key)
        self.limit = 5
        self.maxAttempts = 10
        
    def scrap_data(self):
        ids = self._getVideosIds()
        for id in ids:
            self.scrapVideoData.scrapDataSnippet(id)
            self.scrapVideoData.scrapDataContentDetails(id)
            self.scrapVideoData.scrapDataStatistics(id)
            self.scrapVideoData.video.setPlaylistName(self.playlist.title)
            self.playlist.videos.append(copy.deepcopy(self.scrapVideoData.video))
        
        
    def _getVideosIds(self):
        ids = []
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={self.playlist.id}&key={self.api_key}&maxResults={self.limit}'
        idsFromPage, npt = self._getVideosIdsPerPage(url)
        ids.extend(idsFromPage)
        currentAttempt = 0
        
        while npt is not None and currentAttempt < self.maxAttempts:
            idsFromPage, npt = self._getVideosIdsPerPage(url + '&pageToken=' + npt)
            ids.extend(idsFromPage)
            currentAttempt += 1
            
        return ids
            
    def _getVideosIdsPerPage(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        ids = []
        npt = data.get('nextPageToken', None)
        
        try: 
            stavke = data['items']
        except:
            print('nema stavki')
            
        for stavka in stavke:
            ids.append(stavka['contentDetails']['videoId'])
        
        return ids, npt
    
    def get_playlists_thumbnail(self):
        url = f'https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={self.playlist.id}&key={self.api_key}'
        data = self._fetch_data(url)  
        try:
            items = data['items']
        except:
            print('error get thumbnails')
            return
            
        snippet = items[0]['snippet']    
        self.playlist.thumbnail_url = snippet['thumbnails']['standard']['url']
        
    def _fetch_data(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        return data
        
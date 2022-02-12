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
        self.max_attempts = 10
        
    def scrap_data(self):
        ids = self._get_videos_ids()
        for id in ids:
            self.scrapVideoData.scrap_data_snippet(id)
            self.scrapVideoData.scrap_data_content_details(id)
            self.scrapVideoData.scrap_data_statistics(id)
            self.scrapVideoData.video.playlist_id = self.playlist.id
            self.playlist.videos.append(copy.deepcopy(self.scrapVideoData.video))
        
        
    def _get_videos_ids(self):
        ids = []
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={self.playlist.id}&key={self.api_key}&maxResults={self.limit}'
        idsFromPage, npt = self._get_videos_ids_per_page(url)
        ids.extend(idsFromPage)
        current_attempt = 0
        
        while npt is not None and current_attempt < self.max_attempts:
            ids_from_page, npt = self._get_videos_ids_per_page(url + '&pageToken=' + npt)
            ids.extend(ids_from_page)
            current_attempt += 1
            
        return ids
            
    def _get_videos_ids_per_page(self, url):
        data = self._fetch_data(url)
        ids = []
        npt = data.get('nextPageToken', None)
        try: 
            items = data['items']
        except:
            print('error videos ids')
            return
        for item in items:
            ids.append(item['contentDetails']['videoId'])
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
        
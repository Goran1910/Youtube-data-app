from Entity.Modes import Modes

class Playlist:
    
    def __init__(self, title, id, thumbnail_url, channel_title):
        self.title = title
        self.id = id
        self.channel_title = channel_title
        self.thumbnail_url = thumbnail_url
        self.videos = []
        
    def toList(self):
        return [self.name, self._calculateViews(), self._calculateViewsPerVideo(),
                self._calculateLikes(), self._calculateDislikes(), self._calculateComments()]
    
    def to_tuple(self, mode):   
        if mode == Modes.CREATE:    
            return (self.title, self.id, self.thumbnail_url, self.channel_title)     
        if mode == Modes.UPDATE:
            return (self.title, self.id, self.thumbnail_url, self.channel_title, self.title) 
    
    
    
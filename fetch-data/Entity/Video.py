import datetime

class Video:
    
    def __init__(self):
        self.title = ''
        self.views = 0
        self.likes = 0
        self.dislikes = 0
        self.comments = 0
        self.date = datetime.datetime(1, 1, 1)
        self.playlist_id = ''
        self.duration = 0
        self.thumbnail = ''
        
    def to_tuple(self, additional=None):
        if additional:
            return (self.title, self.playlist_id, self.views, self.likes,
                    self.dislikes, self.comments, self.date, self.duration, self.thumbnail, additional)   
        return (self.title, self.playlist_id, self.views, self.likes,
                    self.dislikes, self.comments, self.date, self.duration, self.thumbnail)
        
    def toList(self):
        if self.playlistName:
            return [self.name, self.playlist_id, self.views, self.duration,
                    self.likes, self.dislikes, self.comments, self.date]    
        return [self.name, self.views, self.duration, self.likes,
                self.dislikes, self.comments, self.date]
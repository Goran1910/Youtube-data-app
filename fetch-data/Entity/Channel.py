from Entity.Modes import Modes

class Channel:
    
    def __init__(self):
        self.id = ''
        self.title = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.thumbnail_url = ''
        
    def to_tuple(self, mode):   
        if mode == Modes.CREATE:    
            return (self.title, self.subscriber_count, self.thumbnail_url, self.id, self.video_count)     
        if mode == Modes.UPDATE:
            return (self.title, self.subscriber_count, self.thumbnail_url, self.id, self.video_count, self.title) 
        
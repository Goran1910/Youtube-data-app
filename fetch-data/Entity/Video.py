class Video:
        
    def setTitle(self, title):
        self.title = title
        
    def setViews(self, views):
        self.views = views
        
    def setLikes(self, likes):
        self.likes = likes
        
    def setDislikes(self, dislikes):
        self.dislikes = dislikes
        
    def setDate(self, date):
        self.date = date
        
    def setComments(self, comments):
        self.comments = comments
        
    def setPlaylistName(self, playlistName):
        self.playlistName = playlistName
        
    def setDuration(self, duration):
        self.duration = duration
    
    def setThumbnail(self, thumbnail):
        self.thumbnail = thumbnail
        
    def to_tuple(self, additional=None):
        if additional:
            
            return (self.title, self.playlistName, self.views, self.likes,
                    self.dislikes, self.comments, self.date, self.duration, self.thumbnail, additional)
        
        return (self.title, self.playlistName, self.views, self.likes,
                    self.dislikes, self.comments, self.date, self.duration, self.thumbnail)
        
    def toList(self):
        if self.playlistName:
            return [self.name, self.playlistName, self.views, self.duration,
                    self.likes, self.dislikes, self.comments, self.date]
        
        return [self.name, self.views, self.duration, self.likes,
                self.dislikes, self.comments, self.date]
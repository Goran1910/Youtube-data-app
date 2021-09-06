import openpyxl

class ExcelRepo:
    
    def __init__(self):
        self.fileName = 'Metallica.xlsx'
        self.wb = openpyxl.load_workbook(filename = self.fileName)
    
    def saveVideos(self, playlist):
        print(playlist)
        ws = self.wb['Jack O\'Shae']
        for v in playlist:
            ws.append([v.name, v.views, v.likes,
                      v.dislikes, v.date[:10], v.comments])
            
        self.wb.save(self.fileName)
        
    def savePlaylist(self, playlist):
        print(playlist)
        ws = self.wb['Most viewed']
        for v in playlist.videos:
            ws.append([v.name, v.views, v.likes,
                      v.dislikes, v.date[:10], v.comments])
            
        self.wb.save(self.fileName)
        

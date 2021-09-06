from Repository.MySQLRepository import MySQLRepository
from Entity.Modes import Modes

class MySQLPlaylistRepository(MySQLRepository):
    
    def add_playlist(self, playlist):
        sql = 'insert into playlist(title, id, thumbnail_url, channel_title) values(%s, %s, %s, %s)'
        val = playlist.to_tuple(Modes.CREATE)
        self._prepare_query_execution(sql, val)
        self._save_query(playlist)

    def update_playlist(self, playlist):
        sql = 'update playlist set title = %s, id = %s, thumbnail_url = %s, channel_title = %s where title = %s'
        val = playlist.to_tuple(Modes.UPDATE)
        self._prepare_query_execution(sql, val)

    def _prepare_query_execution(self, query, value):
        mycursor = self.mydb.cursor()
        mycursor.execute(query, value)        
        self.mydb.commit()
        
    def get_playlists(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT id, title, channel_title FROM playlist")
        playlists = mycursor.fetchall()
        return playlists
    
    def _save_query(self, playlist):
        sql = 'insert into playlist(title, id, thumbnail_url, channel_title) '
        query = sql + f'values("{playlist.title}", "{playlist.id}", "{playlist.thumbnail_url}", "{playlist.channel_title}");\n'
        with open('queries.sql', 'a') as f:
            f.write(query)
    
    
    
    
    
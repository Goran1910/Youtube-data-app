from Repository.MySQLRepository import MySQLRepository
from Entity.Modes import Modes

class MySQLChannelRepository(MySQLRepository):
 
    def add_channel(self, channel):
        sql = 'insert into channel(title, subscriber_count, thumbnail_url, id, video_count) values(%s, %s, %s, %s, %s)'
        val = channel.to_tuple(Modes.CREATE)
        self._prepare_query_execution(sql, val)

    def update_channel(self, channel):
        sql = 'update channel set title = %s, subscriber_count = %s, thumbnail_url = %s, id = %s, video_count = %s where title = %s'
        val = channel.to_tuple(Modes.UPDATE)
        self._prepare_query_execution(sql, val)

    def _prepare_query_execution(self, query, value):
        mycursor = self.mydb.cursor()
        mycursor.execute(query, value)        
        self.mydb.commit()
        
    def get_all_channel_ids(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT id FROM channel")
        ids = mycursor.fetchall()
        return [id[0] for id in ids]
        
        
        
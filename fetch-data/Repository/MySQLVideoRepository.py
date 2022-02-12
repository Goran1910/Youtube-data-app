from Repository.MySQLRepository import MySQLRepository

class MySQLVideoRepository(MySQLRepository):
         
    def save_videos(self, videos):
        sql = 'insert into video(title, playlist_id, views, likes, dislikes, comments, published_at, duration, thumbnail_url) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = [video.to_tuple() for video in videos]
        self._prepare_query_execution(sql, val)
        #self._save_query(videos)
        print(f'videos from {videos[0].playlist_id} are added!')
 
    def update_videos(self, videos):
        sql = 'update video set title = %s, playlist_id = %s, views = %s, likes = %s, dislikes = %s, comments = %s, published_at = %s, duration = %s, thumbnail_url = %s where title = %s'
        val = [video.to_tuple(video.id) for video in videos]
        self._prepare_query_execution(sql, val)
        print(f'videos from {videos[0].playlistName} are updated!')
   
    def _prepare_query_execution(self, query, value):
        mycursor = self.mydb.cursor()
        mycursor.executemany(query, value)        
        self.mydb.commit()
        
    def _save_query(self, videos):
        sql = 'insert into video(title, playlist_id, views, likes, dislikes, comments, published_at, duration, thumbnail_url) '
        queries = []
        for video in videos:   
            queries.append(sql + f'values("{video.title}", "{video.playlistName}", {video.views}, {video.likes}, {video.dislikes}, {video.comments}, "{video.date.strftime("%Y-%m-%d")}", {video.duration}, "{video.thumbnail}");\n')
            
        with open('queries.sql', 'a') as f:
            f.writelines(queries)
            
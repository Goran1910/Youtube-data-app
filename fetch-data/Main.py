from Scraping.ScrapPlaylistData import ScrapPlaylistData
from Scraping.ScrapChannelData import ScrapChannelData
from Repository.MySQLChannelRepository import MySQLChannelRepository
from Repository.MySQLPlaylistRepository import MySQLPlaylistRepository
from Repository.MySQLVideoRepository import MySQLVideoRepository

API_KEY = 'AIzaSyBEm8gr25qWZp5Q23e32uh4bxn-8WAC1Nw'

def add_channel(channel_id):
    scd = ScrapChannelData(API_KEY, channel_id)
    scd.scrap_snippet_data()
    scd.scrap_statistics()
    repo = MySQLChannelRepository()
    repo.add_channel(scd.channel)
    
def update_channels():
    repo = MySQLChannelRepository()
    ids = repo.get_all_channel_ids()
    for id in ids:
        scd = ScrapChannelData(API_KEY, id)
        scd.scrap_snippet_data()
        scd.scrap_statistics()
        repo.update_channel(scd.channel)
        
def add_playlist(id, title, channel_title):
    spd = ScrapPlaylistData(API_KEY, id, title, channel_title)
    spd.get_playlists_thumbnail()
    repo_playlist = MySQLPlaylistRepository()
    repo_playlist.add_playlist(spd.playlist)
    print('wait for videos to be added...')
    spd.scrap_data()
    repo_video = MySQLVideoRepository()
    repo_video.save_videos(spd.playlist.videos)

def update_playlist():
    repo_playlist = MySQLPlaylistRepository()
    playlists = repo_playlist.get_playlists()
    for playlist in playlists:
        spd = ScrapPlaylistData(API_KEY, playlist[0], playlist[1], playlist[2])
        spd.get_playlists_thumbnail()
        repo_playlist = MySQLPlaylistRepository()
        repo_playlist.update_playlist(spd.playlist)
        spd.scrap_data()
        repo_video = MySQLVideoRepository()
        repo_video.update_videos(spd.playlist.videos)
        
if __name__ == '__main__':
    add_channel('UCaisXKBdNOYqGr2qOXCLchQ')
    add_channel('UCLVz1B001PIbq9LliJenV2w')
    add_channel('UCbulh9WdLtEXiooRcYK7SWw')
    
    add_playlist('PL6ogdCG3tAWhOUeMyn8UqrBTNgonrnbs3', '...And Justice For All', 'Metallica')
    add_playlist('PLBU3rjLvn2nTAGUzCiQjgeoPl0Bl0RZeB', 'Black Album', 'Metallica')
    add_playlist('PL6vwnon3sINr_Emg1neUAZoIecAHwOjgY', 'Death Magnetic', 'Metallica')
    add_playlist('PLZ9DoO2uX9wW8zIGvcSLPHtzfKRWYNuCg', 'Hardwired... To Self-Destruct', 'Metallica')
    add_playlist('PLBnJv6rImVe_PcPIPV_iXEUcaOhMb7dYv', 'Kill ''Em All', 'Metallica')
    add_playlist('PL6vwnon3sINrOI8XVtIQDYBCqWfhqJ19d', 'Load', 'Metallica')
    add_playlist('PL6ogdCG3tAWiIOauDDXTvfTL-Gx4vz1Wt', 'Master Of Puppets', 'Metallica')
    add_playlist('PL2D4A44B959D87893', 'Official Music Video', 'Metallica')
    add_playlist('PL6vwnon3sINo-k0MMuit5J75BWd91vohX', 'Reload', 'Metallica')
    add_playlist('PL6ogdCG3tAWjkTOqqaO1JaTzaFtk6WWv4', 'Ride The Lightning', 'Metallica')
    add_playlist('PL6vwnon3sINoNaBSLoO5dEBKc6GNKYI8_', 'St. Anger', 'Metallica')
    add_playlist('PLZSpx1qgL045KdXmH3pdDT0UeNQfX7N0-', 'Countdown To Extinction', 'Megadeth')
    add_playlist('PLZSpx1qgL047Uc0QoTRqLHUJYak2zz0MP', 'Rust In Peace', 'Megadeth')
    add_playlist('PLZSpx1qgL045NZ0nDWBS482rX9h2HKvx7', 'So Far, So Good... So What', 'Megadeth')
    add_playlist('PLRFeURyjsHpNx5zI03BmlbKZjLpvOmMOG', 'Powerslave', 'Iron Maiden')
    add_playlist('PLIKpCFu8Fpmk_7mHRhnVob2vuiPjqYl8X', 'The Number Of The Beast', 'Iron Maiden')
    add_playlist('PLIKpCFu8Fpml1O5EIDNX6C5Mtovztm0Am', 'Piece Of Mind', 'Iron Maiden')
    
    
    
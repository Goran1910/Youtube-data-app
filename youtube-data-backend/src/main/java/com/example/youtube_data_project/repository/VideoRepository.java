package com.example.youtube_data_project.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.example.youtube_data_project.entity.Video;

@Repository
public interface VideoRepository extends JpaRepository<Video, Integer>{
	
	@Query(value = "select * from video join playlist on video.playlist_title = playlist.title where channel_title = :channelTitle order by views desc;", nativeQuery = true)
	public List<Video> findAllByPlaylistChannelTitle(@Param("channelTitle") String channelTitle);
	//public List<Video> findAllByPlaylistChannelTitleOrderByPlaylistChannelTitleAsc(String channelTitle);
	public List<Video> findAllByPlaylistTitle(String playlistTitle);
	
	@Query(value = "select * from video where playlist_title=:playlist_title order by views desc", nativeQuery = true)
	public List<Video> getVideosByPlaylist(@Param("playlist_title") String playlistTitle);
}

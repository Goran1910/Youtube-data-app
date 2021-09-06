package com.example.youtube_data_project.repository;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.example.youtube_data_project.entity.Playlist;

@Repository
public interface PlaylistRepository extends CrudRepository<Playlist, String>{
	public List<Playlist> findAllByChannelTitle(String channelTitle);
	
	@Query(value = "select title from playlist where channel_title = :channelTitle", nativeQuery = true)
	public List<String> getPlaylistsTitlesByChannelTitle(@Param("channelTitle") String channelTitle);
}

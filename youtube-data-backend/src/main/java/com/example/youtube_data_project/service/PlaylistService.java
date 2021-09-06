package com.example.youtube_data_project.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

import com.example.youtube_data_project.entity.Channel;
import com.example.youtube_data_project.entity.Playlist;
import com.example.youtube_data_project.entity.Video;
import com.example.youtube_data_project.repository.PlaylistRepository;
import com.example.youtube_data_project.repository.VideoRepository;

@Service
public class PlaylistService {
	PlaylistRepository playlistRepository;
	VideoRepository videoRepository;
	
	@Autowired
	public PlaylistService(PlaylistRepository playlistRepository, VideoRepository videoRepository) {
		this.playlistRepository = playlistRepository;
		this.videoRepository = videoRepository;
	}
	
	public List<Playlist> getPlaylistsByChannelTitle(String channelTitle){
		List<Playlist> playlists = playlistRepository.findAllByChannelTitle(channelTitle);
		this.calculateAll(playlists);
		return playlists;
	}
	
	public void calculateAll(List<Playlist> playlists) {
		for(Playlist p : playlists) {
			//List<Video> videos = videoRepository.findAllByPlaylistTitle(p.getTitle());
			//p.setVideos(videos);
			p.calculateTotalViews();
			p.calculateTotalLikes();
			p.calculateTotalDislikes();
			p.calculateTotalComments();
			p.calculateLikesPercentage();
			p.calculateLikesAndDislikesPerView();
		}
	}
	
	public List<String> getPlaylistsTitlesByChannelTitle(String channelTitle) {
		return this.playlistRepository.getPlaylistsTitlesByChannelTitle(channelTitle);
	}
}

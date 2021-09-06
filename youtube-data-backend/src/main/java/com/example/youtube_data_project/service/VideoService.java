package com.example.youtube_data_project.service;

import java.lang.reflect.Array;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.youtube_data_project.entity.Channel;
import com.example.youtube_data_project.entity.Video;
import com.example.youtube_data_project.repository.ChannelRepository;
import com.example.youtube_data_project.repository.VideoRepository;

@Service
public class VideoService {
	@Autowired
	VideoRepository videoRepository;
	
	public List<Video> getVideosSortedByChannelName(String name){
		List<Video> videos = (List<Video>) videoRepository.findAllByPlaylistChannelTitle(name);
		this.extraCalculations(videos);
		return videos;
	}
	
	private void extraCalculations(List<Video> videos) {
		for (Video video : videos) {
			video.calculateLikesPercentage();
			video.calculateLikesAndDislikesPerView();
		}
	}
	
	public List<Video> getVideosByPlaylist(String playlistName){
		List<Video> videos = this.videoRepository.getVideosByPlaylist(playlistName);
		this.extraCalculations(videos);
		return videos;
	}
	

	
}

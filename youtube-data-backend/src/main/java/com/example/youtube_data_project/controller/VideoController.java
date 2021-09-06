package com.example.youtube_data_project.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.youtube_data_project.entity.Playlist;
import com.example.youtube_data_project.entity.Video;
import com.example.youtube_data_project.service.PlaylistService;
import com.example.youtube_data_project.service.VideoService;

@RestController
@RequestMapping("videos")
public class VideoController {
	VideoService videoService;
	
	@Autowired
	public VideoController(VideoService videoService) {
		this.videoService = videoService;
	}
	
	@GetMapping("/{channelName}")
	public List<Video> getVideosSortedByChannelName(@PathVariable String channelName){
		return videoService.getVideosSortedByChannelName(channelName);
	}
	
	@GetMapping("/by/{playlistName}")
	public List<Video> getVideosByPlaylist(@PathVariable String playlistName){
		System.out.println(playlistName);
		return videoService.getVideosByPlaylist(playlistName);
	}
}

package com.example.youtube_data_project.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.youtube_data_project.entity.Playlist;
import com.example.youtube_data_project.service.PlaylistService;

@RestController
@RequestMapping(path = "playlists")
public class PlaylistController {
	
	PlaylistService playlistService;
	
	@Autowired
	public PlaylistController(PlaylistService playlistService) {
		this.playlistService = playlistService;
	}
	
	@GetMapping("/{channelTitle}")
	public ResponseEntity<List<Playlist>> getPlaylistsByChannelTitle(@PathVariable("channelTitle") String channelTitle){
		List<Playlist> playlists = playlistService.getPlaylistsByChannelTitle(channelTitle);
		return new ResponseEntity<>(playlists, HttpStatus.OK);
	}
	
	@GetMapping("/titles/{channelTitle}")
	public ResponseEntity<List<String>> getPlaylistsTitlesByChannelTitle(@PathVariable("channelTitle") String channelTitle){
		List<String> playlistsTitles = playlistService.getPlaylistsTitlesByChannelTitle(channelTitle);
		return new ResponseEntity<>(playlistsTitles, HttpStatus.OK);
	}
}

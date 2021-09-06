package com.example.youtube_data_project.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.youtube_data_project.entity.Channel;
import com.example.youtube_data_project.entity.Playlist;
import com.example.youtube_data_project.service.ChannelService;

@RestController
@RequestMapping("channels")
public class ChannelController {
	
	private ChannelService channelService;
	
	@Autowired
	public ChannelController(ChannelService channelService) {
		this.channelService = channelService;
	}
	
	@GetMapping
	public ResponseEntity<List<Channel>> getChannels(){
		List<Channel> channels = channelService.getChannels();
		return new ResponseEntity<>(channels, HttpStatus.OK);
	}
	
	@GetMapping("/{name}")
	public ResponseEntity<Channel> getChannelByTitle(@PathVariable String name){
		Channel channel = channelService.getChannelByTitle(name);
		return new ResponseEntity<>(channel, HttpStatus.OK);
	}
	
}

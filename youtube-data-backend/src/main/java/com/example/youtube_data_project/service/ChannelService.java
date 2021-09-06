package com.example.youtube_data_project.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.youtube_data_project.entity.Channel;
import com.example.youtube_data_project.repository.ChannelRepository;

@Service
public class ChannelService {
	
	@Autowired
	ChannelRepository channelRepository;
	
	public List<Channel> getChannels(){
		return (List<Channel>) channelRepository.findAll();
	}
	
	public Channel getChannelByTitle(String title) {
		return channelRepository.findByTitle(title).orElse(null);
	}
}

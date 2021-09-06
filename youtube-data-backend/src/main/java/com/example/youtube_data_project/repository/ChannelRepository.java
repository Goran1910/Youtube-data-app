package com.example.youtube_data_project.repository;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.youtube_data_project.entity.Channel;

@Repository
public interface ChannelRepository extends CrudRepository<Channel, String>{
	public Optional<Channel> findByTitle(String title);
}

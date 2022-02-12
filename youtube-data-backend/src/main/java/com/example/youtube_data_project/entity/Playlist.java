package com.example.youtube_data_project.entity;

import java.util.List;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Transient;

import org.apache.commons.math3.util.Precision;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonManagedReference;

@Entity(name="playlist")
public class Playlist {
	@Id
	private String id;
	private String title;
	private String thumbnailUrl;
	
	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name="channel_title")
	private Channel channel;
	
	@JsonInclude
	@Transient
	private Long totalViews = 0l;
	
	@JsonInclude
	@Transient
	private int totalLikes;
	
	@JsonInclude
	@Transient
	private int totalDislikes;
	
	@JsonInclude
	@Transient
	private int totalComments;
	
	@JsonInclude
	@Transient
	private double likesPercentage;
	
	@JsonInclude
	@Transient
	private double likesAndDislikesPerView;
	
	@JsonIgnore
	@OneToMany(mappedBy="playlist", fetch=FetchType.LAZY)
	private List<Video> videos;

	public Long getTotalViews() {
		return totalViews;
	}

	public void setTotalViews(Long totalViews) {
		this.totalViews = totalViews;
	}

	public int getTotalLikes() {
		return totalLikes;
	}

	public void setTotalLikes(int totalLikes) {
		this.totalLikes = totalLikes;
	}

	public int getTotalDislikes() {
		return totalDislikes;
	}

	public void setTotalDislikes(int totalDislikes) {
		this.totalDislikes = totalDislikes;
	}

	public int getTotalComments() {
		return totalComments;
	}

	public void setTotalComments(int totalComments) {
		this.totalComments = totalComments;
	}

	public double getLikesPercentage() {
		return likesPercentage;
	}

	public void setLikesPercentage(double likesPercentage) {
		this.likesPercentage = likesPercentage;
	}

	public double getLikesAndDislikesPerView() {
		return likesAndDislikesPerView;
	}

	public void setLikesAndDislikesPerView(double likesAndDislikesPerView) {
		this.likesAndDislikesPerView = likesAndDislikesPerView;
	}
	
	public List<Video> getVideos() {
		return videos;
	}

	public void setVideos(List<Video> videos) {
		this.videos = videos;
	}

	public Playlist() {
		
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getThumbnailUrl() {
		return thumbnailUrl;
	}

	public void setThumbnailUrl(String thumbnailUrl) {
		this.thumbnailUrl = thumbnailUrl;
	}

	public Channel getChannel() {
		return channel;
	}

	public void setChannel(Channel channel) {
		this.channel = channel;
	}
	
	public void calculateTotalViews() {
		for(Video v : videos) {
			this.totalViews += v.getViews();
		}
	}
	
	public void calculateTotalLikes() {
		for(Video v : videos) {
			this.totalLikes += v.getLikes();
		}
	}
	
	public void calculateTotalDislikes() {
		for(Video v : videos) {
			this.totalDislikes += v.getDislikes();
		}
	}
	
	public void calculateTotalComments() {
		for(Video v : videos) {
			this.totalComments += v.getComments();
		}
	}
	
	public void calculateLikesPercentage() {
		double n = ((float) this.totalLikes / (this.totalLikes + this.totalDislikes)) * 100;
		this.likesPercentage = Precision.round(n, 2); 
	}
	
	public void calculateLikesAndDislikesPerView() {
		double n = ((float) (this.totalLikes + this.totalDislikes) / this.totalViews) * 100;
		this.likesAndDislikesPerView = Precision.round(n, 3);
	}
	
}

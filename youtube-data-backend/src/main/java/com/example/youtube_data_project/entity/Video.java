package com.example.youtube_data_project.entity;

import java.sql.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.persistence.Transient;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonInclude;
import org.apache.commons.math3.util.Precision;

@Entity
@Table(name = "video")
public class Video {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	private String title;
	private Long views;
	private int likes;
	private int dislikes;
	private int comments;
	private Date publishedAt;
	private int duration;
	private String thumbnailUrl;
	
	@JsonInclude
	@Transient
	private double likesPercentage;
	
	@JsonInclude
	@Transient
	private double likesAndDislikesPerView;
	
	
	@ManyToOne(fetch=FetchType.EAGER)
	@JoinColumn(name="playlist_id")
	private Playlist playlist;
	
	public Video() {
		
	}
	

	public double getLikesPercentage() {
		return likesPercentage;
	}

	public void setLikesPercentage(double likesPercentage) {
		this.likesPercentage = likesPercentage;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public Long getViews() {
		return views;
	}

	public void setViews(Long views) {
		this.views = views;
	}

	public int getLikes() {
		return likes;
	}

	public void setLikes(int likes) {
		this.likes = likes;
	}

	public int getDislikes() {
		return dislikes;
	}

	public void setDislikes(int dislikes) {
		this.dislikes = dislikes;
	}

	public int getComments() {
		return comments;
	}

	public void setComments(int comments) {
		this.comments = comments;
	}

	public Date getPublishedAt() {
		return publishedAt;
	}

	public void setPublishedAt(Date publishedAt) {
		this.publishedAt = publishedAt;
	}

	public int getDuration() {
		return duration;
	}

	public void setDuration(int duration) {
		this.duration = duration;
	}

	public String getThumbnailUrl() {
		return thumbnailUrl;
	}

	public void setThumbnailUrl(String thumbnailUrl) {
		this.thumbnailUrl = thumbnailUrl;
	}

	public Playlist getPlaylist() {
		return playlist;
	}

	public void setPlaylist(Playlist playlist) {
		this.playlist = playlist;
	}
	
	public double getLikesAndDislikesPerView() {
		return likesAndDislikesPerView;
	}


	public void setLikesAndDislikesPerView(double likesAndDislikesPerView) {
		this.likesAndDislikesPerView = likesAndDislikesPerView;
	}

	public void calculateLikesPercentage() {
		double n = ((float) this.likes / (this.likes + this.dislikes)) * 100;
		this.likesPercentage = Precision.round(n, 2); 
	}
	
	public void calculateLikesAndDislikesPerView() {
		double n = ((float) (this.likes + this.dislikes) / this.views) * 100;
		this.likesAndDislikesPerView = Precision.round(n, 3);
	}
	
}

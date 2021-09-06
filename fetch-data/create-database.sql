create database youtube_data;
create user 'korisnik1' identified by '12345';
grant all on youtube_data.* to 'korisnik1';
use youtube_data;

create table channel(
title varchar(15) not null,
subscriber_count int,
video_count int,
thumbnail_url varchar(200),
id varchar(30),
primary key (title)
);

create table playlist(
title varchar(30) not null,
id varchar(50),
thumbnail_url varchar(200),
channel_title varchar(15),
primary key (title),
foreign key (channel_title) references channel(title)
);

create table video(
id int auto_increment not null,
title varchar(80),
playlist_title varchar(30),
views int,
likes int,
dislikes int,
comments int,
published_at date,
duration int,
thumbnail_url varchar(200),
primary key (id),
foreign key (playlist_title) references playlist(title)
);
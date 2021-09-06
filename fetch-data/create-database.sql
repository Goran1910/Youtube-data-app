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

insert into channel(title, subscriber_count, thumbnail_url, video_count, id) values ('Metallica', 7520000, 1686, 'https://yt3.ggpht.com/ZjcQii3sVKaPcGK3rIm8vot-qwdmm7KAHsWCjlQLsDLa_tm2kykM-Lgmty1IwQWehj7nEzXPUA=s800-c-k-c0x00ffffff-no-nd-rj', 'UCbulh9WdLtEXiooRcYK7SWw');
insert into channel(title, subscriber_count, thumbnail_url, video_count, id) values ('Iron Maiden', 1960000, 238, 'https://yt3.ggpht.com/ytc/AKedOLQaZfQ0DPNoTTMZIHanzzZWogOn8Ahe-srvqx7lZA=s800-c-k-c0x00ffffff-no-rj-mo','UCaisXKBdNOYqGr2qOXCLchQ');
insert into channel(title, subscriber_count, thumbnail_url, video_count, id) values ('Megadeth', 914000, 176, 'https://yt3.ggpht.com/ytc/AKedOLQ4wkmTz21sEl9qI1HCWgZTeUXXE2DGfQbUjpNIPA=s800-c-k-c0x00ffffff-no-rj-mo', 'UCLVz1B001PIbq9LliJenV2w');

insert into playlist(title, id, channel_title) values ('Kill \'Em All', 'PLBnJv6rImVe_PcPIPV_iXEUcaOhMb7dYv', 'Metallica');
insert into playlist(title, id, channel_title) values ('Ride The Lightning', 'PL6ogdCG3tAWjkTOqqaO1JaTzaFtk6WWv4', 'Metallica');
insert into playlist(title, id, channel_title) values ('Master Of Puppets', 'PL6ogdCG3tAWiIOauDDXTvfTL-Gx4vz1Wt', 'Metallica');
insert into playlist(title, id, channel_title) values ('...And Justice For All', 'PL6ogdCG3tAWhOUeMyn8UqrBTNgonrnbs3', 'Metallica');
insert into playlist(title, id, channel_title) values ('Black Album', 'PLBU3rjLvn2nTAGUzCiQjgeoPl0Bl0RZeB', 'Metallica');
insert into playlist(title, id, channel_title) values ('Load', 'PL6vwnon3sINrOI8XVtIQDYBCqWfhqJ19d', 'Metallica');
insert into playlist(title, id, channel_title) values ('Reload', 'PL6vwnon3sINo-k0MMuit5J75BWd91vohX', 'Metallica');
insert into playlist(title, id, channel_title) values ('St. Anger', 'PL6vwnon3sINoNaBSLoO5dEBKc6GNKYI8_', 'Metallica');
insert into playlist(title, id, channel_title) values ('Death Magnetic', 'PL6vwnon3sINr_Emg1neUAZoIecAHwOjgY', 'Metallica');
insert into playlist(title, id, channel_title) values ('Hardwired... To Self-Destruct', 'PLZ9DoO2uX9wW8zIGvcSLPHtzfKRWYNuCg', 'Metallica');
insert into playlist(title, id, channel_title) values ('Official Music Video', 'PL2D4A44B959D87893', 'Metallica');
insert into playlist(title, id, channel_title) values ('Countdown To Extinction', 'PLZSpx1qgL045KdXmH3pdDT0UeNQfX7N0-', 'Megadeth');
insert into playlist(title, id, channel_title) values ('Rust In Peace', 'PLZSpx1qgL047Uc0QoTRqLHUJYak2zz0MP', 'Megadeth');
insert into playlist(title, id, channel_title) values ('So Far, So Good... So What', 'PLZSpx1qgL045NZ0nDWBS482rX9h2HKvx7', 'Megadeth');
insert into playlist(title, id, channel_title) values ('Powerslave', 'PLRFeURyjsHpNx5zI03BmlbKZjLpvOmMOG', 'Iron Maiden');
insert into playlist(title, id, channel_title) values ('The Number Of The Beast', 'PLIKpCFu8Fpmk_7mHRhnVob2vuiPjqYl8X', 'Iron Maiden');
insert into playlist(title, id, channel_title) values ('Piece Of Mind', 'PLIKpCFu8Fpml1O5EIDNX6C5Mtovztm0Am', 'Iron Maiden');

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
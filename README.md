# Lyricloud
Using python to crawl lyrics automatically from a whole playlist at https://music.163.com/, and using https://wordart.com/ to generate word cloud.

###version 1 files
* /cloud_img : store LyriCloud imags
+ /lyrics : store lyric txt files of each album
- lyrics_crawl.py : use python *requests* to get lyrics and *json* to decode lyric content
* get_songid.py : unsolved problem--get song_ids from playlist page using *BeautifulSoup*

version 2 aims at getting song ids automatically using *BeautifulSoup*

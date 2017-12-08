# Lyricloud
Use python to crawl lyrics automatically from a whole playlist at [NetEase](https://music.163.com/) , and use [WordArt](https://wordart.com/)  to generate lyric cloud.

Thank [WangYang-wy](https://github.com/WangYang-wy) for his commits and great support.

### Blog article
This README only contains how to use python to crawl all the lyrics. Visit [this Chinese blog](https://viciayuan.github.io/2017/12/07/LyriCloud/#more) to learn about: 
* detailed directions to generate beautiful LyriCloud pictures 
+ interesting analysis of the results offered by the author

### Version 2 files
- **lyrics_crawl.py** : use album_id as input, then you get the all the lyrics from that album for output.
- **get_songid.py** : how to get song_ids from album_id.
- **.gitmore** : ignore temporary json files which keeps the song's information
- **/cloud_img** : store LyriCloud imags. (just for demonstration)
- **/lyrics** : store lyric txt files of each album. (not so necessary)

### Next step
- Offer more options of playlists
    - from album using album_id (finished)
    - from a singer's top 50 hit songs using singer_id
    - from a playlist created by users using playlist_id
- choose a database to store the lyrics
- to be continued...

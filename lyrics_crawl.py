import requests
import json
import re
from bs4 import BeautifulSoup

# 输入网易云音乐album_id，可任意改成自己喜欢专辑的id
album_id = 36709029

# 根据album_id 从专辑页面获取所有歌曲的song_ids
session = requests.Session()
url = 'https://music.163.com/album?id=' + str(album_id)
s = session.get(url)
soup = BeautifulSoup(s.text, 'html.parser')

getJSON = soup.select("#song-list-pre-cache textarea")[0].contents[0]

json_data = json.loads(getJSON)
with open("./json/reputation.json", 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False)

# 爬取下来的是一个json对象，里面是多个json组成的数组，查看每个元素的key
# print(json_data[0].keys())

# 将每首歌id整合成数组song_ids，用于后面爬取所有歌的歌词。
song_ids = []
for item in json_data:
    # print(type(item['id']))
    id = item['id']
    song_ids.append(id)

# 得到所有song id之后，循环打印每首歌曲页面的歌词
for song_id in song_ids:
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    r = requests.get(url)
    json_obj = r.text
    j = json.loads(json_obj)
    lyric = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lyric = re.sub(pat, "", lyric)
    print(lyric.strip())
    print(song_id)

# 以及谢谢阳神的支持。

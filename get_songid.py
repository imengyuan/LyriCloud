import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()
url = 'https://music.163.com/album?id=36709029'
s = session.get(url)
soup = BeautifulSoup(s.text, 'html.parser')

getJSON = soup.select("#song-list-pre-cache textarea")[0].contents[0]

json_data = json.loads(getJSON)
with open("./json/reputation.json", 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False)

# 爬取下来的是一个json对象，里面是多个json组成的数组，查看每个元素的key。
# print(json_data[0].keys())

# 将每首歌id整合成数组，用于后面爬所有歌的歌词。
song_ids = []
for item in json_data:
    # print(type(item['id']))
    id = item['id']
    song_ids.append(id)

print(song_ids)

# 后续可添加歌曲列表的其他来源，
# 比如来自歌手页面的最热50首歌，或者任意一个网易云音乐歌单

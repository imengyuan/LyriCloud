import requests
from bs4 import BeautifulSoup
import re
import json

session = requests.Session()
url = 'https://music.163.com/album?id=36709029'
s = session.get(url)
soup = BeautifulSoup(s.text, 'html.parser')

getJSON = soup.select("#song-list-pre-cache textarea")[0].contents[0]

j = json.loads(getJSON)

# 查看JSON文件。
# print(j)

for i in j:
    print(i['name'])
    print(i['id'])
    print(i)
#
# # print(soup)
#
#
# song_table = soup.find_all(class_='m-table')
# # print(song_table)
#
# song_ply = soup.select('.ply').get_text()
# print(song_ply)
# #
# # for song_item in song_items:
# #     song_id = song_item.data - res - id
# #     print(song_id)

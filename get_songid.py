import requests
from bs4 import BeautifulSoup
import re

url = 'https://music.163.com/#/album?id=36709029'
r = requests.get(url)
content = r.text
# print(content)
soup = BeautifulSoup(content, 'lxml')
# song_table = soup.find_all(class_ = 'm-table')
song_table = soup.select('.ply').get_text()
print(song_table)
'''
for song_item in song_items:
    song_id = song_item.data-res-id
    print(song_id)'''

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

for item in json_data:
    print("id = ", item['id'], ", name = ", item['name'])

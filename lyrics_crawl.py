import requests
import json
from bs4 import BeautifulSoup


#Taylor-Reputation id看不出任何规律
'''song_id = ['503207093', '516823324', '516827355', '516823325', '516818336', '501133611',
           '516827356', '514235010', '516818337', '516818338', '516823326', '516827357',
           '516819321', '516776413', '516823327']'''
#Taylor-1989 有三首歌和其他的不一样，看不出来是因为先发行（eg. 6）还是因为啥
#song_id = ['29561031', '29498911', '29561033'] #1,4,6
#range(29572501,29572516)

#Taylor-RED 出乎意料的全部有规律！
# range(25787215,25787236)

#RADWIMPS-your name
#range(426881480,426881506)

#Ed Sheeran-divide 4 rebels
song_id = ['460112985', '460112986', '460298206', '460112987']
#range(460043699,460043711)


for i in range(0,4):
    url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(song_id[i])+ '&lv=1&kv=1&tv=-1'
    r = requests.get(url)
    json_obj = r.text
    j = json.loads(json_obj)
    print(j['lrc']['lyric'])
    print(i)

for i in range(460043699,460043711):
    url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(i)+ '&lv=1&kv=1&tv=-1'
    r = requests.get(url)
    json_obj = r.text
    j1 = json.loads(json_obj)
    print(j1['lrc']['lyric'])
    print(i)

# not used but stiil put here
'''content = r.text
soup = BeautifulSoup(r.text,'lxml')

lyric1 = soup.find_all(div_ = 'lyric-content').get_text()
lyric2 = soup.find_all(div_ = 'flag_more').get_text()

print(lyric1)'''
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190406')
soup = BeautifulSoup(url,'lxml')
n_artist = 0   #아티스트 수
n_title = 0   #제목의 수
list_artist = []
list_title = []
"""
for i in soup.find_all(name='p', attrs=({"class":"artist"})):
    n_artist += 1
    print(str(n_artist)+" 위")
    print("아트스트:" +i.find('a').text)

  #  print("아트스트:" +i.text)
print('=======================')
for i in soup.find_all(name='p', attrs=({"class":"title"})):
    n_title += 1
    print(str(n_title)+" 위")
    print("노래제목:" +i.text)
"""

list_artist = soup.find_all(name='p', attrs=({"class":"artist"}))
list_title = soup.find_all(name='p', attrs=({"class":"title"}))

nindex = 0
for i in list_artist:

    n_artist += 1
    print(str(n_artist)+" 위")
    print("아트스트:" +i.find('a').text)
    print("노래제목:" +list_title[nindex].text)
    nindex = nindex + 1







from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

ctx = "C:/Users/ezen/PycharmProjects/"
driver = webdriver.Chrome(ctx+"chromedriver")
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source,'html.parser')
#soup = BeautifulSoup(driver.page_source,'lxml')
soup.prettify()
"""
웹클로링 시 크로링 할 웹 페이지에 들어 가서 F12 번을 클릭 한후
해당 소스를 확인해서 가져올 대상을 결정 한 후 가져 온다
이때 화면의 가져올 대상을 마우스로 위치한 후 마우스 오른쪽 누른 후 
검사 메뉴을 선택 하면 해당 소스 부분으로 이동한다. 

"""
# 'div' 중에서 'class' 가 'tit3' 인 것을 다 가져 온다
all_divs = soup.find_all('div', attrs={'class':'tit3'})
# all_divs 안 에 있는 div 에서 div 의 a 중 string 을 가져와서 productsdp 에 넣어 준다.
products = [div.a.string for div in all_divs]
for i in products:
    print(i)
driver.close()
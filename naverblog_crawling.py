!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)

URL = 'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=recentdate&keyword=%EC%96%91%EC%82%B0'
driver.get(url=URL)

#이승주-양산 관련 네이버 블로그를 최신순으로 5개 나타내기
blog_title = driver.find_elements_by_class_name('desc_inner')
blog_date = driver.find_elements_by_class_name('date')

title=[]
for i in blog_title :
  title.append(i.text)
title=title[:5]
print(title)

date=[]
for i in blog_date :
  date.append(i.text)
date=date[:5]
print(date)

for j in range(len(title)) :
  print(f'순서 : {j+1}, 제목 : {title[j]}') 

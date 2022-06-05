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
#print(title)-양산 관련 블로그 제목 크롤링

date=[]
for i in blog_date :
  date.append(i.text)
date=date[:5]
#print(date)-양산 관련 블로그의 업로드 시간 크롤링

for j in range(len(title)) :
  print(f'순서 : {j+1}, 제목 : {title[j]}, 시간 : {date[j]}')
#양산 관련 블로그 최신순으로 출력하기
  
#김준형-원하는 순서의 블로그 정보 나타내기
blog_author = driver.find_elements_by_class_name('name_author')
blog_name = driver.find_elements_by_class_name('name_blog')

author=[]
for i in blog_author :
  author.append(i.text)
author=author[:5]
#print(author)-블로그 저자 크롤링

name=[]
for i in blog_name :
  name.append(i.text)
name=name[:5]
#print(name)-블로그명 크롤링

blog_want=list(map(int,input('원하는 순서를 입력하시오 : ').split()))
for i in range(len(blog_want)) :
  print(f'제목 : {title[i]}, 저자 : {author[i]}, 블로그명 : {name[i]}, 시간 : {date[i]}')
#원하는 순서 블로그의 제목, 저자, 블로그명, 시간과 같은 블로그 정보 출력

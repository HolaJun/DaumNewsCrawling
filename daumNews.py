# -*- coding: utf-8 -*-

import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions

# chromedriver 위치
wd = 'C:/Users/HolaJun/Desktop/DaumNewsCrawling/chromedriver.exe'
# 크롤링하고자 하는 사이트
addr = 'https://sports.v.daum.net/v/20190102211709263?d=y'
# 출력 파일명
OUTPUT_FILE_NAME = 'output.txt'

# 크롬드라이버 로드
driver = webdriver.Chrome(wd)
# 매개변수의 주소 띄움
driver.get(addr)

# 크롤링에 필요 없는 특정 element의 속성 제거하기(스포츠란)
# element = driver.find_element_by_class_name('vod_cluster2')
# driver.execute_script("""
# var element = arguments[0];
# element.parentNode.removeChild(element);
# """, element)

# 다음뉴스의 모든 댓글 페이지를 띄움
def daumNewsFullpage():
    cnt = 0
    try:
        while cnt < 5:
            driver.find_element_by_css_selector(
                "#alex-area > div > div > div > div.cmt_box > div.alex_more > a"
                ).click()
            time.sleep(0.8)
            cnt += 1
            
    # 페이지 끝
    except exceptions.ElementNotVisibleException as e:
        pass
    # 다른 예외 발생시 확인
    except Exception as e:
        print('[error ^________^]: ', e)

# 다음뉴스 제목, 내용 파싱
def daumNewsParsing():
    html = driver.page_source
    dom = BeautifulSoup(html, 'lxml')
    title = dom.find("h3", "tit_view").text
    print('뉴스제목:', title) 
    return title

# 댓글더보기 다 누른 상태에서의 수행할 파싱 코드
def commentParsing():
    commentAmount = 0
    str = ''
    html = driver.page_source
    dom = BeautifulSoup(html, 'lxml')
    
    # 댓글검색( P 태그의 desc_txt font_size_17 class명을 검색 )
    cnt = 0
    comments = dom.find_all("p", "desc_txt font_size_17")
    for result in comments:
        up = dom.select('button.btn_recomm > span.num_txt')[cnt].text
        down = dom.select('button.btn_oppose > span.num_txt')[cnt].text
        nickname = dom.select('a.link_nick')[cnt].text
        
        # 닉네임 두번째 글자부터 별표 만들기
        for i in range(1, len(nickname)):
            if(nickname[i]):
                nickname = nickname.replace(nickname[i], '*', 1)

        print('닉네임:', nickname)
        print('추천', up, '비추천', down)
        print(result.text , '\n\n')
        cnt += 1;

    return str

def fileSave(txt):
    f = open(OUTPUT_FILE_NAME, 'w', encoding='UTF8')
    f.write(txt)
    f.close()

if __name__ == "__main__":
    daumNewsFullpage() 
    daumNewsParsing()
    result = commentParsing()
    
    fileSave(result)
    driver.quit()
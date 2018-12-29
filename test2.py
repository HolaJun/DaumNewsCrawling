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
addr = 'http://udemycoupon.discountsglobal.com/coupon-category/free-2/'

# 크롬드라이버 로드
driver = webdriver.Chrome(wd)
# 매개변수의 주소 띄움
driver.get(addr)

#select by css
#try *
css_lnks = [i.get_attribute('href') for i in driver.find_elements_by_css_selector('[id*=coupon-link]')]
#or try ^
#css_lnks = [i.get_attribute('href') for i in driver.find_elements_by_css_selector('[id^=coupon-link]')]

#select by xpath
xpth_lnks = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//a[contains(@id,'coupon-link-')]")]

print(xpth_lnks)
print(css_lnks)
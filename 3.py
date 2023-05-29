import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#질병코드 검색으로 크롤링
search = input('알아보고 싶은 질병코드를 입력하세요. :')

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.koicd.kr/")
time.sleep(3)

driver.find_element(By.ID, "text-search").click()
element = driver.find_element(By.ID, "text-search")
element.send_keys(search)

element.send_keys(Keys.RETURN) 

time.sleep(10)
driver.quit()
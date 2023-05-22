# pip install seleniuim
# pip install webdriver_manager

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(options=options)

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)



driver.get("https://health.kdca.go.kr/healthinfo/biz/health/main/mainPage/main.do")
time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div[3]/form[2]/div/div[1]/div/div[2]/span[1]").click()

driver.find_element(By.XPATH, "/html/body/div[3]/form[2]/div/div[1]/div/div[1]/div[1]/div/div/input").click()

data = crawl_data(disease)

driver.find_element(By.XPATH, "/html/body/div[3]/form[2]/div/div[1]/div/div[1]/div[1]/div/div/input").send_keys(data)
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[3]/form[2]/div/div[1]/div/div[1]/div[1]/div/div/button").click()
time.sleep(30)


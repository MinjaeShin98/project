import pandas as pd      # pip install pandas 설치
import numpy as np
import seaborn as sns
import tkinter as tk
import tkinter.font as tkfont

# 한글 깨짐 방지
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

# 엑셀 파일에서 데이터 프레임 생성
data_file = '건강데이터.xlsx'
sheet_names = ['10대 남자', '10대 여자', '20대 남자', '20대 여자', '30대 남자', '30대 여자']

# 시트별로 데이터 불러오기
data_frames = {}  # 시트별 데이터를 저장할 딕셔너리

for sheet_name in sheet_names:
    df = pd.read_excel(data_file, sheet_name=sheet_name)
    
    # '환자수' 열의 데이터 타입 확인 후 문자열로 변환
    if not pd.api.types.is_string_dtype(df['환자수']):
        df['환자수'] = df['환자수'].astype(str)
    
    df['환자수'] = df['환자수'].str.replace(',', '').astype(int)
    data_frames[sheet_name] = df

# 시각화
for sheet_name in sheet_names:
    df = data_frames[sheet_name]
    
    if '10대' in sheet_name:
        # 10대는 가로 막대 그래프 사용
        plt.figure(figsize=(13, 8))
        sns.barplot(x='환자수', y='질병명', data=df)
        plt.title(sheet_name)
        plt.show()
    elif '20대' in sheet_name:
        # 20대는 원 그래프 사용
        plt.figure(figsize=(13, 8))
        plt.pie(df['환자수'], labels=df['질병명'], autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'})
        plt.title(sheet_name)
        plt.show()
    elif '30대' in sheet_name:
        # 30대는 도넛 그래프 사용
        plt.figure(figsize=(13, 8))
        plt.pie(df['환자수'], labels=df['질병명'], autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.3, 'edgecolor': 'white'})
        plt.title(sheet_name)
        plt.show()

'''사용자'''

def find_disease(gender, age):
    # 파일에서 성별과 연령에 따른 질병과 질병 코드를 찾아 반환하는 함수
    df = pd.read_excel('연령별질병.xlsx')
    filtered_df = df[(df['성별'] == gender) & (df['연령'] == age)]
    if not filtered_df.empty:
        diseases = filtered_df['질병'].tolist()
        disease_codes = filtered_df['질병코드'].tolist()
        return diseases, disease_codes
    else:
        return None, None

def save_data(gender, age, diseases, disease_codes):
    # 성별, 연령, 질병, 질병 코드를 파일에 저장하는 함수
    with open('검색기록.txt', 'a', encoding='utf-8') as file:
        file.write(f"성별: {gender}\n")
        file.write(f"연령: {age}\n")
        file.write("질병 및 질병 코드:\n")
        for disease, code in zip(diseases, disease_codes):
            file.write(f"- {disease} ({code})\n")
        file.write("---------------\n")

# 사용자로부터 성별과 연령 입력받음
gender = input("성별을 입력하세요 (남성 또는 여성): ")
age = input("연령대를 입력하세요 (10대, 20대, 30대): ")

# 질병 검색
diseases, disease_codes = find_disease(gender, age)

# 질병 출력
if diseases:
    print("\n해당 성별과 연령에 해당하는 질병 및 질병 코드:\n")
    for disease, code in zip(diseases, disease_codes):
        print(f"{disease} ({code})")
else:
    print("해당 성별과 연령에 해당하는 질병이 없습니다.")

# 검색기록.txt 파일에 데이터 저장
save_data(gender, age, diseases, disease_codes)

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
search = input('\n알아보고 싶은 질병코드를 입력하세요. :')

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
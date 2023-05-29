import pandas as pd      # pip install pandas 설치

import tkinter as tk
import tkinter.font as tkfont

# 한글 깨짐 방지
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'


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

'''질병 검색 크롤링'''

search_disease = input("질병을 검색하시겠습니까? (예/아니오): ")

if search_disease == "예":
   
    webbrowser.open('https://www.koicd.kr/')
    
 
    
else:
    print("질병 검색을 종료합니다.")
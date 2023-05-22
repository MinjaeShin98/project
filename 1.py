import pandas as pd      # pip install pandas 설치

def find_disease(gender, age):
    # 파일에서 성별과 연령에 따른 질병을 찾아 반환하는 함수
    df = pd.read_excel('예시파일.xlsx')
    filtered_df = df[(df['성별'] == gender) & (df['연령'] == age)]
    if not filtered_df.empty:
        diseases = filtered_df['질병'].tolist()
        return diseases
    else:
        return None

def find_prevention(disease):
    # 파일에서 질병에 대한 예방법을 찾아 반환하는 함수
    df = pd.read_excel('예시파일.elsx')
    prevention = df[df['질병'] == disease]['예방법'].iloc[0]
    return prevention

def save_data(gender, age, disease, prevention):
    # 성별, 연령, 질병, 예방법을 파일에 저장하는 함수
    with open('output.txt', 'a') as file:
        file.write(f"성별: {gender}\n")
        file.write(f"연령: {age}\n")
        file.write(f"질병: {disease}\n")
        file.write(f"예방법: {prevention}\n")
        file.write("---------------\n")

# 사용자로부터 성별과 연령 입력받음
gender = input("성별을 입력하세요 (남성 또는 여성): ")
age = int(input("연령을 입력하세요: "))

# 질병 검색
diseases = find_disease(gender, age)

# 질병 출력
if diseases:
    print("해당 성별과 연령에 해당하는 질병:")
    for disease in diseases:
        print(disease)
else:
    print("해당 성별과 연령에 해당하는 질병이 없습니다.")

# 질병 입력받음
disease = input("질병을 입력하세요: ")

# 예방법 검색
prevention = find_prevention(disease)

# 예방법 출력
if prevention:
    print("해당 질병에 대한 예방법: ", prevention)
else:
    print("해당 질병에 대한 예방법이 없습니다.")

# output.txt 파일에 데이터 저장
save_data(gender, age, disease, prevention)

import matplotlib.pyplot as plt # pip install matplotlib 설치


# 사망원인과 그에 따른 비율 데이터
causes = ['암', '심장질환', '폐렴', '뇌혈관질환', '자살']
percentages = [158.2, 60.4, 45.1, 42, 26.9]

# 원 그래프 그리기
plt.pie(percentages, labels=causes, autopct='%1.1f%%')

# 그래프 제목 설정
plt.title('대한민국 사망원인 TOP5')

# 그래프 출력
plt.show()


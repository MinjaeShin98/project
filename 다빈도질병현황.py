import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc #글자가 깨져서 코드를 적용했습니다(5~15).
import platform

if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else: #linux
    rc('font', family='NanumGothic')
    
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 현상 해결 코드

# 건강검진 데이터 파일 불러오기
df = pd.read_csv("다빈도질병현황.csv", encoding='utf-8')

# 출력에서 줄을 맞추기 위해 데이터를 정렬합니다.
df = df[['3단질병명', '순위', '환자수']]

# 데이터 프레임을 출력합니다.
print(df)

# '환자수' 열의 데이터를 숫자 형식으로 변환
df['환자수'] = df['환자수'].str.replace(',', '').astype(int)

# 그래프의 사이즈를 조절합니다.
plt.figure(figsize=(10, 8))

# 막대 그래프를 그립니다.
sns.barplot(x='환자수', y='3단질병명', data=df)

# 그래프 제목을 설정합니다.
plt.title('다빈도 질병 현황')

# y축 레이블의 위치를 조정합니다.
plt.subplots_adjust(left=0.3)

# 그래프를 출력합니다.
plt.show()

#----------------여기는 원 그래프 입니다.----------------

# 그래프의 사이즈를 조절합니다.
plt.figure(figsize=(8, 8))

# 원 그래프를 그립니다.
plt.pie(df['환자수'], labels=df['3단질병명'], startangle=90, counterclock=False, autopct='%1.1f%%')

# 그래프 제목을 설정합니다.
plt.title('다빈도 질병 현황')

# 그래프를 출력합니다.
plt.show()

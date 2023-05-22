######################
#1) 관련 package, module impor하기 
######################


# pip install patplotlib
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

######################
# 2) 그래프 여러개를 하나의 그래프 좌표에 그리기
######################

plt.title("10대 질병별 환자수 TOP 5")

companies = ('복부 및 골반 통증', '급성 충수염', '감염 및 기생충성 질환', '감염 및 원인불명 위장염 및 결장염', 'U07의 응급사용')
sales = [6907, 9421, 14760, 25082, 29173]
plt.barh(companies, sales, height=0.5, color = 'red')
# 막대 위 숫자 작성
for i, v in enumerate(sales) : # enumerate()로 막대의 인덱스와 값을 가져온다
    plt.text(v, i, str(v), ha='right', va='center') # ha = 텍스트 오른쪽 정렬, va = 수직 중앙 정렬, str = 값을 문자열로 변환
plt.show()

plt.title("20대 질병별 환자수 TOP 5")

companies = ('기타 추간판장애', '치핵 및 항문주위정맥혈전증', '감염 및 기생충성 질환', '감염 및 원인불명 위장염 및 결장염', 'U07의 응급사용')
sales = [18127, 22787, 27377, 32920, 46122]
plt.barh(companies, sales, height=0.5, color = 'orange')
# 막대 위 숫자 작성
for i, v in enumerate(sales) : # enumerate()로 막대의 인덱스와 값을 가져온다
    plt.text(v, i, str(v), ha='right', va='center') # ha = 텍스트 오른쪽 정렬, va = 수직 중앙 정렬, str = 값을 문자열로 변환
plt.show()

plt.title("30대 질병별 환자수 TOP 5")

companies = ('치핵 및 항문주위정맥혈전증', '제왕절개에 의한 단일분만', '기타 추간판장애', 'U07의 응급사용', '단일자연분만')
sales = [29309, 29808, 30704, 41215, 53191]
plt.barh(companies, sales, height=0.5, color = 'yellow')
# 막대 위 숫자 작성
for i, v in enumerate(sales) : # enumerate()로 막대의 인덱스와 값을 가져온다
    plt.text(v, i, str(v), ha='right', va='center') # ha = 텍스트 오른쪽 정렬, va = 수직 중앙 정렬, str = 값을 문자열로 변환
plt.show()
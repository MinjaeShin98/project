import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('', encoding='cp949')

print(df.head())
print(df.shape)
print(df)

df1 = pd.read_csv('', encoding='cp949')
N = 30
with open('', encoding='cp949') as myfile:
    head = [next(myfile) for x in range(N)]
print(len(head))
for l in head:
    print(l)
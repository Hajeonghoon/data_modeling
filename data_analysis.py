import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv(r'C:\data_\company_data.csv',  encoding='cp949')
print(csv_data.head())

csv_data.set_index('Unnamed: 0', inplace=True)

# 월별 그래프 그리기
for column in csv_data.columns:
    plt.plot(csv_data.index, csv_data.loc[:, column], marker='o', label=column)

# 그래프 축 레이블과 제목 설정
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Monthly Data')

# 범례 표시
plt.legend()

# 그래프 보여주기
plt.show()
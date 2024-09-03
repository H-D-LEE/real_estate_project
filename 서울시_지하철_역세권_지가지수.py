import pandas as pd
import requests
from io import BytesIO
import seaborn as sns
import matplotlib.pyplot as plt

# GitHub raw 파일 URL
url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EC%A7%80%ED%95%98%EC%B2%A0_%EC%97%AD%EC%84%B8%EA%B6%8C_%EC%A7%80%EA%B0%80%EC%A7%80%EC%88%98.xlsx'

# 파일 가져오기
response = requests.get(url)

if response.status_code == 200:
    # 엑셀 파일을 pandas로 읽기 (openpyxl 엔진 사용)
    file_decoded = BytesIO(response.content)
    df = pd.read_excel(file_decoded, engine='openpyxl')

# '시도', '시군구'를 인덱스로 설정
df.set_index(['시도', '시군구'], inplace=True)

# 열 이름을 연도로 변환
df.columns = pd.to_datetime(df.columns, format='%Y년 %m월').year

# 연도로 그룹핑하고 평균값 계산
df_grouped = df.groupby(level=0, axis=1).mean()

# 히트맵 그리기
plt.figure(figsize=(12, 8))
sns.heatmap(df_grouped, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("연도별 평균값 히트맵")
plt.show()

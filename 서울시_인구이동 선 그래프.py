import pandas as pd
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# GitHub raw 파일 URL
url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EC%9D%B8%EA%B5%AC%EC%9D%B4%EB%8F%99.xlsx'

# 파일 가져오기
response = requests.get(url)
if response.status_code == 200:
    # 엑셀 파일을 pandas로 읽기 (openpyxl 엔진 사용)
    file_decoded = BytesIO(response.content)
    df = pd.read_excel(file_decoded, engine='openpyxl', index_col=0)

    # 열 이름 수정 (원하는 형식으로 변경)
    df.columns = ['2013_입', '2013_출', '2014_입', '2014_출', '2015_입', '2015_출', 
                  '2016_입', '2016_출', '2017_입', '2017_출', '2018_입', '2018_출', 
                  '2019_입', '2019_출', '2020_입', '2020_출', '2021_입', '2021_출', 
                  '2022_입', '2022_출', '2023_입', '2023_출']

# 데이터 확인
print(df.columns)

# 서울특별시 데이터 선택
seoul_data = df.loc['서울특별시']

# 연도별 데이터 추출
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
total_in = seoul_data[[f'{year}_입' for year in years]].values  # '_입' 열을 사용하여 총전입 데이터 추출
total_out = seoul_data[[f'{year}_출' for year in years]].values  # '_출' 열을 사용하여 총전출 데이터 추출

# 연도별 총전입 및 총전출 데이터 시각화
plt.figure(figsize=(10, 6))
plt.plot(years, total_in.flatten(), marker='o', label='총전입')
plt.plot(years, total_out.flatten(), marker='o', label='총전출')

plt.title('서울특별시 연도별 총전입 및 총전출 인구')
plt.xlabel('연도', labelpad = 10)
plt.ylabel('인구 수 (명)', rotation = 0, labelpad = 35)

# y축 숫자 형식 변경 (과학적 표기법 대신 일반 숫자)
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

plt.legend()

# 그래프 표시
plt.show()
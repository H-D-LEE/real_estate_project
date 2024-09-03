import pandas as pd
import requests
import pandas as pd
import requests
from io import BytesIO
import folium
import json

# GitHub raw 파일 URL
url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EC%86%8C%EB%B9%84%EC%9E%90%EB%AC%BC%EA%B0%80_%ED%99%98%EC%9C%A8_2013_2023.xlsx'

# 파일 가져오기
response = requests.get(url)

if response.status_code == 200:
    # 엑셀 파일을 pandas로 읽기 (openpyxl 엔진 사용)
    file_decoded = BytesIO(response.content)
    df = pd.read_excel(file_decoded, engine='openpyxl')

    # 연도와 월별 데이터만 선택 (첫 번째 열은 '지 역'이고 나머지는 가격 데이터)
    price_data = df.iloc[:, 1:]  # 첫 번째 열은 제외하고 나머지 열 선택
    price_data.set_index(df['통계표'], inplace=True)  # '시도'를 인덱스로 설정

price_data
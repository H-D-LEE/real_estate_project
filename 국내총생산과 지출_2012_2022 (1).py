import pandas as pd
import requests
from io import BytesIO

# REST API 엔드포인트 URL (이 예시는 가상의 API URL입니다)
api_url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EA%B5%AD%EB%82%B4%EC%B4%9D%EC%83%9D%EC%82%B0%EA%B3%BC%20%EC%A7%80%EC%B6%9C_2012_2022.xlsx'

# API에서 데이터 가져오기
response = requests.get(api_url)

if response.status_code == 200:
    # API 응답 데이터를 pandas로 읽기
    file_decoded = BytesIO(response.content)
    df = pd.read_excel(file_decoded, engine='openpyxl')

    # 불러온 데이터 출력
    print(df.to_string(index=False))
else:
    print(f"API 요청 실패: {response.status_code}")

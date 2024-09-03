import pandas as pd
import requests
from io import BytesIO

# REST API 엔드포인트 URL (이 예시는 가상의 API URL입니다)
api_url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/GDP%20%EC%84%B1%EC%9E%A5%EB%A5%A0_2013_2023.xlsx'

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

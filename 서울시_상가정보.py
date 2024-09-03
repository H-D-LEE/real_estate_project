import pandas as pd
import requests
from io import BytesIO

# GitHub raw 파일 URL
url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EC%83%81%EA%B0%80%EC%A0%95%EB%B3%B4.csv'

# 파일 가져오기
response = requests.get(url)

if response.status_code == 200:
    # CSV 파일을 pandas로 읽기, 인코딩을 'EUC-KR'로 지정
    file_decoded = BytesIO(response.content)
    df = pd.read_csv(file_decoded, encoding='cp949')

df
import pandas as pd
import requests
from io import BytesIO

# GitHub raw 파일 URL
url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EB%AC%BC%EA%B0%80%EC%83%81%EC%8A%B9%EB%A5%A0_%EB%AC%BC%EA%B0%80%EC%A7%80%EC%88%98_%ED%99%98%EC%9C%A8.xlsx'

# 파일 가져오기
response = requests.get(url)

if response.status_code == 200:
    # 엑셀 파일을 pandas로 읽기 (openpyxl 엔진 사용)
    file_decoded = BytesIO(response.content)
    df = pd.read_excel(file_decoded, engine='openpyxl')

df
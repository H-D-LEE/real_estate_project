import pandas as pd
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# GitHub raw 파일 URL
url = 'https://raw.githubusercontent.com/aaqq8/SteadyEstate/main/%EB%AC%BC%EA%B0%80%EC%83%81%EC%8A%B9%EB%A5%A0_%EB%AC%BC%EA%B0%80%EC%A7%80%EC%88%98_%ED%99%98%EC%9C%A8.xlsx'

# 파일 가져오기
response = requests.get(url)
if response.status_code == 200:
    # 엑셀 파일을 pandas로 읽기
    file_decoded = BytesIO(response.content)
    df = pd.read_excel(file_decoded, engine='openpyxl')

    # '연월'을 datetime 형식으로 변환하고, 연도 추출
    df['연월'] = pd.to_datetime(df['연월'])
    df['연도'] = df['연월'].dt.year

    # 연도별 평균 계산
    df_yearly = df.groupby('연도').mean()

    # 그래프 그리기
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # 소비자물가 상승률
    axs[0].plot(df_yearly.index, df_yearly['소비자물가 상승률'], color='blue', marker='o', label='소비자물가 상승률')
    axs[0].set_title('연도별 소비자물가 상승률')
    axs[0].set_xlabel('연도', labelpad = 10)
    axs[0].set_ylabel('소비자물가 상승률 (%)', rotation = 0, labelpad = 60)
    axs[0].legend()
    axs[0].set_xticks(df_yearly.index)
    axs[0].set_xticklabels(df_yearly.index)

    # 소비자물가지수
    axs[1].plot(df_yearly.index, df_yearly['소비자물가지수'], color='green', marker='o', label='소비자물가지수')
    axs[1].set_title('연도별 소비자물가지수')
    axs[1].set_xlabel('연도', labelpad = 10)
    axs[1].set_ylabel('소비자물가지수', rotation = 0, labelpad = 50)
    axs[1].legend()
    axs[1].set_xticks(df_yearly.index)
    axs[1].set_xticklabels(df_yearly.index)

    # 환율
    axs[2].plot(df_yearly.index, df_yearly['환율'], color='red', marker='o', label='환율')
    axs[2].set_title('연도별 환율')
    axs[2].set_xlabel('연도', labelpad = 10)
    axs[2].set_ylabel('환율 (원)', rotation = 0, labelpad = 30)
    axs[2].legend()
    axs[2].set_xticks(df_yearly.index)
    axs[2].set_xticklabels(df_yearly.index)

    plt.tight_layout()
    plt.show()

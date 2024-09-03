# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:26:22 2024

@author: user
"""

import requests
import pandas as pd
import json

# 수집할 원룸 매물 ID 목록 설정 41960770까지 존재
oneroom_ids = range(39640000, 39740000)  # 예시로 ID 범위를 설정, 실제 ID 범위를 설정하세요.

# 수집된 데이터를 저장할 리스트
data_list = []

# 각 ID에 대해 데이터 수집
for oneroom_id in oneroom_ids:
    print(f"Processing ID: {oneroom_id}")
    url = f"https://apis.zigbang.com/v3/items/{oneroom_id}"
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    requests.get(url, headers=headers)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            # 전체 JSON 데이터 가져오기
            data = response.json()
            
            # 데이터를 리스트에 추가
            data_list.append(data)
            
        except Exception as e:
            print(f"Error processing ID: {oneroom_id}, Error: {str(e)}")
            continue
    else:
        print(f"Failed to retrieve data for ID: {oneroom_id}, Status Code: {response.status_code}")

# 데이터프레임 생성 (모든 컬럼 포함)
df = pd.DataFrame(data_list)

# 파일 경로 설정
xlsx_file_path = 'C:/Users/user/Documents/python/project_ex/all_oneroom_data04.xlsx'

# 데이터프레임을 xlsx 파일로 저장 (모든 컬럼 포함)
df.to_excel(xlsx_file_path, index=False)

# 저장 경로 출력
print(f"Data saved to {xlsx_file_path}")
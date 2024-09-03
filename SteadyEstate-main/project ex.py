# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:44:14 2024

@author: user
"""


import pandas as pd
import requests
import json

# 수집된 데이터를 저장할 리스트
data_list = []

# 특정 ID 범위 내의 데이터를 수집
# 846000까지 매물이 있음 720000까지 크롤링 했음
for i in range(800000, 846000):  # 필요한 범위 설정 (여기서는 예시로 하나의 ID만 사용)
    print(f"Processing ID: {i}")
    
    try:
        url = f"https://apis.zigbang.com/v2/store/article/stores/{i}"
        req = requests.get(url)
        
        if req.status_code != 200:
            print(f"Failed to retrieve data for ID: {i}, Status Code: {req.status_code}")
            continue
        
        data = req.json()
        item = data.get('item', {})
        
        if not item:
            print(f"No 'item' found for ID: {i}")
            continue
        
        # 데이터 리스트에 item 추가
        data_list.append(item)
    
    except Exception as e:
        print(f"Error processing ID: {i}, Error: {str(e)}")
        continue

# 데이터프레임 생성
df = pd.DataFrame(data_list)

# 파일 경로 설정
xlsx_file_path = 'C:/Users/user/Documents/python/project_ex/all_mamul_data.xlsx'

# 데이터프레임을 xlsx 파일로 저장
df.to_excel(xlsx_file_path, index=False)

# 저장 경로 출력
print(f"Data saved to {xlsx_file_path}")
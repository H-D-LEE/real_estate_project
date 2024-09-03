# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:07:35 2024

@author: user
"""

import pandas as pd
import requests
import json

# 수집된 데이터를 저장할 리스트
data_list = []

# 특정 ID 범위 내의 데이터를 수집846001
for i in range(700001, 720001):  # 필요한 범위 설정
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
        
        # 모든 가능한 키에 대해 기본값 할당
        keys = ["section_type", "업종", "title", "sales_title", "매매금액", 
                "보증금액", "월세금액", "관리금액", "size_m2", "lat", "lng", "description", "local1", "local2", "local3"]
        
        for key in keys:
            if key not in item:
                item[key] = None  # 키가 없으면 기본값으로 None을 설정
        
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
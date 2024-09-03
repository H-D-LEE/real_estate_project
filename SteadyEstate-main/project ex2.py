# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:11:45 2024

@author: user
"""

import pandas as pd
import requests
import json

# 수집된 데이터를 저장할 리스트
data_list = []

# 특정 ID 범위 내의 데이터를 수집 21795
for i in range(10001, 21795):  # ID 범위 설정 (10001부터 21794까지)
    print(f"Processing ID: {i}")
    
    try:
        url = f"https://apis.zigbang.com/property/apartments/{i}/v1"
        req = requests.get(url)
        
        if req.status_code != 200:
            print(f"Failed to retrieve data for ID: {i}, Status Code: {req.status_code}")
            continue
        
        data = req.json()
        
        if not data:
            print(f"No data found for ID: {i}")
            continue
        
        # 데이터 리스트에 데이터 추가
        data_list.append(data)
    
    except Exception as e:
        print(f"Error processing ID: {i}, Error: {str(e)}")
        continue

# 데이터프레임 생성 및 컬럼명 설정
# 예시: 'id', 'name', 'address', 'lat', 'lng' 등의 컬럼을 포함
df = pd.DataFrame(data_list)

# 데이터가 가질 컬럼명을 지정 (필요에 맞게 수정)
# df.columns = ['id', 'name', 'address', 'lat', 'lng', 'mapImg', 'itemCnt', ...]
# 실제 데이터에 맞춰 적절한 컬럼명을 넣으세요.
df.columns = df.columns.str.replace(' ', '_')  # 공백을 밑줄로 대체 (필요시)

# 파일 경로 설정
xlsx_file_path = 'C:/Users/user/Documents/python/project_ex/all_apt_data.xlsx'

# 데이터프레임을 xlsx 파일로 저장
df.to_excel(xlsx_file_path, index=False)

# 저장 경로 출력
print(f"Data saved to {xlsx_file_path}")
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:43:53 2024

@author: user
"""

import pandas as pd
import os

# 병합할 파일들의 경로를 리스트로 저장
file_paths = [
    #'C:/Users/user/Documents/python/project_ex/all_oneroom_data01_expanded_v2.xlsx',
    'C:/Users/user/Documents/python/project_ex/all_oneroom_data_expanded.xlsx',
    'C:/Users/user/Documents/python/project_ex/all_oneroom_data0_expanded.xlsx',
    # 추가적인 파일 경로를 여기에 추가
]

# 빈 데이터프레임 리스트 생성
dataframes = []

# 각 파일을 읽어들여 데이터프레임으로 변환한 뒤 리스트에 추가
for file_path in file_paths:
    df = pd.read_excel(file_path)
    dataframes.append(df)

# 모든 데이터프레임을 하나로 병합
merged_df = pd.concat(dataframes, ignore_index=True)

# 병합된 데이터프레임을 새로운 Excel 파일로 저장
output_file_path = 'C:/Users/user/Documents/python/project_ex/oneroom_data_expanded.xlsx'
merged_df.to_excel(output_file_path, index=False)

print(f"Data saved to {output_file_path}")
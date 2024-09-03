# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:13:37 2024

@author: user
"""

import pandas as pd

# 엑셀 파일 경로 설정
file_path = 'C:/Users/user/Documents/python/project_ex/oneroom_data_expanded.xlsx'  # 파일 경로를 실제 경로로 수정하세요

# 엑셀 파일 로드
df = pd.read_excel(file_path)

# 'subwayYN' 컬럼 추가: 'subways' 컬럼의 데이터가 있으면 'O', 없으면 'X'
df['subwayYN'] = df['subways'].apply(lambda x: 'O' if eval(x) else 'X')

# 새로운 엑셀 파일로 저장
output_file_path = 'C:/Users/user/Documents/python/project_ex/oneroom_data_expanded_subway.xlsx'  # 저장할 파일 경로를 실제 경로로 수정하세요
df.to_excel(output_file_path, index=False)

print(f"Data saved to {output_file_path}")
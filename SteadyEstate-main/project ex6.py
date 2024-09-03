# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:15:18 2024

@author: user
"""

import pandas as pd

# 엑셀 파일 경로 설정
file_path = 'C:/Users/user/Documents/python/project_ex/oneroom_data_expanded_subway.xlsx'  # 파일 경로를 실제 경로로 수정하세요

# 엑셀 파일 로드
df = pd.read_excel(file_path)

# 'local1' 컬럼에 '서울'이 포함된 행만 남기기
df_seoul = df[df['local1'].str.contains('서울', na=False)]

# 새로운 엑셀 파일로 저장
output_file_path = 'C:/Users/user/Documents/python/project_ex/seoul_oneroom_data_expanded_subway.xlsx'  # 저장할 파일 경로를 실제 경로로 수정하세요
df_seoul.to_excel(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")
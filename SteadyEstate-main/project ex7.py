# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:25:26 2024

@author: user
"""

import pandas as pd

# 엑셀 파일 경로 설정
file_path = 'C:/Users/user/Documents/python/project_ex/seoul_oneroom_data_expanded_subway.xlsx'  # 파일 경로를 실제 경로로 수정하세요

# 엑셀 파일 로드
df = pd.read_excel(file_path)

# 'salesType'에 따라 데이터 필터링
df_maemae = df[df['salesType'] == '매매']
df_wolse = df[df['salesType'] == '월세']
df_jeonse = df[df['salesType'] == '전세']

# 각각의 데이터를 별도의 엑셀 파일로 저장
output_file_path_maemae = 'C:/Users/user/Documents/python/project_ex/seoul_oneroom_Sale_data.xlsx'  # 매매 파일 경로
output_file_path_wolse = 'C:/Users/user/Documents/python/project_ex/seoul_oneroom_monthly_rent_data.xlsx'   # 월세 파일 경로
output_file_path_jeonse = 'C:/Users/user/Documents/python/project_ex/seoul_oneroom_lease_data.xlsx' # 전세 파일 경로

df_maemae.to_excel(output_file_path_maemae, index=False)
df_wolse.to_excel(output_file_path_wolse, index=False)
df_jeonse.to_excel(output_file_path_jeonse, index=False)

print(f"Files saved to:\n{output_file_path_maemae}\n{output_file_path_wolse}\n{output_file_path_jeonse}")
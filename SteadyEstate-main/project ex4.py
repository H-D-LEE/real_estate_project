# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:21:06 2024

@author: user
"""

import pandas as pd
import json

# 엑셀 파일 불러오기
file_path = 'seoul_apt_subway_update.xlsx'  # 엑셀 파일 경로로 변경
df = pd.read_excel(file_path)

# 'recentlyTransaction' 컬럼에서 필요한 데이터만 추출
df['recentlyTransaction'] = df['recentlyTransaction'].apply(lambda x: json.loads(x))

# rentList만 추출
df['rentList'] = df['recentlyTransaction'].apply(lambda x: x['rentList'])

# netArea별로 데이터를 그룹화하는 함수
def group_by_net_area(rent_list):
    grouped = {}
    for item in rent_list:
        net_area = item['netArea']['m2']
        if net_area not in grouped:
            grouped[net_area] = []
        grouped[net_area].append(item)
    return grouped

# 각 행에 대해 그룹화된 데이터 생성
df['groupedTransactions'] = df['rentList'].apply(group_by_net_area)

# 결과 확인
print(df['groupedTransactions'])

# groupedTransactions를 각각의 시트로 저장하려면 아래 코드를 사용합니다.
with pd.ExcelWriter('grouped_transactions.xlsx') as writer:
    for i, row in df.iterrows():
        sheet_name = f"Sheet_{i+1}"
        grouped_data = row['groupedTransactions']
        for net_area, transactions in grouped_data.items():
            trans_df = pd.DataFrame(transactions)
            trans_df.to_excel(writer, sheet_name=f'{sheet_name}_NetArea_{net_area}', index=False)
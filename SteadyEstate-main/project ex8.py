# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:48:03 2024

@author: user
"""

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# 엑셀 파일 읽기
file_path = 'C:/Users/user/Documents/python/project_ex/seoul_store_data_with_dong_gu.xlsx'
df = pd.read_excel(file_path)

# geocoder 설정
geolocator = Nominatim(user_agent="geoapiExercises")

# 위도와 경도로 주소를 가져오는 함수
def reverse_geocode(lat, lng):
    try:
        location = geolocator.reverse((lat, lng), language='ko', exactly_one=True)
        if location:
            address = location.raw['address']
            city = address.get('city', '')
            district = address.get('district', '')
            neighborhood = address.get('neighborhood', '')
            return city, district, neighborhood
        else:
            return '', '', ''
    except GeocoderTimedOut:
        return reverse_geocode(lat, lng)  # 타임아웃 시 재시도

# 새로운 컬럼 생성
df[['local1', 'local2', 'local3']] = df.apply(lambda row: pd.Series(reverse_geocode(row['lat'], row['lng'])), axis=1)

# 결과를 엑셀 파일로 저장
output_path = 'C:/Users/user/Documents/python/project_ex/seoul_store_data.xlsx'
df.to_excel(output_path, index=False)
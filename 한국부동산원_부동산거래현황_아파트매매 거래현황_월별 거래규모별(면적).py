import requests
import pandas as pd

# API Key 설정
API_KEY_decode = '0IFLWr3lrBWyDv1TcSH9JK4V7qxk5WUIbx+H0Tf9I2yR6dmyj3piwsNkmQHrXGwZ/e15hPxQFiDlHw9OnjodEg=='

# 요청 URL 설정
req_url = "https://api.odcloud.kr/api/15068502/v1/uddi:8ab58e4f-495c-4215-ada4-d9d70c01fa58"

# API 호출 시 query string에 API Key 전달
req_parameter = {
    "serviceKey": API_KEY_decode,
    "perPage": 10000,  # 많은 데이터를 한 번에 가져오기 위해 perPage 값을 크게 설정
}

# API 요청 보내기
r = requests.get(req_url, params=req_parameter)

# 응답 상태 코드 확인
if r.status_code == 200:
    json_data = r.json()
    data = pd.DataFrame(json_data['data'])
else:
    print(f"Error: {r.status_code}, {r.text}")
    data = pd.DataFrame()  # 빈 데이터프레임 생성

# 서울과 서울의 각 구에 해당하는 데이터를 필터링하여 저장할 데이터프레임 생성
seoul_districts = [
    '서울 종로구', '서울 중구', '서울 용산구', '서울 성동구', '서울 광진구', 
    '서울 동대문구', '서울 중랑구', '서울 성북구', '서울 강북구', '서울 도봉구', 
    '서울 노원구', '서울 은평구', '서울 서대문구', '서울 마포구', '서울 양천구', 
    '서울 강서구', '서울 구로구', '서울 금천구', '서울 영등포구', '서울 동작구', 
    '서울 관악구', '서울 서초구', '서울 강남구', '서울 송파구', '서울 강동구'
]

# 결과를 저장할 데이터프레임 생성
seoul_data = pd.DataFrame()

# 먼저 서울 전체 합계를 계산
seoul_total_data = data[data['아파트매매 거래규모별'].str.startswith('서울 /')]
if not seoul_total_data.empty:
    relevant_columns = [col for col in seoul_total_data.columns if col.startswith(('2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'))]
    seoul_total_sum = seoul_total_data[relevant_columns].sum().to_frame().T
    seoul_total_sum.insert(0, '아파트매매 거래규모별', '서울')  # '서울' 이름으로 유지
    seoul_data = pd.concat([seoul_data, seoul_total_sum], ignore_index=True)

# 각 구별로 합계를 계산
for district in seoul_districts:
    district_data = data[data['아파트매매 거래규모별'].str.contains(district)]
    if not district_data.empty:
        relevant_columns = [col for col in district_data.columns if col.startswith(('2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'))]
        district_data_sum = district_data[relevant_columns].sum().to_frame().T
        district_data_sum.insert(0, '아파트매매 거래규모별', district)  # 구 이름을 유지
        seoul_data = pd.concat([seoul_data, district_data_sum], ignore_index=True)

# 데이터프레임을 월별로 정렬
sorted_columns = ['아파트매매 거래규모별'] + sorted([col for col in seoul_data.columns if col != '아파트매매 거래규모별'])
seoul_data = seoul_data[sorted_columns]

# 데이터프레임을 CSV 파일로 저장
seoul_data.to_csv('서울 아파트 매매 연도별 합산 데이터.csv', encoding='utf-8-sig', index=False)

print("CSV 파일로 저장되었습니다.")

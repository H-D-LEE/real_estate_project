import requests
import pandas as pd

# API Key 설정
API_KEY_decode = '0IFLWr3lrBWyDv1TcSH9JK4V7qxk5WUIbx+H0Tf9I2yR6dmyj3piwsNkmQHrXGwZ/e15hPxQFiDlHw9OnjodEg=='

# 요청 URL 설정
req_url = "https://api.odcloud.kr/api/15068118/v1/uddi:4251feab-9716-47d3-9332-a15c84dbf281"

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

# 서울의 구 목록
seoul_districts = [
    '종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', 
    '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', 
    '동작구', '관악구', '서초구', '강남구', '송파구', '강동구', '서울'
]

# 면적별로 데이터를 저장할 딕셔너리 생성
area_data = {}

# 모든 구에 대해 면적별 연도별 합계를 계산
for district in seoul_districts:
    for area in ['서울_330㎡이하', '서울_331~660㎡', '서울_661~1,000㎡', 
                 '서울_1,001~2,000㎡', '서울_2,001~5,000㎡', '서울_5,001~10,000㎡', 
                 '서울_10,001~33,000㎡', '서울_33,000㎡초과',
                 f'서울 {district}_330㎡이하', f'서울 {district}_331~660㎡', f'서울 {district}_661~1,000㎡', 
                 f'서울 {district}_1,001~2,000㎡', f'서울 {district}_2,001~5,000㎡', f'서울 {district}_5,001~10,000㎡', 
                 f'서울 {district}_10,001~33,000㎡', f'서울 {district}_33,000㎡초과']:
        area_specific_data = data[data['지역_거래규모'] == area]
        if not area_specific_data.empty:  # 데이터가 비어있지 않은 경우
            if area not in area_data:
                area_data[area] = {}
            for year in range(2019, 2024):  # 2019년부터 2023년까지
                yearly_columns = [col for col in area_specific_data.columns if col.startswith(str(year))]
                yearly_sum = area_specific_data[yearly_columns].sum(axis=1).sum()  # 전체 합계
                area_data[area][str(year)] = int(yearly_sum)

# 결과를 데이터프레임으로 변환
area_df = pd.DataFrame.from_dict(area_data, orient='index')

# 열 이름을 변경하여 '지역_거래규모'로 설정
area_df.reset_index(inplace=True)
area_df.rename(columns={'index': '지역_거래규모'}, inplace=True)

# 데이터프레임을 CSV 파일로 저장
area_df.to_csv('seoul_districts_yearly_area_data.csv', encoding='utf-8-sig', index=False)

print("CSV 파일로 저장되었습니다.")

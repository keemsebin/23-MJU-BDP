import re
import pandas as pd

def preprocess_text(text):
    # 특수 문자 및 숫자 제거
    cleaned_text = re.sub(r'[^가-힣a-zA-Z\s]', '', text)
    return cleaned_text

# 파일에서 데이터 읽기
with open('crawling.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

# 데이터프레임 생성
df = pd.DataFrame(columns=['Title', 'Date'])

# 결과 출력 및 데이터프레임에 저장
for row in data:
    # title과 date 분리
    split_data = row.split(',')
    title = ' '.join(split_data[:-1]).strip()

    # 특수문자 및 숫자 제거
    cleaned_title = preprocess_text(title)

    date = split_data[-1].strip()

    # 데이터프레임에 저장
    df = df.append({'Title': cleaned_title.split(), 'Date': date}, ignore_index=True)

# TXT 파일로 저장
with open('crawling_processed.txt', 'w', encoding='utf-8') as file:
    for index, row in df.iterrows():
        title_str = ' '.join(row['Title_List']) # 리스트를 공백으로 구분된 문자열로 변환
        file.write(title_str + "," + row['Date'] + "\n")

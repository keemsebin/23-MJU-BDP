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

    # <br /> 삭제
    title = title.replace('<br />', '')

    # 특수문자 및 숫자 제거
    cleaned_title = preprocess_text(title)

    date = split_data[-1].strip()

    # 결과 출력
    result = [cleaned_title, date]
    print(result)

    # 데이터프레임에 저장
    df = df.append({'Title': cleaned_title, 'Date': date}, ignore_index=True)

# 띄어쓰기를 기준으로 title 나누기
df['Title'] = df['Title'].apply(preprocess_text)

# Title 컬럼에서 띄어쓰기를 기준으로 나눈 결과를 하나의 컬럼에 넣기
df['Title'] = df['Title'].apply(lambda x: ', '.join(x.split()))

# CSV 파일로 저장
df.to_csv('crawling_processed.csv', index=False)

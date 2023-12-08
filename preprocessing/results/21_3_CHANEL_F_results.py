import pandas as pd
import re

with open('21_3_CHANEL_F.txt', 'r') as f:
    data = f.readlines()

# 숫자가 포함된 데이터만 선택
filtered_data = [line for line in data if re.search(r'\d', line)]

# '파운드' 혹은 '￡'가 포함된 라인 찾기
pound_lines = [line for line in filtered_data if '파운드' in line or '￡' in line]

# '달러', '$', '불'이 포함된 라인 찾기
dollar_lines = [line for line in filtered_data if '달러' in line or '$' in line or '불' in line]

# '유로', '€'가 포함된 라인 찾기
euro_lines = [line for line in filtered_data if '유로' in line or '€' in line]

#'원'이 포함된 라인 찾기
won_lines = [line for line in filtered_data if '원' in line]

# 출력
print('파운드, ￡가 포함된 라인 수:', len(pound_lines))
print('달러, $, 불이 포함된 라인 수:', len(dollar_lines))
print('유로, €가 포함된 라인 수:', len(euro_lines))
print('원 이 포함된 라인 수:', len(won_lines))

# 숫자를 찾기 위한 정규 표현식 패턴
pattern = re.compile(r'(\d+\.\d+)')

# 숫자와 '파운드', '￡', '달러', '$', '불' 혹은 '유로', '€'를 찾기 위한 정규 표현식 패턴
pattern_front_pound = re.compile(r'(\d+\.\d+)(파운드|￡)')
pattern_back_pound = re.compile(r'(파운드|￡)(\d+\.\d+)')
pattern_front_dollar = re.compile(r'(\d+\.\d+)(달러|\$|불)')
pattern_back_dollar = re.compile(r'(달러|\$|불)(\d+\.\d+)')
pattern_front_euro = re.compile(r'(\d+\.\d+)(유로|€)')
pattern_back_euro = re.compile(r'(유로|€)(\d+\.\d+)')

# 숫자와 '원'을 찾기 위한 정규 표현식 패턴
pattern_won = re.compile(r'(\d+)원$')

# 결과를 저장할 리스트
results = []

# 필터링된 라인에서 숫자를 찾아 1158.73로 곱하기
for line in filtered_data:
    match = pattern.search(line)
    if match:
        result = round(1158.73 * float(match.group(1)), 2)
        results.append(result)

# 파운드, 달러, 유로 처리
for line in pound_lines:
    match_front = pattern_front_pound.search(line)
    match_back = pattern_back_pound.search(line)
    if match_front:
        result = round(1597.50 * float(match_front.group(1)), 2)
        results.append(result)
    elif match_back:
        result = round(1597.50 * float(match_back.group(2)), 2)
        results.append(result)

for line in dollar_lines:
    match_front = pattern_front_dollar.search(line)
    match_back = pattern_back_dollar.search(line)
    if match_front:
        result = round(1158.73 * float(match_front.group(1)), 2)
        results.append(result)
    elif match_back:
        result = round(1158.73 * float(match_back.group(2)), 2)
        results.append(result)

for line in euro_lines:
    match_front = pattern_front_euro.search(line)
    match_back = pattern_back_euro.search(line)
    if match_front:
        result = round(1366.38 * float(match_front.group(1)), 2)
        results.append(result)
    elif match_back:
        result = round(1366.38 * float(match_back.group(2)), 2)
        results.append(result)

# 필터링된 라인에서 숫자와 '원'을 찾아 '원'을 떼고 결과에 추가
for line in filtered_data:
    match = pattern_won.search(line)
    if match:
        result = int(match.group(1))
        results.append(result)


# 결과 출력
print(f'Filtered data line count: {len(filtered_data)}')
print(f'Total result line count: {len(results)}')
for result in results:
    print(result)

# 결과를 txt 파일로 저장
with open('21_3_CHANEL_F_results.txt', 'w') as f:
    for result in results:
        f.write(str(result) + '\n')
# 파일에서 데이터를 읽어오기
with open('/content/drive/MyDrive/Colab Notebooks/BDP/23_2_NIKE_F.txt', 'r') as f:
    lines = f.readlines()

    total_lines = len(lines)  # 전처리 전의 총 라인 수
    removed_lines = 0  # 제외한 라인 수
    results = []

    for line in lines:
        items = [x.strip() for x in line.split(',')]
        if len(items) < 3:  # 콤마가 2개 미만으로 나뉘는 경우, 해당 라인 제외
            removed_lines += 1
            continue
        first = items[0]
        middle = items[1]
        last = items[-1]

        # 첫번째, 가운데, 마지막 항목 중 하나라도 빈 문자열인 경우 제외
        # 공백 외의 다른 문자가 있는지 확인
        if first and middle and last and first.isprintable() and middle.isprintable() and last.isprintable():
            results.append(', '.join([first, middle, last]))
        else:
            removed_lines += 1

    # 결과 출력
    print("전처리 전의 총 라인 수: ", total_lines)
    print("제외한 라인 수: ", removed_lines)
    print("출력된 라인 수: ", len(results))

    for result in results:
        print(result)

import pandas as pd
import re
import math

# 숫자가 포함된 데이터만 선택
filtered_data = [line for line in results if re.search(r'\d', line)]

# '파운드' 혹은 '￡'가 포함된 라인 찾기
pound_lines = [line for line in filtered_data if '파운드' in line or '￡' in line]

# '달러', '$', '불'이 포함된 라인 찾기
dollar_lines = [line for line in filtered_data if '달러' in line or '$' in line or '불' in line]

# '유로', '€'가 포함된 라인 찾기
euro_lines = [line for line in filtered_data if '유로' in line or '€' in line]

#'원'이 포함된 라인 찾기
won_lines = [line for line in filtered_data if '원' in line]

# 출력
print(f'Filtered data line count: {len(filtered_data)}')
print('파운드, ￡가 포함된 라인 수:', len(pound_lines))
print('달러, $, 불이 포함된 라인 수:', len(dollar_lines))
print('유로, €가 포함된 라인 수:', len(euro_lines))
print('원 이 포함된 라인 수:', len(won_lines))

# 숫자와 '파운드', '￡', '달러', '$', '불' 혹은 '유로', '€'를 찾기 위한 정규 표현식 패턴
pattern_front_pound = re.compile(r'(\d+(?:,\d+)*\.?\d*)(파운드|￡)')
pattern_back_pound = re.compile(r'(파운드|￡)(\d+(?:,\d+)*\.?\d*)')
pattern_front_dollar = re.compile(r'(\d+(?:,\d+)*\.?\d*)(달러|\$|불)')
pattern_back_dollar = re.compile(r'(달러|\$|불)(\d+(?:,\d+)*\.?\d*)')
pattern_front_euro = re.compile(r'(\d+(?:,\d+)*\.?\d*)(유로|€)')
pattern_back_euro = re.compile(r'(유로|€)(\d+(?:,\d+)*\.?\d*)')

# 숫자와 '원'을 찾기 위한 정규 표현식 패턴
pattern_won = re.compile(r'(\d+)원$')

# 숫자와 '백'을 찾기 위한 정규 표현식 패턴
pattern_baek = re.compile(r'(\d+)백')

# 결과를 저장할 리스트
price_results = []

# 필터링된 라인에서 숫자만 있는 경우에만 1317.65로 곱하기
for line in filtered_data:
    shop_name, product_name, price_info = line.split(', ')
    match = re.search(r'^(\d+(?:,\d+)*\.?\d*)$', price_info)
    if match:
        num = float(match.group(1).replace(',', ''))
        result = math.floor(1317.65 * num)
        price_results.append((shop_name, product_name, result))

# 파운드, 달러, 유로 처리
for line in pound_lines:
    shop_name, product_name, price_info = line.split(', ')
    match_front = pattern_front_pound.search(price_info)
    match_back = pattern_back_pound.search(price_info)
    if match_front:
        num = float(match_front.group(1).replace(',', ''))
        result =math.floor(1650.56 * num)
        price_results.append((shop_name, product_name, result))
    elif match_back:
        num = float(match_back.group(2).replace(',', ''))
        result = math.floor(1650.56 * num)
        price_results.append((shop_name, product_name, result))

for line in dollar_lines:
    shop_name, product_name, price_info = line.split(', ')
    match_front = pattern_front_dollar.search(line)
    match_back = pattern_back_dollar.search(line)
    if match_front:
        num = float(match_front.group(1).replace(',', ''))
        result = math.floor(1317.65 * num)
        price_results.append((shop_name, product_name, result))
    elif match_back:
        num = float(match_back.group(2).replace(',', ''))
        result = math.floor(1317.65 * num)
        price_results.append((shop_name, product_name, result))


for line in euro_lines:
    shop_name, product_name, price_info = line.split(', ')
    match_front = pattern_front_euro.search(line)
    match_back = pattern_back_euro.search(line)
    if match_front:
        num = float(match_front.group(1).replace(',', ''))
        result = math.floor(1435.27 * num)
        price_results.append((shop_name, product_name, result))
    elif match_back:
        num = float(match_back.group(2).replace(',', ''))
        result = math.floor(1435.27 * num)
        price_results.append((shop_name, product_name, result))

# 필터링된 라인에서 숫자와 '원'을 찾아 '원'을 떼고 결과에 추가
for line in filtered_data:
    shop_name, product_name, price_info = line.split(', ')
    match = pattern_won.search(price_info)
    if match:
        result = int(match.group(1))
        price_results.append((shop_name, product_name, result))

# 백 처리
for line in filtered_data:
    shop_name, product_name, price_info = line.split(', ')
    match = pattern_baek.search(price_info)
    if match:
        num = int(match.group(1))
        result = num * 1000000
        price_results.append((shop_name, product_name, result))

# 결과를 저장할 리스트
price_results_processed = []

for shop, product, price in price_results:
    # 상품명에서 영어를 소문자로 변환
    product = product.lower()

    # '/'나 '.'을 ','로 치환
    product = product.replace('/', ',').replace('.', ',')

    # '나이키'나 'nike'를 제거
    product = product.replace('나이키', '').replace('nike', '')
    # '('나')' 제거
    product = product.replace('(', '').replace(')', '')
    # 처리가 끝난 결과를 새로운 리스트에 추가
    price_results_processed.append((shop, product.strip(), price))

# 결과 출력
print(f'Filtered data line count: {len(filtered_data)}')
print(f'Total result line count: {len(price_results_processed)}')

for result in price_results_processed:
    print(result)

# 결과를 파일에 저장
with open('/content/drive/MyDrive/Colab Notebooks/BDP/23_2_NIKE_F_new.txt', 'w') as f:
    for result in price_results_processed:
        f.write(', '.join(map(str, result)) + '\n')
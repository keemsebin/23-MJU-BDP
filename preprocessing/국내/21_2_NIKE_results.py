# 국내 전처리

import re
import unicodedata

brand = '나이키'

def remove_emoji(string):
    return ''.join(c for c in string if unicodedata.category(c) not in ['So', 'Cn'])

# '/' 문자 앞뒤에 공백이 있는 경우 이를 먼저 제거한 후 ','로 치환하는 함수
def replace_slash(string):
    return re.sub(r'\s?/\s?', ',', string).strip()

# '.' 문자를 찾아 이를 ','로 치환하는 함수
def replace_period(string):
    return string.replace('.', ',')

# '('나 ')'를 찾아 이를 제거하는 함수
def remove_parentheses(string):
    return string.replace('(', '').replace(')', '')

# brand를 찾아 이를 제거하는 함수
def remove_brand(string):
    return string.replace(brand, '')

with open('/content/drive/MyDrive/Colab Notebooks/BDP/21_2_NIKE.txt', 'r') as f:
    lines = f.readlines()

total_lines = len(lines)
removed_lines = 0
results = []

for line in lines:
    parts = line.split(',', 2)
    items = [re.sub(r'(\d),(\d)', r'\1\2', part.strip()) for part in parts]

    if len(items) < 3:
        removed_lines += 1
        continue
    first = items[0]
    middle = items[1]
    last = items[-1]

    if not re.search(r'\d', last):
        removed_lines += 1
        continue

    last = re.sub(r'\D', '', last)

    if len(last) >= 8:
        removed_lines += 1
        continue

    first = remove_emoji(first).lower()  # 문자열에서 영어를 찾아 모두 소문자로 바꾸는 코드 추가
    middle = remove_brand(remove_parentheses(replace_period(replace_slash(remove_emoji(middle))))).lower()  # '나이키'를 찾아 이를 제거하는 코드 추가
    last = remove_emoji(last)

    if first and middle and last and first.isprintable() and middle.isprintable() and last.isprintable():
        results.append(', '.join([first, middle, last]))
    else:
        removed_lines += 12

print("전처리 전의 총 라인 수: ", total_lines)
print("제외한 라인 수: ", removed_lines)
print("출력된 라인 수: ", len(results))

for result in results:
    print(result)

with open('/content/drive/MyDrive/Colab Notebooks/BDP/21_2_NIKE_new.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')

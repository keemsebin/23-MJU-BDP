import re

# 숫자를 찾기 위한 정규 표현식 패턴
pattern = re.compile(r'(\d+,\d+|\d+)')
# '만원' 혹은 '만'을 포함하는 패턴
pattern_million = re.compile(r'(\d+)(만원|만)')

# 결과를 저장할 리스트
results = []

# 파일에서 데이터를 읽어오기
with open('/content/drive/MyDrive/Colab Notebooks/BDP/23_3_CHANEL.txt', 'r') as f:
    lines = f.readlines()

    # 각 라인에서 숫자를 찾아 처리하기
    for line in lines:
        match_million = pattern_million.search(line)
        if match_million:  # '만원' 혹은 '만'을 포함하는 경우
            num = int(match_million.group(1)) * 10000  # '만원' 혹은 '만'을 10000으로 바꿔서 앞의 숫자와 곱하기
            results.append(str(num))
            continue  # 다음 라인으로 넘어가기

        match = pattern.search(line)
        if match:
            num = match.group().replace(',', '')  # 쉼표 제거
            results.append(num)

# 결과 출력
for result in results:
    print(result)

# 결과를 파일에 저장하기
with open('/content/drive/MyDrive/Colab Notebooks/BDP/23_3_CHANEL_results.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')
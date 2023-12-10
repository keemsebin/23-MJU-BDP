import sys

null_count = 0

# 매퍼
def mapper(line):
    line = line.strip()
    words, date = line.split(',')
    date = date.rstrip('.')  # 마지막 '.' 제거
    if not words or not date:  # words 또는 date가 None 또는 빈 문자열인 경우
        global null_count
        null_count += 1
        return

    year, month = date.split('.')
    month = int(month)
    quarter = (month - 1) // 3 + 1  # 분기 계산

    for word in words.split():
        key = (quarter, word)  # 분기와 단어를 키로 사용
        if key not in mapper_out:
            mapper_out[key] = 0
        mapper_out[key] += 1

# 리듀서
def reducer(mapper_out):
    reducer_out = {}  # 리듀서의 출력을 저장할 딕셔너리

    for key, value in mapper_out.items():
        quarter, word = key
        if quarter not in reducer_out:
            reducer_out[quarter] = []
        reducer_out[quarter].append((word, value))

    # 각 분기별로 카운트된 횟수에 따라 단어 정렬
    for quarter in reducer_out:
        reducer_out[quarter].sort(key=lambda x: x[1], reverse=True)

    return reducer_out

# 파일 읽기
with open('crawling_processed.txt', 'r') as f:
    lines = f.readlines()

# 매퍼 실행
mapper_out = {}  # 매퍼의 출력을 저장할 딕셔너리
for line in lines:
    mapper(line)

# 리듀서 실행 및 결과 출력
reducer_out = reducer(mapper_out)
for quarter in sorted(reducer_out.keys()):
    print(f'분기: {quarter}')
    for word, count in reducer_out[quarter][:20]:  # 가장 많이 카운트된 단어 20개 추출
        print(word, count)

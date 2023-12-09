import re

# 파일에서 데이터를 읽어오기
with open('/content/drive/MyDrive/Colab Notebooks/BDP/23_3_CHANEL.txt', 'r') as f:
    lines = f.readlines()

    total_lines = len(lines)  # 전처리 전의 총 라인 수
    removed_lines = 0  # 제외한 라인 수
    results = []

    for line in lines:
        # 맨 앞과 맨 뒤의 콤마를 기준으로 세 부분으로 나누기
        parts = line.split(',', 2)
        # 숫자 사이의 콤마를 무시하기 위해 정규 표현식 사용
        items = [re.sub(r'(\d),(\d)', r'\1\2', part.strip()) for part in parts]

        if len(items) < 3:  # 콤마가 2개 미만으로 나뉘는 경우, 해당 라인 제외
            removed_lines += 1
            continue
        first = items[0]
        middle = items[1]
        last = items[-1]

        # 가격 부분에 숫자가 없는 경우 제외
        if not re.search(r'\d', last):
            removed_lines += 1
            continue

        # 가격 부분에서 숫자 이외의 모든 문자 제거
        last = re.sub(r'\D', '', last)

        # 가격 부분에서 숫자가 8자리 이상인 경우 제외
        if len(last) >= 8:
            removed_lines += 1
            continue

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

 # 결과를 파일에 저장
with open('/content/drive/MyDrive/Colab Notebooks/BDP/23_3_CHANEL_results.txt', 'w') as f:
        for result in results:
            f.write(result + '\n')
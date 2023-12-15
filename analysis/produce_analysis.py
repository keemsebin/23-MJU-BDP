from collections import Counter

# 결과를 저장할 Counter 객체 생성
counter_store = Counter()
counter_product = Counter()

# 가격들을 저장할 리스트 생성
prices = []

with open('/content/drive/MyDrive/BDP/KoreaData/2023_NIKE.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    # 각 라인을 콤마로 분리
    items = line.split(',')
    store = items[0].lower().replace(" ", "")
    counter_store[store] += 1

    if len(items) > 1:
        product = items[1].replace(" ", "").strip()
        counter_product[product] += 1
    if len(items) > 2:
        price = items[2].strip()
        if price.isdigit():
            prices.append(int(price))

print("판매처의 등장 횟수 (Top 5):")
for store, count in counter_store.most_common(5):
    print(store, count)

print("---------------------------------------")
print("상품명의 등장 횟수 (Top 5):")
for product, count in counter_product.most_common(5):
    print(product, count)
print("---------------------------------------")

# 가격들의 평균을 계산하고 출력
if prices:
    average_price = int(sum(prices) / len(prices))
    print("가격의 평균:", average_price)

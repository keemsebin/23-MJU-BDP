from collections import Counter

counter_store = Counter()
counter_product = Counter()

keyword = 'dunk'

keyword_prices = []

with open('/content/drive/MyDrive/BDP/ForeignData/2023_NIKE_F_new.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    items = line.split(',')
    store = items[0].lower().replace(" ", "")
    counter_store[store] += 1

    if len(items) > 1:
        product = items[1].replace(" ", "").strip()
        counter_product[product] += 1

        # 만약 키워드가 상품명 안에 포함되어 있다면 상품가격을 추가
        if keyword.lower() in product.lower() and len(items) > 2:
            price = items[2].strip()
            if price.isdigit():
                keyword_prices.append(int(price))

if keyword_prices:
    keyword_average_price = int(sum(keyword_prices) / len(keyword_prices))
    print(f"Average price of products containing '{keyword}':", keyword_average_price)
else:
    print(f"No products containing '{keyword}' were found.")

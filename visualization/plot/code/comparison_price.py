import pandas as pd
import matplotlib.pyplot as plt

# 국내 가격과 해외 가격 데이터 예시
data = {
    'Year': ['2021', '2022', '2023'],
    'Domestic Price': [95080, 260435, 134449],
    'Foreign Price': [88942, 94352, 100236]
}

df = pd.DataFrame(data)

# 막대그래프 그리기
ax = df.plot(x='Year', y=['Domestic Price', 'Foreign Price'], kind='bar', figsize=(10, 6))

# 각 값 표시
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

plt.title('Comparison between Domestic Price and Foreign Price')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

import matplotlib.pyplot as plt

year = [2021]
domestic_sales = [104882]
international_sales = [83814]

bar_width = 0.35

r1 = range(len(year))
r2 = [x + bar_width for x in r1]

plt.bar(r1, domestic_sales, color='purple', width=bar_width, label='Domestic')
plt.bar(r2, international_sales, color='orange', width=bar_width, label='International')

plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Comparison')

plt.xticks([r + bar_width/2 for r in range(len(year))], year)

for i, v in enumerate(domestic_sales):
    plt.text(i, v, str(v), ha='center', va='bottom', color='black')
for i, v in enumerate(international_sales):
    plt.text(i + bar_width, v, str(v), ha='center', va='bottom', color='black')

plt.legend()

plt.show()

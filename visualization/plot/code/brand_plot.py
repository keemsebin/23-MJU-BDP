# 나눔 폰트 설치

# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for i, quarter in enumerate(sorted(reducer_out.keys())):
    words, counts = zip(*reducer_out[quarter][:10])  # 단어와 빈도를 분리

    words = words[1:]
    counts = counts[1:]

    axs[i].bar(words, counts, color='skyblue')
    axs[i].set_title(f'{quarter}분기')
    axs[i].set_xlabel('단어')
    axs[i].set_ylabel('빈도')
    axs[i].set_xticks(words)  #
    axs[i].set_xticklabels(words, rotation=45)
    axs[i].set_ylim(100, 300)

plt.tight_layout()
plt.show()

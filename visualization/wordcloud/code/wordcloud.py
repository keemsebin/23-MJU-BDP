# 연도별 wordcloud 추출
import matplotlib.font_manager as fm

# 설치된 폰트 확인 및 경로 저장
fontpath = '/content/drive/MyDrive/NanumGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np

# 텍스트 파일을 읽어오는 코드
with open('/content/drive/MyDrive/BDP/ForeignData/2023_NIKE_F_new.txt', 'r') as f:
    lines = f.readlines()

# 상품명만 추출해서 text에 저장
text = ""
for line in lines:
    split_line = line.split(',')  # 콤마로 구분
    if len(split_line) > 2:  # 상품명이 있는 경우에만
        text += split_line[1].strip() + ' '  # 상품명을 text에 추가

# WordCloud 생성

# WordCloud 생성
wordcloud = WordCloud(
    font_path = fontpath,
    background_color='white',
    width = 1000,
    height = 500).generate(text)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis('off')

plt.savefig('2023_F_NIKE.png', bbox_inches='tight')
plt.show()

import matplotlib.pyplot as plt 
from wordcloud import WordCloud 
import konlpy
from konlpy.tag import Okt 
from collections import Counter

korean_text = open('/content/drive/MyDrive/BDP/23_3_CHANEL.txt', encoding = 'utf-8').read()
t = Okt ()
tokens = t.nouns (korean_text)
count = Counter (tokens)
tags = count.most_common (10)
print (type(tags))
dict_tags = dict(tags)
print (dict_tags)

wordcloud = WordCloud(font_path ="/content/drive/MyDrive/BDP/NanumGothic.ttf",background_color='white',width=1000, height=500, max_font_size=100).generate(korean_text)

plt.figure(figsize=(10, 5)) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off")
plt.savefig('2023_CHANEL.png', bbox_inches='tight',dpi=300)
plt.show()
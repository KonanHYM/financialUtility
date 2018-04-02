# -*- coding: utf-8 -*-

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 加载自定义分词字典
commandTest = "pdf2htmlEX --zoom 1.5 --split-pages 1 aaa.pdf --page-filename aaa_%d.html"
jieba.load_userdict("news.txt")

# 语料
corpos = "美媒称，鉴于全球石油市场过度供给的情况，中国原油需求下滑是其首要担忧之一。过量生产拉低了石油价格，但是中国过去一年左右的疲弱需求引发了缓慢的回弹。"

seg_list = jieba.cut(corpos)
seg_list2 = jieba.cut(corpos)
text = " ".join(seg_list)

# 词频统计
segStat = {}
for seg in seg_list2:
    if seg in segStat:
        segStat[seg] += 1
    else:
        segStat[seg] = 1
print segStat

# 创建词云
wordcloud = WordCloud(background_color="black").generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

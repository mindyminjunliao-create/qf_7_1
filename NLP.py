from jqdata import *
import datetime
yesterday = datetime.date.today() - datetime.timedelta(days=1)
q = query(finance.CCTV_NEWS).filter(finance.CCTV_NEWS.day==yesterday)
news = finance.run_query(q)
news.head(5)

text = news.iloc[13, 3]
text

text = text.replace(' ', '')
text = text.replace('\r\n', '')
text = text.replace('\n', '')
text

import jieba
words = jieba.cut(text)
words = ' '.join(words)
words

word_list = jieba.lcut(text)
word_list[:30]

word = ''
stopwords = [line.strip() for line in open('stopwords.txt', encoding='UTF-8').readlines()]
for element in words:
    if element not in stopwords:
        word += element
word



import jieba.analyse
jieba.analyse.set_stop_words("stopwords.txt")
tags = jieba.analyse.extract_tags(text, withWeight=False)
tags

tags = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
tags

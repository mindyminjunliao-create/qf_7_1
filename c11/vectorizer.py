from jqdata import *
import datetime
import jieba
import pandas as pd
yesterday = datetime.date.today() - datetime.timedelta(days=1)
q = query(finance.CCTV_NEWS).filter(finance.CCTV_NEWS.day==yesterday)
news = finance.run_query(q)
news.head()

message = news.iloc[7][3]
message = ''.join(message.split())
words=''
stopwords = [line.strip() for line in open('stopwords.txt', encoding = 'UTF-8').readlines()]
word = ' '.join(jieba.cut(message))
for w in word:
    if w not in stopwords:
        words += w
words

#using sklearn to vectorize
#method1: using the frequency of a word in a text
from sklearn.feature_extraction.text import CountVectorizer
with open('message.txt', 'w') as f:
    f.write(words)
vect = CountVectorizer()
f = open('message.txt', 'r')
vect.fit(f)

f = open('message.txt')
vectors = vect.transform(f)
print(vectors.toarray())

#method2: TF-IDF-inverse document frequency-measure if a word can distinguish a text from other texts
from sklearn.feature_extraction.text import CountVectorizer
with open('message.txt', 'w') as f:
    f.write(words)
vect = CountVectorizer()
f = open('message.txt', 'r')
vect.fit(f)

f = open('message.txt')
vectors = vect.transform(f)
print(vectors.toarray())

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
f = open('message.txt')
vect_tf = tfidf.fit_transform(f)
print(vect_tf.toarray()[0][:10])

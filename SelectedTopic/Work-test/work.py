from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
import re
from collections import Counter

f = open("CH3I/wiki/wiki_article_0.txt", "r")
f1 = open("CH3I/wiki/wiki_article_1.txt", "r")
f2 = open("CH3I/wiki/wiki_article_2.txt", "r")
f3 = open("CH3I/wiki/wiki_article_3.txt", "r")
f4 = open("CH3I/wiki/wiki_article_4.txt", "r")
f5 = open("CH3I/wiki/wiki_article_5.txt", "r")
f6 = open("CH3I/wiki/wiki_article_6.txt", "r")
f7 = open("CH3I/wiki/wiki_article_7.txt", "r")
f8 = open("CH3I/wiki/wiki_article_8.txt", "r")
f9 = open("CH3I/wiki/wiki_article_9.txt", "r")

file5 = [f, f1, f2, f3, f4, f5, f6, f7, f8, f9]
result = []
for i in range(10):
    article = file5[i].read()
    tokens = word_tokenize(article)
    lower_tokens = [l.lower() for l in tokens]
    bow_simple = Counter(lower_tokens)
    alpha_only = [t for t in lower_tokens if t.isalpha()]
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    bow = Counter(lemmatized)
    result.append(bow)
    print(result[i].most_common(1))


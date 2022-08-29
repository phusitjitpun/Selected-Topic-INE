from traceback import print_tb
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
import itertools

from gensim.models.tfidfmodel import TfidfModel

articles = []
for i in range(10) :

    f = open(f".\CH3I\wiki\wiki_article_{i}.txt", "r")
    article = f.read()

    tokens = word_tokenize(article)

    lower_tokens = [t.lower() for t in tokens]

    alpha_only = [t for t in lower_tokens if t.isalpha()]

    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]

    wordnet_lemmatizer = WordNetLemmatizer()

    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

    articles.append(lemmatized)

dictionary = Dictionary(articles)

computer_id = dictionary.token2id.get(input("Search a word: "))
print('Result: ', dictionary.get(computer_id))

corpus = [dictionary.doc2bow(a) for a in articles]

doc = corpus[2]

bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

print('Top 5 high frequency using Bow: ')
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)

tfidf = TfidfModel(corpus)

tfidf_weights = tfidf[doc]

sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

print('Top 5 high frequency using TF-IDF: ')
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)
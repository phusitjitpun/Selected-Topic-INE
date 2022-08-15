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
#Read TXT file
    f = open(f".\CH3I\wiki\wiki_article_{i}.txt", "r")
    article = f.read()
# Tokenize the article: tokens
    tokens = word_tokenize(article)
# Convert the tokens into lowercase: lower_tokens
    lower_tokens = [t.lower() for t in tokens]
# Retain alphabetic words: alpha_only
    alpha_only = [t for t in lower_tokens if t.isalpha()]
# Remove all stop words: no_stops
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
# Instantiate the WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
# Lemmatize all tokens into a new list: lemmatized
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
#list_article
    articles.append(lemmatized)

#print(articles)


# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
#print(dictionary.get(computer_id))

# Create a Corpus: corpus
corpus = [dictionary.doc2bow(a) for a in articles]

# Save the second document: doc
doc = corpus[9]

# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
#print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)
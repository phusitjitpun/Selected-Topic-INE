from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
import re
from collections import Counter

f = open("Work1/arsenal.txt", "r")
f1 = open("Work1/chelsea.txt", "r")
f2 = open("Work1/liverpool.txt", "r")
f3 = open("Work1/manCity.txt", "r")
f4 = open("Work1/manU.txt", "r")

file5 = [f, f1, f2, f3, f4]
result = []
for i in range(5):
    article = file5[i].read()
# Tokenize the article: tokens
    tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
    lower_tokens = [l.lower() for l in tokens]

# Create a Counter with the lowercase tokens: bow_simple
    bow_simple = Counter(lower_tokens)

# Retain alphabetic words: alpha_only
    alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]

# Instantiate the WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
    bow = Counter(lemmatized)

# Print the 10 most common tokens
    result.append(bow)
    print(result[i].most_common(10))

#print(len(result))

'''for i in range(len(result)):
    print(i+1)
    print(result[i].most_common(10))'''
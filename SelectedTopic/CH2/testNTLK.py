from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize

tweets = ['This is the #nlp exercise! #python', '#NLP is super fun! <3 #learning', 'Thanks @fitmkmutnb :) #nlp #python']
pattern1 = r"#\w+"
hashtags = regexp_tokenize(tweets[0], pattern1)
#print(hashtags)

pattern2 = r"([@#]\w+)"
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
#print(mentions_hashtags)

tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
#print(all_tokens)

german_text = "Wann gehen wir Pizza essen? 🍕🍕 Und fährst du mit Über? 🚕🚕"

all_words = word_tokenize(german_text)
#print(all_words)

capital_words = r"[A-ZÜ]\w+"
#print(regexp_tokenize(german_text, capital_words))

emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))
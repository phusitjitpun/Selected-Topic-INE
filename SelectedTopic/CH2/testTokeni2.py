from ast import pattern
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re

f = open("scene_one.txt", "r")
scene_one = f.read()
print(scene_one)

sentences = sent_tokenize(scene_one)
#print(sentences)

tokenized_sent = word_tokenize(sentences[3])
#print(tokenized_sent)

unique_tokens = set(word_tokenize(scene_one))
#print(unique_tokens)

match = re.search("coconuts", scene_one)
#print(match.start(), match.end())

pattern1 = r"\[.*\]"
#print(re.search(pattern1, scene_one))

pattern2 = r"[\w\s]+:"
#print(re.match(pattern2, sentences[3]))


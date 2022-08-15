from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
import re
from nltk.tokenize import regexp_tokenize

#plt.hist([1, 5, 5, 7, 7, 7, 9])
#plt.show()

#words = word_tokenize("This is a pretty cool tool!")
#word_lengths = [len(w) for w in words]
#plt.hist(word_lengths)
#plt.show()

f = open("CH2/holy_grail.txt", "r")
holy_grail = f.read()
#print(holy_grail)
lines = holy_grail.split('\n')

pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

tokenized_lines = [regexp_tokenize(s, '\w+') for s in lines]

line_num_words = [len(t_line) for t_line in tokenized_lines]
#plt.hist(line_num_words)
#plt.show()
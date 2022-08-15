from ast import pattern
import re

match_digits_and_words = ('(\d+|\w+)')
#print(re.findall(match_digits_and_words, 'He has 11 cats'))

my_str = 'match lowercase spaces nums like 12, but no commas'
match_str = ('[a-z0-9 \,]+')
#print(re.match(match_str, my_str))

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
pattern1 = r"(\w+|#\d|\?|!)"
print(re.findall(pattern1, my_string))
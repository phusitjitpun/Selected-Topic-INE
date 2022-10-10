# Import the required packages
from textblob import TextBlob
'''text = "You are so fuck stupid"
# Create a textblob object
blob_two_cities = TextBlob(text)

# Print out the sentiment
print(blob_two_cities.sentiment)'''

#Read TXT file
f = open("CH6\Titanic.txt", "r")
titanic = f.read()
# Create a textblob object
blob_titanic = TextBlob(titanic)

# Print out its sentiment
print(blob_titanic.sentiment)
import pandas as pd
movies = pd.read_csv('CH6\Train.csv')

# Find the number of positive and negative reviews
print('Number of positive and negative reviews: ', movies.label.value_counts())

# Find the proportion of positive and negative reviews
print('Proportion of positive and negative reviews: ', movies.label.value_counts() / len(movies))

length_reviews = movies.text.str.len()

# How long is the longest review
print(max(length_reviews))

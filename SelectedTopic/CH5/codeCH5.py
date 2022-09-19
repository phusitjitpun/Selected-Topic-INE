import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
from collections import Counter

# load the dataset
news_d = pd.read_csv('CH5/ch5/train.csv')
#print("Shape of News data:", news_d.shape)
#print("News data columns", news_d.columns)

# by using df.head(), we can immediately familiarize ourselves with the dataset.
#print(news_d.head())

#Text Word startistics: min, mean, max and interquartile range
txt_length = news_d.text.str.split().str.len()
#print(txt_length.describe())

#Title statistics
title_length = news_d.title.str.split().str.len()
#print(title_length.describe())

sns.countplot(x="label", data=news_d);
#print("1: Unreliable")
#print("0: Reliable")
#print("Distribution of labels:")
#print(news_d.label.value_counts());
#print(round(news_d.label.value_counts(normalize=True),2)*100);

# Constants that are used to clean the datasets
column_n = ['id', 'title', 'author', 'text', 'label']
remove_c = ['id','author']
categorical_features = []
target_col = ['label']
text_f = ['title', 'text']
ps = PorterStemmer()
wnl = nltk.stem.WordNetLemmatizer()
stop_words = stopwords.words('english')
stopwords_dict = Counter(stop_words)

# Removed unused clumns
def remove_unused_c(df,column_n=remove_c):
    df = df.drop(column_n,axis=1)
    return df

# Impute null values with None
def null_process(feature_df):
    for col in text_f:
        feature_df.loc[feature_df[col].isnull(), col] = "None"
    return feature_df

def clean_dataset(df):
    # remove unused column
    df = remove_unused_c(df)
    #impute null values
    df = null_process(df)
    return df

# Cleaning text from unused characters
def clean_text(text):
    # removing urls
    text = str(text).replace(r'http[\w:/\.]+', ' ')
    # remove everything except characters and punctuation
    text = str(text).replace(r'[^\.\w\s]', ' ')
    text = str(text).replace('[^a-zA-Z]', ' ')
    text = str(text).replace(r'\s\s+', ' ')
    text = text.lower().strip()
    return text

## Nltk Preprocessing include:
# Stop words, Stemming and Lemmatization
# For our project we use only Stop word removal
def nltk_preprocess(text):
    text = clean_text(text)
    wordlist = re.sub(r'[^\w\s]','', text).split()
    text = ' '.join([wnl.lemmatize(word) for word in wordlist if word not in stopwords_dict])
    return text

# Perform data cleaning on train and test dataset by calling clean_dataset function
df = clean_dataset(news_d)
# apply preprocessing on text through apply method by calling the function nltk_preprocess
df["text"] = df.text.apply(nltk_preprocess)
# apply preprocessing on title through apply method by calling the function nltk_preprocess
df["title"] = df.title.apply(nltk_preprocess)
# Dataset after cleaning and preprocessing step
#print(df.head())

#WordCloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# initialize the word cloud
wordcloud = WordCloud( background_color='black', width=800, height=600)
# generate the word cloud by passing the corpus
text_cloud = wordcloud.generate(' '.join(df['text']))
# plotting the word cloud
#plt.figure(figsize=(20,30))
#plt.imshow(text_cloud)
#plt.axis('off')
#plt.show()

true_n = ' '.join(df[df['label']==0]['text'])
wc = wordcloud.generate(true_n)
#plt.figure(figsize=(20,30))
#plt.imshow(wc)
#plt.axis('off')
#plt.show()

#Fine-tuning BERT
import torch
from transformers.file_utils import is_tf_available,is_torch_available, is_torch_tpu_available
from transformers import BertTokenizerFast,BertForSequenceClassification
from transformers import Trainer, TrainingArguments
import numpy as np
from sklearn.model_selection import train_test_split

import random

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    if is_torch_available():
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        # ^^ safe to call this function even if cuda is not available
    if is_tf_available():
        import tensorflow as tf
        tf.random.set_seed(seed)
set_seed(1)

# the model we gonna train, base uncased BERT
# check text classification models here:https://huggingface.co/models?filter=text-classification
model_name = "bert-base-uncased"
# max sequence length for each document/sentence sample
max_length = 512

# load the tokenizer
tokenizer = BertTokenizerFast.from_pretrained(model_name,
do_lower_case=True)

news_df = news_d[news_d['text'].notna()]
news_df = news_df[news_df["author"].notna()]
news_df = news_df[news_df["title"].notna()]

def prepare_data(df, test_size=0.2, include_title=True, include_author=True):
    texts = []
    labels = []
    for i in range(len(df)):
        text = df["text"].iloc[i]
        label = df["label"].iloc[i]
        if include_title:
            text = df["title"].iloc[i] + " - " + text
        if include_author:
            text = df["author"].iloc[i] + " : " + text
        if text and label in [0, 1]:
            texts.append(text)
            labels.append(label)
    return train_test_split(texts, labels, test_size=test_size)

train_texts, valid_texts, train_labels, valid_labels = prepare_data(news_df)

print(len(train_texts), len(train_labels))
print(len(valid_texts), len(valid_labels))
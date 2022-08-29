from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
import itertools
from gensim.models.tfidfmodel import TfidfModel
import nltk
import spacy

app = Flask(__name__, template_folder='template')

app.config["UPLOAD_FOLDER"] = "Work-NER/upload/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = file.read()   
        
    return render_template('index.html', content=content)
@app.route('/search', methods = ['GET', 'POST'])
def serech_word():
    if request.method == 'POST':
        word = request.form['word']
        dir_path = r'Work-NER/upload/'
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
    articles = []
    for i in range(count):
        f = open(f"Work-NER/upload/wiki_article_{i}.txt", "r")
        article = f.read()
        tokens = word_tokenize(article)
        lower_tokens = [t.lower() for t in tokens]
        alpha_only = [t for t in lower_tokens if t.isalpha()]
        no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
        articles.append(lemmatized)
    dictionary = Dictionary(articles)
    #print(dictionary)
    word_id = dictionary.token2id.get(word)
    msg=word
    msg1=" : There are"
    msg2=word_id
    msg3="words"
    
    return render_template('index.html',msg = msg ,msg1=msg1,msg2=msg2,msg3=msg3)

@app.route('/top', methods = ['GET', 'POST'])
def top5_word():
    if request.method == 'POST':
        dir_path = r'Work-NER/upload/'
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
    articles = []
    for i in range(count):
        f = open(f"Work-NER/upload/wiki_article_{i}.txt", "r")
        article = f.read()
        tokens = word_tokenize(article)
        lower_tokens = [t.lower() for t in tokens]
        alpha_only = [t for t in lower_tokens if t.isalpha()]
        no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
        articles.append(lemmatized)
    dictionary = Dictionary(articles)
    corpus = [dictionary.doc2bow(a) for a in articles]
    doc = corpus[0]
    tfidf = TfidfModel(corpus)
    tfidf_weights = tfidf[doc]
    sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
    msgtop = []
    msgtop2 = []
    for term_id, weight in sorted_tfidf_weights[:5]:
        a = dictionary.get(term_id), weight
        msgtop.append(a)
    bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)
    for word_id, word_count in bow_doc[:5]:
        b = dictionary.get(word_id), word_count
        msgtop2.append(b)
    return render_template('index.html', msgtop = msgtop , msgtop2 = msgtop2)
    
@app.route('/wordtype', methods = ['GET', 'POST'])
def wordtype():
    if request.method == 'POST':
        filename = request.form['filename']
        totallist = []
        person = []
        norp = []
        org = []
        gpe = []
        loc = []
        product = []
        event = []
        workart = []
        language = []
        date = []
        time = []
        percent = []
        money = []
        quantity = []
        ordinal = []
        cardinal = []
        nlp = spacy.load('en_core_web_sm')
        #part = 'wiki_article_0'
        f = open(f"Work-NER/upload/{filename}", "r")
        article = f.read()
        doc = nlp(article)
        for ent in doc.ents:
            #print(ent.ents[0],ent.ents[0].label_)
            a = ent.label_,ent.text
            #print(type(a))
            if a[0] == "CARDINAL":
                if a[1] not in cardinal:
                    cardinal.append(a[1])
            elif a[0] == "PERSON":
                if a[1] not in person:
                    person.append(a[1])
            elif a[0] == "NORP":
                if a[1] not in norp:
                    norp.append(a[1])
            elif a[0] == "ORG":
                if a[1] not in org:
                    org.append(a[1])
            elif a[0] == "GPE":
                if a[1] not in gpe:
                    gpe.append(a[1])
            elif a[0] == "LOC":
                if a[1] not in loc:
                    loc.append(a[1])
            elif a[0] == "PRODUCT":
                if a[1] not in product:
                    product.append(a[1])
            elif a[0] == "EVENT":
                if a[1] not in event:
                    event.append(a[1])
            elif a[0] == "WORK OF ART":
                if a[1] not in workart:
                    workart.append(a[1])
            elif a[0] == "LANGUAGE":
                if a[1] not in language:
                    language.append(a[1])
            elif a[0] == "DATE":
                if a[1] not in date:
                    date.append(a[1])
            elif a[0] == "TIME":
                if a[1] not in time:
                    time.append(a[1])
            elif a[0] == "PERCENT":
                if a[1] not in percent:
                    percent.append(a[1])
            elif a[0] == "MONEY":
                if a[1] not in money:
                    money.append(a[1])
            elif a[0] == "QUANTITY":
                if a[1] not in quantity:
                    quantity.append(a[1])
            elif a[0] == "ORDINAL":
                if a[1] not in ordinal:
                    ordinal.append(a[1])
        
        totallist.append(cardinal)
        totallist.append(person)
        totallist.append(norp)
        totallist.append(org)
        totallist.append(gpe)
        totallist.append(loc)
        totallist.append(product)
        totallist.append(event)
        totallist.append(workart)
        totallist.append(language)
        totallist.append(date)
        totallist.append(time)
        totallist.append(percent)
        totallist.append(money)
        totallist.append(quantity)
        totallist.append(ordinal)
    return render_template('wordtype.html', value = totallist , rgo = len(max(totallist)))
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
from typing import Text
from textblob import TextBlob, Word
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
import random
import time

app = Flask(__name__)
Bootstrap(app)

print("hello")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    startTime = time.time()
    if request.methods == 'POST':
        rawText = request.form('rawText')

        #pass raw text into textblob
        blob = TextBlob(rawText)
        recievedText = blob
        #get scores of sentiment and subjectivity
        blobSentiment, blobSubjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        #get the number of words
        numberOfTokens = len(list(blob.words))
        #what are the available nouns?
        nouns = list()
        for word, tag in blob.tags:
            if tag == "NN":
                nouns.append(word.lemmeatize())
                lenOfWords = len(nouns)
                randomWords = random.sample(nouns, len(nouns))
                finalWord=list()
                for item in randomWords:
                    word = Word(item).pluralize()
                    finalWord.append(word)
                    summary = finalWord
                    endTime = time.time()
                    finalTime = endTime - startTime
    return render_template('index.html',recieved_text=recievedText, number_of_tokens = numberOfTokens, blob_sentiment = blobSentiment, blob_subjectivity = blobSubjectivity,summary = summary, final_time=finalTime)
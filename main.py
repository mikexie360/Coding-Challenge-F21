from typing import Text
from nltk.tag.senna import SennaTagger
from textblob import TextBlob, Word
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
import random
import time

from textblob.blob import Sentence
import text2emotion as te
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = Flask(__name__)
Bootstrap(app)

print("hello")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    summary=""
    final_time=0
    startTime = time.time()

    #for individual sentence sentiment scores
    sentence_list = list()
    sentence_sentiment = list()
    sentence_subjectivity= list()

    #overall emotion
    blob_emotion = {"Happy" : 0, "Angry": 0, "Surprise": 0, "Sad":0, "Fear":0}

    #for individual sentence emotion scores
    sentence_emotion = list()

    if request.method == 'POST':

        # using textblob
        rawText = request.form['rawText']

        #pass raw text into textblob
        blob = TextBlob(rawText)
        recieved_text = blob

        #what are the available nouns?
        #nouns = list()
        
        #for overall sentiment scores
        #get scores of sentiment and subjectivity
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        #get scores for emotion for overall
        blob_emotion = te.get_emotion(rawText)
        #get the number of words
        number_of_tokens = len(list(blob.words))
        
        #for word, tag in blob.tags:
            #if tag == "NN":
                #nouns.append(word.lemmatize())
                #lenOfWords = len(nouns)
                #randomWords = random.sample(nouns, len(nouns))
                #finalWord=list()
                #for item in randomWords:
                    #word = Word(item).pluralize()
                    #finalWord.append(word)
                    #summary = finalWord
                    #endTime = time.time()
                    #final_time = endTime - startTime
        #for individual sentiment scores and overall sentiment scores using vader
        sid_obj = SentimentIntensityAnalyzer()

        number_of_sentences = len(blob.sentences)
        vader_overall = sid_obj.polarity_scores(rawText)

        vader_sentence = list()

        for sentence in blob.sentences:
            vader_sentence.append(sid_obj.polarity_scores(sentence))
        
        #for diagrams and screenshots



        print("-------------------")
        print("Overall emotions")
        print(blob_emotion)
        print("--------------------")
    return render_template('index.html',blob=blob,number_of_sentences=number_of_sentences, rawText=rawText,vader_overall=vader_overall,vader_sentence=vader_sentence, blob_emotion=blob_emotion, sentence_subjectivity=sentence_subjectivity, sentence_list=sentence_list, sentence_sentiment= sentence_sentiment,recieved_text=recieved_text, number_of_tokens = number_of_tokens, blob_sentiment = blob_sentiment, blob_subjectivity = blob_subjectivity,summary = summary, final_time=final_time)
if __name__=="__main__":
    app.run(debug=True)
# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

**----------------------------------------------------**

## Solution and Explanation
The following solution was made with Python3, Flask, textblob, vader as well as other python functions.
Using sentiment anlaysis from textblob and vader, I was able to determine what the most probable sentiment was for the overal text, each sentence, as well as the overall emotions of the text.

**How I built my program**
I was already quite knowledgeble in python and textblob from previous courses at UTD. I also already have taken some NLP courses as a student. However I did do more research on sentiment analysis and possible libraries to use.

I researched sentiment analysis using wikipedia, free online lectures on youtube, and tech articles and tutorials that go over sentiment analysis in python.

Coding the project was easier. Using a borrowed flask html file as a skeleton, I used the flask as a sort of GUI to take input from the user and output the sentiment analysis of the program.

My program uses multiple libraries.
The most important one is probable textblob. I used textblob to help parse the text to extract features to do sentiment anlaysis. However textblob was not necessary designed for sentiment anaylsis.
So I also used vader. Vader is an open source library that gives more accurate sentiment analysis according to tech articles that have done some testing comparing the two. Not only that but Vader is much better for sentiment anlysis on sentences than textblob.
text2emotion was used for calculating the overall emotion of the raw text. Not very useful for short sentences though.

**Overall Sentiment Score of the text file**
The overall sentiment score of the first text had a score of 0.188888 in polarity and 0.6242 in subjectivity according to textblob.
The overall emotion of the first text had a score of .02 happy, .14 angry, .4 surprise, .14 sad and .3 fear. With surprise and fear being the most probable scores, using text2emotion.
The overall sentiment score for the first text with vader had a score of 0.133 positve, .71 neutral, .157 negative and -0.9228 compound.

The overall sentiment score for the second text had a score of .2217 in polarity, .5857 in subjectivity according to textblob.
The overall emotion of the second text had a score of .27 happy, .02 angry, .24 surprise, .18 sad and .29 fear, using text2emotion.
The overall sentiment score for the second text with vader had a score of .215 positve, .736 neutral, .048 negative and .9979 compound.

The entire input text had an overall sentiment score of .2135 polarity, .59539 subjectivity with textblob.
The overall emotion of the overall input text had a .17 happy, .07 angry, .3 surprise, .16 sad, and .3 fear, with text2emotion.
The overall sentiment score with vader had a .173 positve, .758 neutral, .069 negative and .9978 compound.

**What the Score means, and what I expected**
In textblob, polarity is how positve, neutral and negative the sentiment of the text is. 1 is very positive, 0 is neutral and -1 is very negative.
Subjectivity is how opinionated or factual the text is. 1 is very opinionated, and 0 is very factual.
Emotions of the overall text was calculated using text2emotion. Emotions can be Happy, Angry, Surprise, Sad and Fear.
Vader has a compound score, that tells us the overall sentiment, while it also has seperate positve, neutral and negative scores. 1 in compound is overall very positve, -1 in compound is overall very negative.

Also, do not pay much attention to textblob and pay more attention to vader. Textblob is actually not a very good sentiment analysis tool. Textblob fails on more complicated pieces of text and its polarity and subjectivity cannot always be trusted. Vader is much better as sentiment analysis.

So what does this all mean?

First text file is From "Fahrenheit 451".
Fahrenheit 451 is a 1953 dystopian novel. It takes place in a future American society where books are burned.

So in our analysis we can expect to have a negative sentiment with fear and sadness as our main emotions.
However in our textblob, we see that the score is positve. After some research, I found that textblob is actually not very good at sentiment analysis, so using vader, we can see that the sentiment is overall negative with the compound score. This makes sense as the book takes place in a dystopian society. Also it makes sense for textblob to fail at times as textblob is only fairly useful for simple texts, and this book is quite advance in vocab.
In our emotions we see that the text is mainly surprise and fear which makes sense. The text has so much yelling and shouting between two characters that it makes sense for vader to sense fear and surpise in the text.

Second text file is from "The Autobiography of Benjamin Franklin".
The Autobiography of Benjamin Franklin is about the great American inventor himself. He has done many things and most likely has many positve things to write about himself.

So in our analysis we can expect to have very positive sentiment with happy as our main emotions.
And in our anlysis we can see that textblob shows that the text is mostly positve and mostly factual. Vader agrees with textblob that the text has very positive sentiment. The main emotions from text2emotion shows that the text is mostly happy, surprise and fear.
Our analysis on polarity and compound makes sense from textblob and vader. However, our emotions from text2emotion do not make as much sense. I can see why the text can be happy, but I do not see how the text can be surprising or fearful. The only explantion I can come up with after doing more research and reading the text itself, is that the book itself is quite old as it was written in 1793. Which could mean that the text2emotion is getting confused over the complex text and the old way of writing from back 200+ years ago.

Overall vader and text2emotion did a decent job at analysing the text, while textblob was more hit or miss.

**Individual Sentence Scores**
The individual sentence scores does tell us the sentiment scores for each sentence without context from adjacent sentences.
To have the individual sentence scores to give us more information, we would most likely need a graph to see how the sentiment scores in the sentences changes throughout the text.
Right now the individual sentence scores do not tell us much, its better to use the overall sentiment score of the entire text right now.

**Future**
In the future I would like to explore more python libraries for more accurate sentiment analysis, but also for individual sentence emotion analysis, and also I would like to use numpy and matplotlib.pyplot to draw graphs of how the senitment changes through out the texts.
Weather or not using a graph plot to see the change in sentiment throughout the text is useful or not may require more research, but it will help us analyze the text.

**Programming langauge, Library and API**
Used Python3, textblob, vader, text2emotion, nltk, flask.
In the future I would like to use random, time, numpy and matplotlib.pyplot
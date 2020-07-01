from textblob import TextBlob, Word, Blobber # hooking up to nltk
import tweepy # for twitter api
import numpy as np # for analysis later
import pandas as pd
import matplotlib.pyplot as plt # for mapping our data

consumer_key = 'bUe0HnRooyKBZpzo6de0ZDf4P' 
consumer_secret = 'Fx4bgDYsIwVpONwQqJZsuC4kBbc3Ib8TJywLmbJkoTcZdMepmo'
access_token = '1272931080790773763-g2ZkaDSOlc2nnhJfWLCMXhDuGkE02O'
access_token_secret = 'xtiBwgpR8kUYsMTvNXaf0VcZARgma4EYIGbMVULsF71pX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
polarity = []
subjectivity = []
tweetArr = []
polarArr = np.array([])
subArr = np.array([])

polarPos = 0
polarNeg = 0

subjectPos = 0
subjectNeg = 0

query = 'fulton county covid'
# you can change your lang to all but it returns a bunch of arabic tweets lol
public_tweets = tweepy.Cursor(api.search, q=query, rpp=100, count=200, result_type="recent", include_entities=True, lang="en").items(500) 
for i in public_tweets:
    analysis = TextBlob(i.text)
    
    polar = analysis.sentiment
    polarity.append(float(polar.polarity))
    
    subject = analysis.sentiment
    subjectivity.append(float(subject.subjectivity))

    if((subject.subjectivity < .5) and (subject.subjectivity > -.5)):
        tweetArr.append(i.text)
    
    
    if(polar.polarity > 0):
        polarPos+=1
    elif(polar.polarity < 0):
        polarNeg+=1
    else: pass
    
    if(subject.subjectivity > 0):
        subjectPos+=1
    elif(subject.subjectivity < 0):
        subejctNeg+=1
    else: pass
polarData = np.append(polarArr, polarity) 
subData = np.append(subArr, subjectivity)  
print(subData.size, " Results loaded!")
print("\nPositive polarity::  "  + str(polarPos/len(polarity)*100) + "% \tNegative polarity::  " + str(polarNeg/len(polarity)*100) + "%")
print("Positive subjectivity::  "  + str(subjectPos/len(subjectivity)*100) + "% \tNegative subjectivity::  " + str(subjectNeg/len(subjectivity)*100) + "%")
print("Median polarity:: ", np.median(polarData), "\t\t Median subjectivity::  ", np.median(subData))
# print("\n POLARITY::  ") # if you want to see each individual polarity/subjectivity
# print(polarity)
# print("\n SUBJECTIVITY::  " + str(subject))
# print(subjectivity)
    
    
print("\n TWEETS::  ")
print(tweetArr)
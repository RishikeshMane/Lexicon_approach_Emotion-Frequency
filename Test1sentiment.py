
#importing required libraries

import re
import nltk 
from nltk import word_tokenize,sent_tokenize
from typing import Counter, List
from nltk.corpus import stopwords
from nltk.util import filestring, pr
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
import csv

#taking document data from csv and also trying with small text

#below cvs is not that much practical for emotion analysis but almost resulats are same as per given in sentiment column in csv file

#in final output we are not getting maximum frequency of neutrl and worry because in emotions.txt file words which are defining neutral etc emotions are not there

csvfile=pd.read_csv('tweet_emotions.csv')
# print(csvfile.head(10))

csv_content=csvfile['content']

# csv_sentiment=csvfile['sentiment']
# csv_senti_count=[]
# for i in csv_sentiment:
#     csv_senti_count.append(i)
# print(csv_senti_count)
# xcs=Counter(csv_senti_count)
# print(xcs)

csv_text=[]
for i in csv_content:
    csv_text.append(i)

csv_words=[]
countsm=1
for i in csv_text:
    i = re.sub('[^a-zA-Z]',' ', i)
    i=i.replace('  ','')
    i=i.split()
    for f in i:
        if not f in set(stopwords.words('english')):
            csv_words.append(f)

print(csv_words)




#reading emotions.txt files for comparing words with emotions  between words in emotions data and  csv_words data 

emotions=open("emotions.txt","r+")
# emote=emotions.readline()
emotions=emotions.readlines()
count=0

test_text=open("Sentiment-Analysis/read.txt",encoding="utf-8")
tstext=test_text.readlines()
finaltx=[]
# print(tstext)
for i in tstext:
    i = re.sub('[^a-zA-Z]',' ', i)
    i=i.replace('    ',' ')
    i=i.split()
    for f in i:
        finaltx.append(f)
# print(finaltx)

#optional using dummy text for testing at small scale 
text="Initially, texts from a variety of articles in this wide range of sources will be extracted. However, there is no guarantee that the text will provide a balanced mix of sentences with all the necessary categories of emotions. In other words, since not all sentences will contain emotional cues that we are interested in, it is highly possible the proportion of “neutral” sentences outweigh those with emotional elements. To understand the impact of this, sentences are passed into a sentiment analyzer to provide basic labels of “positive”, “neutral” or “negative”. This allows us to filter the set if necessary, and gives us a rough idea of the mix of sentences that we will be putting through to the Mechanical Turk for hand-labelling those sentences that convey emotions that we are looking for."
# print(text)
for i in text:
    text=text.replace(',','')
text=text.split()
final_text=[]
for i in text:
    if not i in set(stopwords.words('english')):
        final_text.append(i)
# print(final_text)
x = Counter(final_text)
# print(x)

final_counter = []

for i in emotions:
    count=count+1
    i=i.replace("'",'').replace(",",'').replace("\n",'').strip()
    word,emotion=i.split(':')
    if word in csv_words:
        final_counter.append(emotion)   
    
ct=Counter(final_counter)
print(ct)
figure(num=None, figsize=(20,18), dpi=80, facecolor='w', edgecolor='r') 
plt.xticks(rotation=90)   
plt.bar(ct.keys(),ct.values())
plt.xlabel('Emotions')
plt.ylabel('Frequency')
plt.savefig('graph.png')
plt.show()
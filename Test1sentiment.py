from typing import Counter, List
import re
import nltk 
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.util import filestring, pr
from matplotlib import pyplot as plt

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

text="Initially, texts from a variety of articles in this wide range of sources will be extracted. However, there is no guarantee that the text will provide a balanced mix of sentences with all the necessary categories of emotions. In other words, since not all sentences will contain emotional cues that we are interested in, it is highly possible the proportion of “neutral” sentences outweigh those with emotional elements. To understand the impact of this, sentences are passed into a sentiment analyzer to provide basic labels of “positive”, “neutral” or “negative”. This allows us to filter the set if necessary, and gives us a rough idea of the mix of sentences that we will be putting through to the Mechanical Turk for hand-labelling those sentences that convey emotions that we are looking for."
# print(text)
for i in text:
    text=text.replace(',','')
# print(text)
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
    if word in finaltx:
        final_counter.append(emotion)   
    
ct=Counter(final_counter)
print(ct)    
plt.bar(ct.keys(),ct.values())
plt.show()
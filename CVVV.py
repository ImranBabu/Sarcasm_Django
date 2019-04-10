import pandas as pd
import numpy  as np
from sklearn.feature_extraction.text import CountVectorizer

data=pd.read_csv('Sarcastic.csv')

X=data['Tweet']
Y=data['Class']


cv=CountVectorizer()

x=cv.fit_transform(X)
s=[]
for i in x:
    s.append(i)
data=list(zip(s,Y))
Feature=pd.DataFrame(data,columns=['Tweet','Class'],index=False)


Feature.to_csv(r'H:/Sarcasm/Feature_list.csv')
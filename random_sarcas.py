import pandas as pd
import numpy as np

import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle

data=pd.read_csv('Sarcastic.csv')

X=data['Tweet']
y=data.Class

CV=CountVectorizer()

X=CV.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf=RandomForestClassifier()
clf.fit(X_train,y_train)
sc=clf.score(X_test,y_test)
print(sc*100)
filename="RF2.sav"
pickle.dump(clf,open(filename,"wb"))

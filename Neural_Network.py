import pandas as pd
import numpy as np

import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle

data=pd.read_csv('Sarcasm.csv',sep="	")

X=data['Tweet']
y=data.Class

CV=CountVectorizer()

X=CV.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf=MLPClassifier()
clf.fit(X_train,y_train)
sc=clf.score(X_test,y_test)

filename="NN1.sav"
pickle.dump(clf,open(filename,"wb"))
score=clf.score(X_test,y_test)
print(score*100)

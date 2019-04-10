from django.shortcuts import render,redirect
from .models import Register,Comments
import os
from django.conf import settings
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from django.http import HttpResponse

def home(request):
    return render(request,"sarcasm/sarcasm.html")

def loginv(request):
    if request.method == "POST":
        name = request.POST['name']
        pwd = request.POST['pwd']
        verified = Register.objects.get(name=name)
        if verified.pwd == pwd:
            return render(request,"sarcasm/sarcasm.html")
    return render(request,"sarcasm/Login.html")

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        pwd = request.POST['pwd']
        mailid = request.POST['mailid']
        ph = request.POST['ph']
        if name == "" or pwd == "":
            return redirect('/post/')
        else:
            reg = Register(
            name=name,
            pwd=pwd,
            mailid=mailid,
            ph=ph
            )
            reg.save()
            return render(request,"sarcasm/Login.html")
    return render(request,"sarcasm/Register.html")

def post(request):
  
    data=pd.read_csv( "E:/ML-Project/Devaraj/Sarcasm/Sarcastic.csv")
    X=data['Tweet']
    Y=data['Class']
    cv = CountVectorizer()
    X=cv.fit(X)
    clf = MultinomialNB()
    file = "E:/ML-Project/Devaraj/Sarcasm/RF2.sav"
    loaded_model = pickle.load(open(file,'rb'))
    data = Comments.objects.filter(spam="Normal")
    if request.method == "GET":
        return render(request,"sarcasm/Post.html",{'data':data})
    else:
        cmd = request.POST["cmd"]
        data = [cmd]
        vect = cv.transform(data).toarray()
        prediction = loaded_model.predict(vect)
        if prediction == 1:
            comments = Comments(
            feed=cmd,
            spam="Sarcastic"
            )
            comments.save()
            data = Comments.objects.filter(spam="Normal")
            return redirect('/post/')
        else:
            comments = Comments(
            feed=cmd,
            spam="Normal"
            )
            comments.save()
            data = Comments.objects.filter(spam="Normal")
            return redirect('/post/')
    #return HttpResponse("Empty")

# Create your views here.

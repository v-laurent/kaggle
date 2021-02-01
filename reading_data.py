import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

def clean_date(date):
    date = date.lower()
    date = date.replace(",","").replace("-"," ").replace("  "," ")
    return date   

def read_data(dataset_path):
    train_dataset = pd.read_csv(dataset_path, index_col=0)
    X_labels = ["date","org","tld","ccs","bcced","mail_type","images","urls","salutations","designation","chars_in_subject","chars_in_body"]
    Y_labels = ["updates","personal","promotions","forums","purchases","travel","spam","social"]
    X_dataset = train_dataset[X_labels]
    Y_dataset = train_dataset[Y_labels]

    #X_dataset
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    dates = ["day", "year", "hour", "minute", "second"]
    mail_types = ['multipart/mixed', 'No_mail_type', 'text/html', 'multipart/related', 'multipart/IDM', 'text/HTML', 'multipart/alternative', 'Multipart/Mixed', 'Multipart/Alternative', 'multipart/report', 'text/html ', 'text/calendar', 'multipart/signed', 'Text/Html', 'text/plain']
    other_labels = ["org","tld","ccs","bcced","images","urls","salutations","designation","chars_in_subject","chars_in_body"]
    new_labels = days + months + dates + mail_types +  other_labels

    X_train = dict( [ (label,[]) for label in new_labels ] )

    for _, row in X_dataset.iterrows():
        #date
        date = clean_date( row["date"] ).split(" ")
        for d in days:
            X_train[d].append(0)

        #if the name of the day is not provided
        decalage = 0
        if  date[0] in days: 
            X_train[ date[0] ][-1] = 1
        else:
            decalage = 1

        X_train["day"].append( date[1-decalage] )
        for m in months:
            X_train[m].append(0)
        X_train[ date[2-decalage] ][-1] = 1

        X_train["year"].append( date[3-decalage] )
        h, m, s = date[4-decalage].split(":")
        X_train["hour"].append(h)
        X_train["minute"].append(m)
        X_train["second"].append(s)
        #chars_in_subject
        if not math.isnan( row["chars_in_subject"] ):
            X_train["chars_in_subject"].append( int( row["chars_in_subject"] ) )
        else:
            X_train["chars_in_subject"].append(0)
        #mail_type
        for mail_type in mail_types:
            X_train[mail_type].append(0)
        if not row["mail_type"] in mail_types: 
            X_train["No_mail_type"][-1] = 1
        else:
            X_train[ row["mail_type"] ][-1] = 1
        #others
        for label in ["org","tld","ccs","bcced","images","urls","salutations","designation","chars_in_body"]:
            X_train[label].append( row[label] )

    return pd.DataFrame(X_train), Y_dataset


X_train, Y_train = read_data(r'C:\Users\Valen\Desktop\train_ml.csv')

X_train.to_csv('X_train.csv')
Y_train.to_csv('Y_train.csv')


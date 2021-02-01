import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from sklearn.decomposition import PCA

X_train = pd.read_csv("X_train.csv", index_col=0)
days = ["mon","tue","wed","thu","fri","sat","sun"]
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
dates = ["day", "year", "hour", "minute", "second"]
mail_types = ['multipart/mixed', 'No_mail_type', 'text/html', 'multipart/related', 'multipart/IDM', 'text/HTML', 'multipart/alternative', 'Multipart/Mixed', 'Multipart/Alternative', 'multipart/report', 'text/html ', 'text/calendar', 'multipart/signed', 'Text/Html', 'text/plain']
other_labels = ["org","tld","ccs","bcced","images","urls","salutations","designation","chars_in_subject","chars_in_body"]
Y_train = pd.read_csv("Y_train.csv", index_col=0)

#correlation matrix 
for c in other_labels[2:][::-1]:
    Y_train.insert(0, c, X_train[c], True) 

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(Y_train.corr().to_numpy()[:8,8:], interpolation='nearest')
fig.colorbar(cax)

ax.set_xticklabels(['']+['updates','personal','promotions','forums','purchases','travel','spam','social'] )
ax.set_yticklabels(['']+other_labels[2:])
plt.title("correlation matrix")
plt.show()

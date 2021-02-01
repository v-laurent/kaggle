import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train_dataset = pd.read_csv(r'C:\Users\Valen\Desktop\kaggle\train_ml.csv', index_col=0)
X_parameters = ["date","org","tld","ccs","bcced","mail_type","images","urls","salutations","designation","chars_in_subject","chars_in_body"]
Y_parameters = ["updates","personal","promotions","forums","purchases","travel","spam","social"]
X_train = train_dataset[X_parameters]
Y_train = train_dataset[Y_parameters]
"""
print(X_train[:10])

organisations = list(set(X_train["org"]))
c = []

for org in organisations:
    df_mask=X_train['org']== org
    ds = X_train[df_mask]
    c.append(len(ds))
    
    s = list(set(ds['tld']))
    if len(s) != 1:
        print(org,s)
    
print(sorted(c))

frequency = X_train["org"].value_counts()[:100]
fig, ax = plt.subplots()
frequency.plot(ax=ax, kind='bar')
plt.show()


frequency = X_train["urls"].value_counts()
fig, ax = plt.subplots()
frequency.plot(ax=ax, kind='bar')
plt.title("ccs")
plt.show()
"""

Y_train = train_dataset[Y_parameters]
plt.matshow(Y_train.corr())
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.show()

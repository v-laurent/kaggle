import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


"""
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


Y_train = train_dataset[Y_parameters]
plt.matshow(Y_train.corr())
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.show()
"""
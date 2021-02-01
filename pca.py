import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X_train = pd.read_csv("X_train.csv", index_col=0)
Y_train = pd.read_csv("Y_train.csv", index_col=0)

mail_types = ['multipart/mixed', 'No_mail_type', 'text/html', 'multipart/related', 'multipart/IDM', 'text/HTML', 'multipart/alternative', 'Multipart/Mixed', 'Multipart/Alternative', 'multipart/report', 'text/html ', 'text/calendar', 'multipart/signed', 'Text/Html', 'text/plain']
important_labels = ['hour', 'year'] + mail_types + ['ccs', 'urls', 'salutations', 'designation', 'chars_in_subject']

x = X_train[important_labels][:100]
# Standardizing the features
x = x.subtract(x.mean())
#pca
pca = PCA(n_components='mle')
principalComponents = pca.fit_transform(x)
#new dataset
PCA_X_train = pd.DataFrame(data = principalComponents)
print(PCA_X_train)
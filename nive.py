import numpy as np
from sklearn.naive_bayes import GaussianNB
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
import pandas as pd

df = pd.read_csv(r'C:\Users\adilt\Desktop\ML_HW\test.csv', header=None, sep=',',
                 names=['sha256', 'family'])

#print (len(df))
a = df.ix[1][0]
print (a)
#clf = GaussianNB()
#for i in range (len(df)):
     #x
#    y = (df.ix[i][1])

#clf.fit(X, Y)
loc = 'C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test\\'
def find(a, loc):
    for root, dirs, files in os.walk(path):
        if name in files:
            print ("found")

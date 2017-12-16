import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import shutil
df = pd.read_csv(r'C:\Users\adilt\Desktop\ML_HW\test.csv', header=None, sep=',',
                 names=['sha256', 'family'])
#asf = df.ix[2][0]
#print (asf)
#print (len(df))
for i in range(len(df)):
    srcfile = ('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\feature_vectors\\')+df.ix[i][0]
    dstroot = ('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test\\')
    shutil.move(srcfile, dstroot)

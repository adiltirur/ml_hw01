import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
import pandas as pd
df = pd.read_csv(r'C:\Users\adilt\Desktop\ML_HW\sha256_family.csv', header=None, sep=',',
                 names=['sha256', 'family'])
print (df)
train, test = train_test_split(df, train_size = 0.7)
train.to_csv(r'C:\Users\adilt\Desktop\ML_HW\train.csv', encoding='utf-8', index=False)
test.to_csv(r'C:\Users\adilt\Desktop\ML_HW\test.csv', encoding='utf-8', index=False)
#print (train)

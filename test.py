import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn import svm
df = pd.read_csv(r'C:\Users\adilt\Desktop\ML_HW\train.csv', header=None, sep=',',
                 names=['sha256', 'family'])   # columns names if no header


vect = TfidfVectorizer()
X_train = vect.fit_transform(df['sha256'])
y_train = df['family']

df = pd.read_csv(r'C:\Users\adilt\Desktop\ML_HW\test.csv', header=None, sep=',',
                 names=['sha256', 'family'])   # columns names if no header


vect = TfidfVectorizer()
X_test= vect.fit_transform(df['sha256'])
y_test = df['family']
#print (X1)
clf = svm.SVC(kernel='linear')
clf.fit(X_train,y_train)
clf.predict(X_test)

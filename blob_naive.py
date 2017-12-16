from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import sys
from time import time
test = open('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test.txt')
classify = test.readlines()

t0 = time()
for i in range(10):
    text_file_1 = open('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test_blob\\train\\malware\\'+str(i)+'.txt')
    lines = text_file_1.readlines()
    text_fil = open('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test_blob\\train\\goodware\\'+str(i)+'.txt')
    lines_1 = text_fil.readlines()
    #print (lines)
    #print (lines_1)

train = [
        (lines,'malware'),
        (lines_1,'goodware')
        ]

for j in range(4):
    text_file_2 = open('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test_blob\\test\\malware\\'+str(j)+'.txt')
    lines_test = text_file_2.readlines()
    text_fileee = open('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\test_blob\\test\\goodware\\'+str(j)+'.txt')
    lines1_test= text_fileee.readlines()
test = [
        (lines_test,'malware'),
        (lines1_test,'goodware')


]

cl = NaiveBayesClassifier(train)
print ("training time: "),
print (round(time()-t0, 3))
# Classify some text
print(cl.classify(lines1_test[10]))
print("Accuracy: {0}".format(cl.accuracy(test)))

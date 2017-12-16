from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
#for i in range(10):
text_file_1 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\0", "r")
text_file_2 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\1", "r")
text_file_3 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\2", "r")
text_file_4 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\3", "r")
text_file_5 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\4", "r")
text_file_6 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\5", "r")
text_file_7 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\6", "r")
text_file_8 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\7", "r")
text_file_9 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\8", "r")
text_file_10 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\9", "r")
lines_1 = text_file_1.readlines()
lines_2 = text_file_2.readlines()
lines_3 = text_file_3.readlines()
lines_4 = text_file_4.readlines()
lines_5 = text_file_5.readlines()
lines_6 = text_file_6.readlines()
lines_7 = text_file_7.readlines()
lines_8 = text_file_8.readlines()
lines_9 = text_file_9.readlines()
lines_10 = text_file_10.readlines()
text_file_11 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\10", "r")
text_file_12 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\11", "r")
text_file_13 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\12", "r")
text_file_14 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\13", "r")
text_file_15 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\14", "r")
text_file_16 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\15", "r")
text_file_17 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\16", "r")
text_file_18 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\17", "r")
text_file_19 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\18", "r")
text_file_20 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\train\\19", "r")
lines_11 = text_file_1.readlines()
lines_12 = text_file_2.readlines()
lines_13 = text_file_3.readlines()
lines_14 = text_file_4.readlines()
lines_15 = text_file_5.readlines()
lines_16 = text_file_6.readlines()
lines_17 = text_file_7.readlines()
lines_18 = text_file_8.readlines()
lines_19 = text_file_9.readlines()
lines_20 = text_file_10.readlines()


text_file_21 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\76", "r")
text_file_22 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\2", "r")
text_file_23 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\3", "r")
text_file_24 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\4", "r")
text_file_25 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\5", "r")
text_file_26 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\6", "r")
text_file_27 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\7", "r")
text_file_28 = open("C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\my_classification\\blob\\test\\8", "r")
lines_21 = text_file_21.readlines()
lines_22 = text_file_22.readlines()
lines_23 = text_file_23.readlines()
lines_24 = text_file_24.readlines()
lines_25 = text_file_25.readlines()
lines_26 = text_file_26.readlines()
lines_27 = text_file_27.readlines()
lines_28 = text_file_28.readlines()

train = [
    (lines_1, 'goodware'),
    (lines_2, 'goodware'),
    (lines_3, 'goodware'),
    (lines_4, 'goodware'),
    (lines_5, 'goodware'),
    (lines_6, 'goodware'),
    (lines_7, 'goodware'),
    (lines_8, 'goodware'),
    (lines_9, 'goodware'),
    (lines_10, 'goodware'),
    (lines_11, 'malware'),
    (lines_12, 'malware'),
    (lines_13, 'malware'),
    (lines_14, 'malware'),
    (lines_15, 'malware'),
    (lines_16, 'malware'),
    (lines_17, 'malware'),
    (lines_18, 'malware'),
    (lines_19, 'malware'),
    (lines_20, 'malware'),

]
test = [

    (lines_22, 'malware'),
    (lines_23, 'malware'),
    (lines_24, 'malware'),
    (lines_25, 'goodware'),
    (lines_26, 'goodware'),
    (lines_27, 'goodware'),
    (lines_28, 'goodware'),
]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify(lines_28))  # "pos"
#print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
#blob = TextBlob("The beer was amazing. But the hangover was horrible. "
    #            "My boss was not pleased.", classifier=cl)
#print(blob)
#print(blob.classify())

#for sentence in blob.sentences:
#    print(sentence)
#    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
#cl.show_informative_features(5)


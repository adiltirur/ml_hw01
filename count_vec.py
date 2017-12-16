from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(decode_error='ignore',strip_accents='unicode')
text_file = open(r"C:\Users\adilt\Desktop\corpus.txt", "r")
lines = text_file.readlines()
#print len(lines)

#print (lines)
#corpus = open('C:\\Users\\adilt\\Desktop\\corpus.txt')
#vectors = vectorizer.fit_transform(corpus).toarray()
#print (vectors)
cv = CountVectorizer()
cv_fit=cv.fit_transform(lines)

print(cv.get_feature_names())
print(cv_fit.toarray())
print(cv_fit.toarray().sum(axis=0))
text_file.close()

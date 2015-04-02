#Load, train, and classify documents.
#This serves as a prototype for experimenting with document classification. This
#module should NOT be referred to by any other classes.
from stylproj.dochandler import DocumentExtractor
from stylproj.featuresets.basic9 import Basic9Extractor
from sklearn import svm
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import chi2, SelectKBest

import codecs
import numpy as np
import matplotlib.pyplot as plt

#load our list of training document paths (original author)
labels = []
paths = []
with open("trainingDocs.txt", "r") as trainingDocs:
    for line in trainingDocs.readlines():
        paths.append(line.split(':')[0])
        labels.append(line.split(':')[1].replace('\n', ''))
        #print("Training set with label: " + line)

#load our list of test document paths
testlabels = []
testpaths = []
with open("testDocs.txt", "r") as testDocs:
    for line in testDocs.readlines():
        testpaths.append(line.split(':')[0])
        testlabels.append(line.split(':')[1].replace('\n', ''))

#load each file in our list of paths
trainingStrings = []
for path in paths:
    with codecs.open(path, "r", encoding='utf8',errors='replace') as docString:
            document = docString.read()
            trainingStrings.append(document)
   # except UnicodeDecodeError:
        #TODO: For now, we alert the user that their document is corrupted. In the
        #future, we ought to try to remove any offending characters from the
        #document and just move on.
    #    print("It appears you have tried to load a document that stylproj"
    #    " cannot read. Please remove any non-UTF-8 symbols and try again.")

#load each of our testfile path list
testStrings = []
for path in testpaths:
    with codecs.open(path, "r", encoding = 'utf8') as docString:
        document = docString.read()
        testStrings.append(document)

#extract features from each document
extractedFeats = DocumentExtractor(Basic9Extractor(), trainingStrings)
extracted = extractedFeats.docExtract()

#extract features from our test documents:
print("Extracting features...")
testFeats = DocumentExtractor(Basic9Extractor(), testStrings)
testvecs = testFeats.docExtract()

#scale our feature vectors to make them suitable for SVM input
print("Scaling feature vectors...")
print("Performing feature selection with chi2")
selection = SelectKBest(chi2, k=9)
selection.fit(extracted, labels)
extracted = selection.transform(extracted)
extracted = preprocessing.scale(extracted)
#instantiate classifier and train it
print("Instantiating classifier...")
clf = svm.SVC(probability=True, kernel='rbf')
print("Fitting dataset to classifier...")
clf.fit(extracted, labels)
#do some predictions, again with test vectors scaled
print("Computing predictions...")
normalizedpredic = clf.predict(preprocessing.scale(selection.transform(testvecs)))

#compute number of authors
authorSet = set()
for label in labels:
    authorSet.add(label)

print("Comparing authors:")
for n in authorSet:
    print(n)
#print(str(clf.score(preprocessing.scale(testvecs), testlabels) * 100) + "% score on this dataset.")

testvecsscaled = preprocessing.scale(testvecs)
testvecsscaled = selection.transform(testvecs)
#Cross-validation
print("Computing cross validation...")
cvIterations = 5
scores = cross_validation.cross_val_score(clf, extracted, labels,
cv=cvIterations)
print("Accuracy by " + str(cvIterations)  + "-fold CV: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

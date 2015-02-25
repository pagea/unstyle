#Load, train, and classify documents.
#This serves as a prototype to be refactored ASAP.
from stylproj.dochandler import DocumentExtractor
from stylproj.featuresets.basic9 import Basic9Extractor
from sklearn import svm
from sklearn.preprocessing import normalize
import codecs
import numpy as np

#load our list of training document paths (original author)
labels = []
paths = []
with open("trainingDocs.txt", "r") as trainingDocs:
    for line in trainingDocs.readlines():
        paths.append(line.split(':')[0])
        labels.append(line.split(':')[1].replace('\n', ''))
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
    try:
        with codecs.open(path, "r", encoding = 'utf8') as docString:
            document = docString.read()
            trainingStrings.append(document)
    except UnicodeDecodeError:
        #TODO: For now, we alert the user that their document is corrupted. In the
        #future, we ought to try to remove any offending characters from the
        #document and just move on.
        print("It appears you have tried to load a document that stylproj"
        " cannot read. Please convert your document to utf-8 and try again.")

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
testFeats = DocumentExtractor(Basic9Extractor(), testStrings)
testvecs = testFeats.docExtract()


#instantiate SVM
clf = svm.SVC()
#train SVM, normalizing on y axis
clf.fit(normalize(extracted, axis=0), labels)
#do some predictions
clf.predict(normalize(testvecs, axis=0))

#label as training documents

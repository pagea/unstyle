#Load, train, and classify documents.
#This serves as a prototype to be refactored ASAP.
from stylproj.dochandler import DocumentExtractor
from stylproj.featuresets.basic9 import Basic9Extractor
from sklearn import svm
import codecs

#load our list of training document paths (original author)
paths = []
with open("trainingDocs.txt", "r") as trainingDocs:
    for line in trainingDocs.readlines():
        paths.append(line.replace('\n', ''))
#load our list of test document paths
testpaths = []
with open("testDocs.txt", "r") as testDocs:
    for line in testDocs.readlines():
        testpaths.append(line.replace('\n', ''))

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

#set of labels for our training set
target = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

#instantiate SVM
clf = svm.SVC()
#train SVM
clf.fit(extracted, target)
#do some predictions
clf.predict(testvecs)

#label as training documents

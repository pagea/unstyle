"""This module is the link between the frontend and the backend of stylproj.
"""

from sklearn import svm, preprocessing
# gui imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from stylproj.gui.stylproj_frontend import StylProj

# backend imports
from stylproj.dochandler import DocumentExtractor
from stylproj.featuresets.basic9 import Basic9Extractor
from stylproj.feat_select import rank_features_rfe
from stylproj.adversarial import compute_target_vals

import codecs
import glob
import logging
import numpy as np
import os
import random
import stylproj
import sys
import timeit

# Instance of the frontend
window = None
# Target feature values
targets = None
# Feature set
featset = None

# TODO: move to dochandler
def load_document(docpath):
    # TODO: Support docx and odf. Should be easy; python has internal libraries
    # for this.
    """Load a document into a string.
    :param docpath: The path of the document to load.
    :returns: A string.
    """
    document = ""
    with codecs.open(docpath, "r", encoding = 'utf8', errors='replace') as docString:
        document = docString.read()
    return document

# TODO: move to dochandler
def _get_random_doc_paths(directory, numAuthors):
    """Get some random documents (and their labels) from our pre-supplied corpus.
    :returns: A tuple of (document paths, labels)
    """
    paths = []
    labels = []
    authorsToLoad = random.sample(os.listdir(directory), numAuthors)
    for auth in authorsToLoad:
        # oh my glob
        docpaths = glob.glob(os.path.join(directory, auth, "*"))
        print(docpaths)
        paths.extend(docpaths)
        for _ in range(len(docpaths)):
            labels.append(auth)
            print(auth)

    print(list(zip(paths, labels)))
    return list(zip(paths, labels))
 
def train_on_docs(pathToAnonymize, otherUserDocPaths, otherAuthorDocPaths):
    """Load and classify all documents referenced by the given paths.
    :returns: A classifier trained on the user's documents and a random subset
    of our corpus.
    """
    document_to_anonymize = load_document(pathToAnonymize)
    other_user_docs = []
    other_author_docs = []
    # Load other documents by the user.
    for path in otherUserDocPaths:
        other_user_docs.append(load_document(path))

    # Load documents by some other authors
    for path in otherAuthorDocPaths:
        other_author_docs.append(load_document(path[0]))

    # Load labels by the randomly selected authors:
    otherAuthorLabels = []
    for pair in other_author_paths:
        otherAuthorLabels.append(pair[1])
    # Extract features from all documents using the Basic-9 Feature Set.
    stylproj.controller.featset = Basic9Extractor()

    stylproj.controller.featlabels = []
    for index, func in enumerate(featset.features):
        stylproj.controller.featlabels.append(func)

    # TODO: Make DocumentExtractor work properly with one document
    docToList = []
    docToList.append(document_to_anonymize)
    userDocFeatures = DocumentExtractor(featset, docToList).docExtract()
    print("User doc features: ", userDocFeatures)
    stylproj.controller.to_anonymize_features = userDocFeatures
    # Features from other documents by the user (excludes documentToAnonymize)
    userOtherFeatures = DocumentExtractor(featset, other_user_docs).docExtract()
    print("User other features: ", userOtherFeatures)
    # Features from documents by other authors.
    otherAuthorFeatures = DocumentExtractor(featset, other_author_docs).docExtract()
    print("Other author features: ", otherAuthorFeatures)
    # Features from documents by other authors AND the user.
    userAndOtherFeatures = np.vstack((userOtherFeatures, otherAuthorFeatures))

    # Label all of our user's other documents as 'user'.
    userLabels = []
    for _ in otherUserDocPaths:
        userLabels.append('user')

    # Combine documents and labels. This creates the training set.
    X = np.vstack((userOtherFeatures, otherAuthorFeatures))
    y = []
    y.extend(userLabels)
    y.extend(otherAuthorLabels)
    print("Training labels: ", y)

    # Instantiate classifier; train and predict on scaled data.
    scaler = preprocessing.StandardScaler().fit(X)
    clf = svm.SVC(probability=True, kernel='rbf', C=1.0)
    clf.fit(scaler.transform(X), y)
    print("Predicted author of doc: " +
    str(clf.predict(scaler.transform(userDocFeatures))))
    print("Certainty: ", clf.predict_proba(scaler.transform(userDocFeatures)))
    print("Classifier internal label rep: ", clf.classes_)

    # Get feature ranks
    stylproj.controller.feature_ranks = rank_features_rfe(scaler.transform(X), y, featset)
    print(str(feature_ranks))

    # Get target values for features.
    authors = stylproj.controller.numAuthors
    stylproj.controller.targets = stylproj.adversarial.compute_target_vals(
                                                                           userDocFeatures,
                                                                           X,
                                                                           clf,
                                                                           featset,
                                                                           numAuthors+1
                                                                          )

    # Tell the frontend we're done computing on the input it gave us.
    window.update_stats()
    return (clf, scaler)

def validateInput():
    # Make sure the user didn't accidentally put document_to_anonymize in the
    # training set
    for doc in other_user_documents_paths:
        if document_to_anonymize_path == doc:
            return False
        else:
            return True

def readyToClassify():
    """ The frontend calls this after it has given the controller all of
    the requisite input documents.
    """
    stylproj.controller.trained_classifier = train_on_docs(document_to_anonymize_path,
                                       other_user_documents_paths,
                                       other_author_paths)
def checkAnonymity(text):
    """Check if the user has properly anonymized their document.
    :param: The current state of the user's document.
    :returns: 0 if the classifier identifies the user as the most likely author;
    1 if the user is not the most likely author but there is an above random
    chance that he or she IS the author; 2 if the author is anonymous.
    """
    randomChance = 1/(numAuthors+1)
    # Extract features from the text
    docToList = []
    docToList.append(text)
    extractor = DocumentExtractor(featset, docToList)
    extr = extractor.docExtract()
    print("Current doc features: ", extr)
    print("Scaled doc features: ", trained_classifier[1].transform(extr))
    # Get the probabilities for every label
    probas = trained_classifier[0].predict_proba(trained_classifier[1].transform(extr))[0]
    # Get the probability of the user label
    index = (trained_classifier[0].classes_).tolist().index('user')
    print("Probabilities:", probas)
    proba = probas[index]
    print("Probability: ", proba)
    print("Random chance: ", randomChance)
    prediction = trained_classifier[0].predict(trained_classifier[1].transform(extr))[0]
    print(trained_classifier[0].predict_proba(trained_classifier[1].transform(extr)))
    print("Current prediction: ", prediction)
    print("Prediction type: ", type(prediction))
    
    if prediction is np.str_('user'):
        print("Predicted USER")
        return 0
    if proba > randomChance:
        return 1
    else:
        return 2

def startGUI():
   app = QApplication(sys.argv)
   stylproj.controller.window = StylProj()
   stylproj.controller.window.show()
   sys.exit(app.exec_()) 

# File paths
document_to_anonymize_path = ''
to_anonymize_features = []
other_user_documents_paths  = []

# Get the paths of documents from a set of random authors.
numAuthors = 7
drexel_dataset_path = os.path.join('datasets', 'drexel_1')
other_author_paths = _get_random_doc_paths(drexel_dataset_path, numAuthors)

# Training data
document_to_anonymize = ''
trained_classifier = None
feature_ranks = []
feat_labels = []

"""This module is the link between the frontend and the backend of stylproj.
"""
# FIXME: This module needs a workover; it's messy in here.

from sklearn import svm, preprocessing

# gui imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from stylproj.gui.stylproj_frontend import StylProj

# backend imports
from stylproj.dochandler import DocumentExtractor
from stylproj.featuresets.basic9 import Basic9Extractor

import codecs
import glob
import logging
import numpy as np
import os
import random
import sys

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
        paths.extend(docpaths)
        for _ in enumerate(docpaths):
            labels.append(auth)

    return zip(paths, labels)
    
def train_on_docs(pathToAnonymize, otherUserDocPaths, otherAuthorDocPaths):
    """Load and classify all documents referenced by the given paths.
    :returns: A trained classifier.
    """
    document_to_anonymize = load_document(pathToAnonymize)
    other_user_docs = ""
    other_author_docs = "" 
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
    featset = Basic9Extractor()

    userDocFeatures = DocumentExtractor(featset, [document_to_anonymize])
    # Features from other documents by the user (excludes documentToAnonymize)
    userOtherFeatures = DocumentExtractor(featset, other_user_docs).docExtract()
    # Features from documents by other authors.
    otherAuthorFeatures = DocumentExtractor(featset, other_author_docs).docExtract()
    # Features from documents by other authors AND the user.
    userAndOtherFeatures = np.vstack(userOtherFeatures, otherAuthorFeatures)

    # Label all of our user's other documents as 'user'.
    userLabels = []
    for _ in otherUserDocPaths:
        userLabels.append('user')

    # Combine documents and labels. This creates the training set.
    X = np.vstack(userOtherFeatures, otherAuthorFeatures)
    y = []
    y.extend(userLabels)
    y.extend(otherAuthorLabels)

    # Instantiate classifier; train on SCALED DATA.
    clf = svm.SVC(probability=True, kernel='rbf')
    clf.fit(preprocessing.scale(X), y)

    return clf

def readyToclassify():
    """ The View (frontend) calls this after it has given the controller all of
    the requisite input documents.
    """
    trainOndocs(document_to_anonymize_path,
                other_user_documents_paths,
                other_author_paths)

def startGUI():
   app = QApplication(sys.argv)
   #app.setStype(QStyleFactory.create("motif"))
   window = StylProj()
   window.show()
   sys.exit(app.exec_()) 

# File paths
document_to_anonymize_path = ''
other_user_documents_paths  = []

# Get the paths of documents from 4 random authors.
drexel_dataset_path = os.path.join('datasets', 'drexel_1')
other_author_paths = _get_random_doc_paths(drexel_dataset_path, 4)

document_to_anonymize = ''

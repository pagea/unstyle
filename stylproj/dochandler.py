import numpy as np
import glob
import os
#Import feature extractors:
#Import classifiers:

#class DocumentHandler:
#    """Given some text, this class will perform feature
#    extractiowith a DocumentExtractor and train a classifier on the
#    documents, constructing a profile of a given author."""
#    def __init__(self, featExtractor, trainingDocs, targetDocs,
#    self.trainingDocs = [docs for docs in trainingDocs]
#    self.targetDocs   = [docs for docs in targetDocs]
#    self.featExtractor = featExtractor
#    
#    def setTrainingSet(self, docs):
#        for each doc in docs:
#            self.trainingDocs.append(doc)
#
#    def setTargetSet(self, docs):
#        for each doc in docs:
#            self.targetDocs.append(doc)
#
#    def setExtractor(self, extractor):
#        """Set the feature extractor our handler will use."""
#        self.featExtractor = extractor
#
#class DocumentLoader:
#    """Load each document in a list of document paths."""
#    def __init__(self, docs):
#        docs = 
#    def loadDoc(self, doc):
        

class DocumentExtractor:
    """A class that performs feature extraction on a given set of documents.

    :param feat_extractor: An instance of a feature extractor (e.g. the Basic-9
    feature set, or writeprints. Any class implementing FeatureSetExtractor
    should work.)
    :param docs: An arbitrary number of documents (strings of text).

    Example:
    >>>from stylproj.featuresets.basic9 import Basic9Extractor
    >>>d = DocumentExtractor(Basic9Extractor(), ["text of document 1", "text of
    document 2"])
    >>>d.docExtract()
    """

    def __init__(self, feat_extractor, docs):
        self.documents = docs
        self.featureSet = feat_extractor

        if self.documents is None:
            raise TypeError

    def docExtract(self):
        """Extract features from each document. Return it as a matrix of (number of
        docs) by (number of features)."""

        self.fv = []
        for doc in self.documents:
            self.fv.append(self.featureSet.extract(doc))

        # Convert to a numpy matrix.
        return np.array(np.asmatrix(self.fv))
        #return self.fv

import numpy as np
import glob
import os
# Import feature extractors:
# Import classifiers:


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
        # return self.fv

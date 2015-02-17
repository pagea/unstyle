import numpy as np
#Import feature extractors:
#Import classifiers:

class DocumentExtractor:
    """A class that performs feature extraction on a given set of documents.

    :param feat_extractor: An instance of a feature extractor (e.g. the Basic-9
    feature set, or writeprints. Any class implementing FeatureSetExtractor
    should work.)
    :param docs: An arbitrary number of documents (strings of text).

    Example:
    >>>from stylproj.featuresets.basic9 import Basic9Extractor
    >>>b = Basic9Extractor()
    >>>d = DocumentExtractor(b, "text of document 1", "text of document 2")
    >>>d.docExtract()
    """

    def __init__(self, feat_extractor, *docs):
        self.documents = []
        self.featureSet = feat_extractor

        for n in docs:
            self.documents.append(n)

        if documents is None:
            raise TypeError

    def docExtract(self):
        """Extract features from each document. Return it as a matrix of (number of
        docs) by (number of features)."""

        fv = []
        for doc in self.documents:
            fv.append(self.featureSet.extract(doc))

        # Convert to a numpy matrix. After this step, the feature vector should
        # be ready to be input as a training set/target set/etc.
        return np.array(np.asmatrix(fv))

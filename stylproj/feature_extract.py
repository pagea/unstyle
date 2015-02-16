from abc import ABCMeta, abstractmethod

class FeatureSetExtractor:

    """The metaclass that all feature set extractors must extend."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(self, text):
        """The procedure to extract all of the features from a body of text.
        Every instance of FeatureSet MUST override this function.
        
        Return a list of features.
        """
        raise NotImplementedError()

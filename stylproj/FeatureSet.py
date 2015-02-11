from abc import ABCMeta, abstractmethod

class FeatureSet:

    """The metaclass that all feature sets must extend."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(self, text):
        """The procedure to extract all of the features from a body of text.
        Every instance of FeatureSet MUST override this function.
        
        MUST return a feature vector.
        """
        raise NotImplementedError()

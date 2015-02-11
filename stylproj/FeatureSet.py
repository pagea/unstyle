from abc import ABCMeta, abstractmethod

class FeatureSet:

    """The metaclass that all feature sets must extend."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def extractFeatures(self, text):
        pass

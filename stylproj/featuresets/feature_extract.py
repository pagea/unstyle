from stylproj.features.featregister import featregistry

class FeatureSetExtractor:
    """Superclass that all feature sets should extend."""
    def __init__(self):
        self.features = []

    def extract(self, text):
        """The procedure to extract all of the features from a body of text.
        Returns a list of extracted features.
        """
        self.extractor = None
        self.extractedFeatures = []
        for feature in self.features:
            self.extractor = featregistry[feature]
            self.extractedFeatures.append(self.extractor(text))

        return self.extractedFeatures

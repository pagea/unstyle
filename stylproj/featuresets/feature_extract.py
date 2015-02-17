from stylproj.features.featregister import featregistry

class FeatureSetExtractor:
    def __init__(self):
    self.features = []

    def extract(self, text):
        """The procedure to extract all of the features from a body of text.
        Returns a list of extracted features.
        """
        extractedFeatures = []
        for feature in self.features:
            extractedFeatures.append(featregistry[feature])

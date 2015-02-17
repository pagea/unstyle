from stylproj.featuresets.feature_extract import FeatureSetExtractor
from stylproj.features import characterfeatures
from stylproj.features import lexicalfeatures

class Basic9Extractor(FeatureSetExtractor):
    """The Basic-9 feature set extractor.[1]

    [1] Michael Brennan and Rachel Greenstadt. Practical Attacks Against Authorship
    Recognition Techniques in Proceedings of the Twenty-First Conference on
    Innovative Applications of Artificial Intelligence (IAAI), Pasadena, California,
    July 2009.
    """
    def __init__(self):
        self.features = [
            "letterSpace",
            "gunningFog",
            "avgSyllablesPerWord",
            "unique_words",
            "sentenceCount",
            "characterSpace",
            "avgSentenceLength",
            "complexity",
            "fleschReadingEase"
        ]

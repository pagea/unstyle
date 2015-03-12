"""The feature extractor register. This keeps track of all active feature extractors.
You can compose feature sets by accessing this dictionary.

Note that the featregistry is ordered. So, if you have a feature vector that
looks like

array([1, 50.32, 40.02],
[5, 23.23, 93.2]),

then you can figure out which column is which feature by iterating over
featregistry.


Use the @register_feat decorator to register a feature extractor with stylproj.
"""
# FIXME: Right now, the feature registry basically assumes that you only
# register features from a single featureset. If, in the future, we were to
# try to instantiate multiple feature sets at once, they will all get jumbled
# together in the feature register. If our classification model uses feature
# selection, this shouldn't be a big deal, but for the sake of keeping
# everything consistent, we ought cleanly separate featuresets in the registry.
#
# In order to fix this, we should restructure the featureregistry to be a
# dictionary of dictionaries, where each Key is a featureset name, and each
# respective value is the features (that is, the "feature functions" found in
# stylproj.features) associated with the featureset. Example:
#
# {'Basic9FeatureSet' : {'unique_words' : <function unique_words>,
#                        'characterSpace' : <function characterSpace>,
#                        ...
#                        .
#                        .
#                       },
#  'Writeprints' :      {'char_bigrams' : <function char_bigrams>,
#                        ...
#                        .
#                        .
#                       }
# }
#
# Unfortunately, this means refactoring any functions that use the featregistry.
from collections import OrderedDict

featregistry = OrderedDict()

def register_feat(func):
    """Adds decorated function to a dictionary in the form {'name of
    function':function}. For instance, we add the characterSpace feature to our
    registry by adding @register_feat before the definition:
    
    @register_feat
    def characterSpace(text):
        ...

    Then the state of our dictionary becomes:
    {'characterSpace' : <function characterfeatures.characterSpace>}
    
    This makes it easy to make a featureset composed of whatever functions we
    would like to experiment with.
    """

    name = func.__name__
    featregistry[name] = func

    return func

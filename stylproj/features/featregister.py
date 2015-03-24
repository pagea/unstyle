"""The feature extractor register. This keeps track of all feature extractors.
We compose feature sets (subsets of stylproj's set of all feature extractors) by accessing this dictionary.

** The feature register should only be used by DocumentHandlers. **

Note that the featregistry is ordered.

Use the @register_feat decorator to register a feature extractor with stylproj.
"""

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

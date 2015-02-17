"""The feature extractor register. This keeps track of all feature extractors.
You can compose feature sets by accessing this dictionary.

Use the @register_feat decorator to register a feature extractor with stylproj.
"""

featregistry = {}

def register_feat(func):
    """Adds decorated function to a dictionary in the form {'name of
    function':function}. For instance, we add the characterSpace feature to our
    registry by adding @register_feat before the definition:
    
    @register_feat
    def characterSpace(text):
        ...

    Then the state of our dictionary becomes:
    {'characterSpace' : <function characterfeatures.characterSpace}
    """
    print("register_feat called")
    name = func.__name__
    featregistry[name] = func

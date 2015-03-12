# featrank.py
""" Given a training set X, a set of labels y, and a feature extractor,
 rank features by a scoring function. For now, we use an Extra
 Trees classifier's "importance" attribute to decide feature ranking; the
 scoring function can be changed in the future if this proves ineffective.
"""
from sklearn.ensemble import ExtraTreesClassifier
from numpy import sort
from stylproj.features.featregister import featregistry
from collections import OrderedDict

# TODO: Grid search with k-fold cross-validation on classifier in order to see
# if better ranking results can be achieved.
def rank_features(X, y, featureset):
    """Rank features by their importance.

    :param X: A training set of features.
    :param y: A target set (aka class labels for the training set)
    :param featureset: An instance of a featureset (such as Basic9Extractor())
    :rtype: An OrderedDict of the form {K : V}, with K being the feature name
    and V being its importance. This dictionary will be sorted by importance.
    """

    classifier = ExtraTreesClassifier()
    classifier.fit(X, y)
    importances = classifier.feature_importances_

    feat_importance = OrderedDict()

    # Get the names of the feature columns.
    for index, func in enumerate(featureset.features):
        feat_importance[func] = importances[index]
    print("\nFeat importance dict:")
    print(str(feat_importance))

    # Sort the dictionary by value and return it. 
    return sorted(feat_importance.items(), key=lambda x:x[1], reverse=True)

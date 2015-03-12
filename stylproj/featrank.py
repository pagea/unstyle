# featrank.py
""" Given a training set X, y, where X is the training set and y is the set of
 labels, rank features by a scoring function. For now, we use an Extra
 Trees classifier's "importance" attribute to decide feature ranking; the
 scoring function can be changed in the future if this proves ineffective.
"""
from sklearn.ensemble import ExtraTreesClassifier
from numpy import sort

# TODO: Grid search with k-fold cross-validation in order to see if better
# ranking results can be achieved.
def rank_features(X, y):
    """Rank features by their importance.

    :param X: A training set of features.
    :param y: A target set (aka class labels for the training set)
    :rtype: A 1-dimensional numpy array of feature rankings.
    """

    classifier = ExtraTreesClassifier()
    classifier.fit(X, y)
    importances = classifier.feature_importances_
    return importances

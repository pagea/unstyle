# feat_select.py
""" Tools for feature selection.
"""

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_selection import RFE
from numpy import sort
from stylproj.features.featregister import featregistry
from collections import OrderedDict

# TODO: Grid search with k-fold cross-validation on classifier in order to see
# if better ranking results can be achieved.
def rank_features_dt(X, y, featureset):
    """Rank features by their importance with a decision tree.

    This does not seem to agree with rank_features_rbe, although it is
    considerably faster. Using this with SVM classifiers is likely a bad idea.

    :param X: A training set of features.
    :param y: A target set (aka class labels for the training set)
    :param featureset: An instance of a featureset (such as Basic9Extractor())
    :rtype: An OrderedDict of the form {K : V}, with K being the feature name
    and V being its importance. This dictionary will be sorted by importance.
    """

    classifier = ExtraTreesClassifier(n_estimators=500, n_jobs=-1)
    classifier.fit(X, y)
    importances = classifier.feature_importances_

    feat_importance = OrderedDict()

    # Get the names of the feature columns.
    for index, func in enumerate(featureset.features):
        feat_importance[func] = importances[index]

    print(feat_importance)

    # Sort the dictionary by value and return it. 
    return sorted(feat_importance.items(), key=lambda x:x[1], reverse=True)

def rank_features_rfe(X, y, featureset):
    """Rank features by their importance using recursive feature elimination.

    :param X: A training set of features.
    :param y: A target set (aka class labels for the training set)
    :param featureset: An instance of a featureset (such as Basic9Extractor())
    :rtype: An OrderedDict of the form {K : V}, with K being the feature name
    and V being its importance. This dictionary will be sorted by importance.
    """

    # FIXME: Use an RBF SVC to rank features. It is likely that the "importance"
    # rankings derived from a LinearSVC are similar as an RBF kernel SVM, but,
    # for safety's sake, it is best to assume they are not.

    classifier = LinearSVC()
    classifier.fit(X, y)

    ranker = RFE(classifier, 1, step=1)
    ranker = ranker.fit(X, y)

    # Get the names of the feature columns.
    # FIXME: Duplicate code from rank_features. Make this its own function.
    feat_importance = OrderedDict()
    for index, func in enumerate(featureset.features):
        feat_importance[func] = ranker.ranking_[index]

    return sorted(feat_importance.items(), key=lambda x:x[1])

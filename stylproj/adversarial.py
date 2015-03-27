"""Module containing functions related to defeating stylometry.
"""
from stylproj.feat_select import ak_means_cluster
import numpy as np
import random
import sys

def compute_target_vals(docfeatures, X, classifier, featureSet, numAuthors)
    """Given a set of feature vectors and a trained classifier, determine what
    each feature must be changed to change the classifier's label of the set of
    feature vectors.

    :param docfeatures: The feature vector of the document we are trying to
    anonymize.
    :param X: A complete feature set composed of the feature vectors from
    other_user_documents and other_author_documents.
    :param classifier: A classifier trained on X.
    :param featureSet: A feature extractor, such as Basic9Extractor().
    :param numAuthors: The number of authors in X.
    :returns: A list of target vectors for each feature.
    """
    # Cluster every feature vector; put them all in a list.
    print("Clustering features...")
    allFeatureClusters = []
    for col in range(X.shape[0]):
        # Get every sample of a given feature; cluster into <= numAuthors groups.
        feature = X[:, col]
        ak = ak_means_cluster(feature, numAuthors)
        
        # Retrieve the clusters for the given feature; store them in a hash
        # table of the form {cluster : members_of_cluster}
        clusters = {k: [] for k in ak[1]}
        allFeatureClusters.append(clusters)
        #Store in our list of potential cluster targets
        for idx, label in enumerate(ak[0].labels_):
            clusters[label].append(feature[idx].mean())
        print("Stored feature cluster mean.")

    # Find a target cluster that confuses the classifier.
    print("Computing target cluster...")
    iterations = 0
    configuration = generate_target_clusters(clusters)
    while classifier.predict(configuration)[0] is 'user' or
            authorship_near_random_chance(probability, numAuthors) is False:
        configuration = generate_target_cluster(clusters)
        iterations += 1
        # We have found a configuration that confounds the classifier.
        print("Found target cluster in ", iterations, " iterations.")
        return configuration
    else:
        continue

def generate_target_cluster(clusters):
    # FIXME: Right now, we try random targets from list of potential clusters
    # until we find a working configuration. That's dumb. Implement a less naive
    # search for a target cluster. Trying to "fuzz" the author's most important
    # features incrementally is likely the best way to go.
    configuration = []
    for featureNum in clusters:
        configuration.append(random.choice(clusters[featureNum])
    return configuration

def authorship_below_random_chance(probability, numAuthors):
"""See if the chance of the user being the author is below random chance.
"""
    randomChance = 1/numAuthors
    authorProb = classifier.predict_proba(X, classifier)[0]
    if authorProb <= randomChance or is_near(authorProb, randomChance):
        return True
    else
        return False

def is_near(num1, num2)
    """Check num1 is within +/- 5 of num2.
    """
    if abs(num1 - num2) <= numAuthors:
        return True
    else:
        return False

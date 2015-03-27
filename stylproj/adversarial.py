"""Module containing functions related to defeating stylometry.
"""
from stylproj.feat_select import ak_means_cluster
import numpy as np
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
    allFeatureClusters = []
    for col in range(X.shape[0]):
        # Get every sample of a given feature; cluster into <= numAuthors groups.
        feature = X[:, col]
        ak = ak_means_cluster(feature, numAuthors)
        
        # Retrieve the clusters for the given feature; store them in a hash
        # table of the form {cluster : members_of_cluster}
        clusters = {k: [] for k in range(len(ak[1]))}
        allFeatureClusters.append(clusters)
        #Store in our list of clusters-per-feature
        for idx, label in enumerate(ak[0].labels_):
            clusters[label].append(feature[idx])

    # Find a target cluster configuration that confuses the classifier.
    # TODO: Lower predict_proba for a given author below random chance. We omit
    # this for now because it is computationally expensive to do this.
    print("Computing target cluster...")
    for configuration in 
        if classifier.predict(configuration)[0] is not 'user':
            if authorship_near_random_chance():
            # We have found a configuration that confounds the classifier.
            return configuration
        else:
            continue

def authorship_below_random_chance(X, classifier, numAuthors):
    randomChance = 1/numAuthors
    authorProb = classifier.predict_proba(X, classifier)[0]
    if authorProb <= randomChance or is_near(authorProb, randomChance):

def is_near(num1, num2)
    """Check num1 is within +/- 5 of num2.
    """
    if abs(num1 - num2) <= numAuthors:
        return True
    else:
        return False

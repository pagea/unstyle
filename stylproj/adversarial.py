"""Module containing functions related to defeating stylometry.
"""
from stylproj.feat_select import ak_means_cluster
import numpy as np
import random
import sys


def compute_target_vals(docfeatures, X, classifier, featureSet, numAuthors):
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
    :rtype: A list of target vectors for each feature.
    """
    # TODO: Split this function up; it's very monolithic
    # Cluster every feature vector; put them all in a list.
    print("Clustering features...")
    clusterMeansList = []
    for col in range(X.shape[1]):
        # Get every sample of a given feature; cluster into <= numAuthors
        # groups.
        feature = np.asmatrix(X[:, col]).transpose()
        print("Clustering the following samples:")
        print(feature)
        ak = ak_means_cluster(feature, numAuthors)

        # Put all of the clusters from this feature into a table of the form
        # {cluster : members_of_cluster}
        clusters = {k: [] for k in range(ak[1])}
        print("Cluster labels: ", ak[0].labels_)
        for idx, label in enumerate(ak[0].labels_):
            clusters[label].append(feature[idx])

        # Compute the mean of every cluster
        clusterMeans = {k: [] for k in range(ak[1])}
        for cluster in clusters:
            total = 0
            print(clusters[cluster])
            for num in clusters[cluster]:
                total += num
            mean = total / len(clusters[cluster])
            clusterMeans[cluster].append(mean)
        clusterMeansList.append(clusterMeans)

    # Find a target cluster that confuses the classifier.
    iterations = 0
    configuration = generate_ran_target_cluster(clusterMeansList)
    print("Initial target configuration: ", configuration)
    # Keep generating target clusters until we find one that works.
    while ((classifier.predict_proba(configuration)[0] is 'user')
           or (authorship_below_random_chance(configuration, classifier, numAuthors) is False)):
        configuration = generate_ran_target_cluster(clusterMeansList)
        iterations += 1
        # We have found a configuration that confounds the classifier.
        print("Found target cluster in ", iterations, " iterations.")
        return configuration
    return configuration


def generate_ran_target_cluster(clusterMeansList):
    # FIXME: Right now, we try random targets from list of potential clusters
    # until we find a working configuration. That's dumb. Implement a less naive
    # search for a target cluster. Trying to "fuzz" the author's most important
    # features incrementally is likely the best way to go.
    configuration = []
    print("generate_target_clusters on: ", clusterMeansList,
          " of len ", len(clusterMeansList))
    for feature in clusterMeansList:
        configuration.append(random.choice(list(feature.values())))
    print("Returning target configuration of len: ", len(configuration))

    # The configuration is populated with lists of lists of matrix objects of
    # [[numbers]]. We don't want that. This ugly hack turns the matrices into regular
    # floats.
    # FIXME: Find root cause of the matrix issue.
    fixed = []
    for matrix in configuration:
        fixed.append(matrix[0][0].item(0))
    return fixed


def generate_sane_target_cluster(clusterMeansList, docFeatures):
    """Find the closest possible feature configuration that will fool the
    classifier.
    :param clusterMeansList: A list of potential target values.
    :param docFeatures: The document_to_anonymize's features.
    :configuration: A non-working 
    """
    pass


def authorship_below_random_chance(X, classifier, numAuthors):
    """See if the user's document features fool the classifier
    """
    randomChance = 1 / numAuthors
    authorProb = classifier.predict_proba(X)
    print("User probability: ", authorProb[0][0])
    print("numAuthors: ", numAuthors)
    print("Highest probability in array: ", np.amax(authorProb))
    if authorProb[0][0] <= randomChance:
        return True
    else:
        return False

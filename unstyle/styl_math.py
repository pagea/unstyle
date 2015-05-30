"""Various mathematical functions that are useful for performing stylometry.
"""
from numpy.linalg import norm


def cosine_distance(m, f):
    """Compute the cosine distance between a "model" M from an author's set of
    documents and a featureset F extracted from D (the document to anonymize.)
    Note that m and f must be of equal length for this computation to be
    meaningful.

    :param m: A set of averages of every author's feature.
    :param f: The featureset extracted from D.
    :rtype: A distance such that, given cosine_distance(x, y) <
    cosine_distance(x, z), we say that x is "closer to" y than z.
    """
    return (1 - ((m * f).sum() / (norm(m) * norm(f))))

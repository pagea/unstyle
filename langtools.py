# Miscellaneous natural language programming functions.

import nltk
from nltk.corpus import cmudict

d = smudict.dict()

# Return the ESTIMATED number of syllables in a given word.
def syllableCount(word):
    if word not in d:
        return None
    else:
        return max([len([y for y in x if isdigit(y[-1])]) for x in d[word.lower()]])

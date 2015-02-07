# Miscellaneous natural language programming functions.
# TODO: it's kind of stupid to have curses be a dependency just because of one
# function

from curses.ascii import isdigit
from nltk.corpus import cmudict
import pylab

d = cmudict.dict()

# Return the ESTIMATED number of syllables in a given word.
def syllableCount(word):
    if word not in d:
        return None
    else:
        return nsyl(word)

def nsyl(word):
    """return the max syllable count"""
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

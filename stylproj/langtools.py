# Miscellaneous natural language programming functions.
# TODO: it's kind of stupid to have curses be a dependency just because of one
# function

from curses.ascii import isdigit
from nltk.corpus import cmudict
import pylab

d = cmudict.dict()

def syllableCount(word):
    """Return the ESTIMATED number of syllables in a given word. Returns none if
    the word is not inthe dictionary. Be warned that there isn't a deterministic
    way to count syllables, and that some words with multiple pronunciations
    have ambiguous numbers of syllables. For words with multiple pronunciations,
    this method returns the number of syllables found in the first pronunciation
    of a given word found.
    """
    if word.lower() not in d:
        return None
    else:
        return nsyl(word.lower())

def nsyl(word):
    """Return the max syllable count.
    Near-indecipherable one-liner from stackoverflow; should probably replace
    this."""
    syllables = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    return syllables[0]

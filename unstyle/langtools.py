# Miscellaneous natural language programming functions.

import numpy as np
import re

from curses.ascii import isdigit
from nltk.corpus import cmudict

d = cmudict.dict()


def tokenize(text):
    """Tokenizes a given block of text. We use this rather than NLTK's
    tokenizers for more control over the tokenization process. See
    /doc/tokenization for details.
    """
    # 1. Replace hyphens and newlines with spaces

    noNewls = text.replace('\n', ' ')
    noHyphens = noNewls.replace('-', ' ')

    # 2. Split all words by spaces.
    noSpaces = noHyphens.split(' ')

    # 3. Remove all punctuation.
    # TODO: Deal with apostrophes better. We don't want to strip them from
    # contractions.
    punctuation = "[\.,!?;,:\"\'()\[\]\{\}–]"
    noPunc = []
    for word in noSpaces:
        noPunc.append(re.sub(punctuation, '', word))
    return noPunc


def syllableCount(word):
    """Return the ESTIMATED number of syllables in a given word. Returns none if
    the word is not inthe dictionary. Be warned that there is no deterministic
    way to count syllables, and that some words with multiple pronunciations
    have ambiguous numbers of syllables. We cope with this by returning the
    first syllable count that we find.
    """
    if word.lower() not in d:
        # We couldn't find the word in the dictionary. Use a naive syllable
        # approximation algorithm.
        # TODO: Naive syllable approximation
        return None
    else:
        return nsyl(word.lower())


def nsyl(word):
    """Return the minimum syllable count."""
    # TODO: Near-indecipherable one-liner from stackoverflow; should probably
    # replace this.
    syllables = [len(list(y for y in x if y[-1].isdigit()))
                 for x in d[word.lower()]]
    return syllables[0]

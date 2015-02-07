# features.py
# Module containing functions related to collecting stylometric features from
# text.

import string
from langtools import syllableCount

# TODO: Each feature set should probably be a separate class in a separate file,
# all inside a "features" folder. Implement an "Extractor" class that calls
# these functions.
# TODO: PEP8 checks.

###############################################################################
############################# Basic-9 Feature Set #############################
###############################################################################

def unique_words(tokens):
    """Return a dictionary tracking unique word occurrences."""

    wordSet = set()
    for token in tokens:
        wordSet.add(token)
    return len(wordSet)

def complexity(tokens):
    """Return the ratio of unique words to total number of words in the
    document.
    """
    unique = unique_words(tokens)
    wordCount = len(tokens)
    complexityRatio = len(unique) / len(wordCount)
    return complexityRatio

# TODO: More sophisticated sentence detection.
def sentenceCount(tokens):
    """Naive sentence counter that treats periods as sentences."""
    return tokens.count('.')

def avgSentenceLength(tokens):
    """Return the average length of a sentence."""
    return len(tokens) / sentenceCount(tokens)

# TODO: syllableCount is from another online source; make sure it actually works
# properly.
def avgSyllablesPerWord(tokens):
    """ Return the average number of syllables per word. """
    totalWords = len(tokens)
    totalSyllables = 0
    
    for word in tokens:
        count += 1
        totalSyllables += syllableCount(word)

    return totalSyllables / totalWords

def gunningFog(tokens):
    """Return the Gunning-Fog readability measure."""
    # Complex words are words with 3 or more syllables.
    complexWords = 1;
    for word in tokens:
        if syllableCount(word) >= 3:
            complexWords += 1
    totalWords = len(tokens)
    totalSentences = sentenceCount(tokens)
    return 0.4*((totalWords/totalSentences) + 100*(complexWords/totalWords))

# TODO: This should include spaces. Tokenized words are probably not an
# appropriate input for this function.
def characterSpace(tokens):
    """Return the total number of characters."""
    count = 0
    for word, char in tokens:
        count += 1

def letterSpace(tokens):
    """Return the total number of letters (excludes spaces and punctuation)"""
    count = 0;
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    for word, char in tokens:
        if char in alphabet:
            count += 1
    return count

def fleschReadingEase(tokens):
    """Return the Flesch reading ease score."""
    totalWords = len(tokens)
    totalSentences = sentenceCount(tokens)
    totalSyllables = 0

    for word in tokens:
        totalSyllables += syllableCount(word)
    return 206.835-1.015*(totalWords / totalSentences) - 84.6*(totalSyllables /
    totalWords)

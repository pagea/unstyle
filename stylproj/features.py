# features.py
# Module containing functions related to collecting stylometric features from
# text.

import string
from langtools import syllableCount
from langtools import tokenize

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
    complexityRatio = unique / wordCount
    return complexityRatio

# TODO: More sophisticated sentence detection.
def sentenceCount(text):
    """Naive sentence counter that treats periods as sentences."""
    return text.count('.') + text.count('?') + text.count('!')

def avgSentenceLength(tokens):
    """Return the average length of a sentence."""
    return len(tokens) / sentenceCount(tokens)

def avgSyllablesPerWord(tokens):
    """ Return the average number of syllables per word. """
    totalWords = len(tokens)
    totalSyllables = 0
    for word in tokens:
        syllablesInWord = syllableCount(word)
        #Ignore words not found in our dictinoary.
        if syllablesInWord is not None:
            totalSyllables += syllablesInWord
    return totalSyllables / totalWords

def gunningFog(text, tokens):
    """Return the Gunning-Fog readability measure."""
    # Complex words are words with 3 or more syllables.
    complexWords = 0;
    for word in tokens:
        syllables = syllableCount(word)
        if syllables is not None:
            if syllables >= 3:
                complexWords += 1
    totalWords = len(tokens)
    totalSentences = sentenceCount(text)
    return 0.4*((totalWords/totalSentences) + 100*(complexWords/totalWords))

def characterSpace(text):
    """Return the total number of characters."""
    return len(count)

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

    return (206.835-1.015*(totalWords / totalSentences) - 84.6*(totalSyllables /
    totalWords))

# Basic9.py
# Module containing functions related to collecting Basic-9
# text.

import string
import numpy

from langtools import syllableCount
from langtools import tokenize

# TODO: PEP8 checks.

###############################################################################
############################# Basic-9 Feature Set #############################
###############################################################################
class Basic9(FeatureSet):
    """The Basic-9 feature set as described by Brennan and Greenstadt.[1]

    [1] Michael Brennan and Rachel Greenstadt. Practical Attacks Against Authorship
    Recognition Techniques in Proceedings of the Twenty-First Conference on
    Innovative Applications of Artificial Intelligence (IAAI), Pasadena,
    California, July 2009.
    """

    def unique_words(self, tokens):
        """Return the number of unique words."""

        wordSet = set()
        for token in tokens:
            wordSet.add(token)
        return len(wordSet)

    def complexity(self, tokens):
        """Return the ratio of unique words to total number of words in the
        document.
        """
        unique = unique_words(tokens)
        wordCount = len(tokens)
        complexityRatio = unique / wordCount
        return complexityRatio

    def sentenceCount(self, text):
        """Get the number of sentences using NLTK's pickle tokenizer.
        """
        return len(nltk.tokenize.sent_tokenize(text))

    def avgSentenceLength(self, tokens):
        """Return the average length of a sentence."""
        return len(tokens) / sentenceCount(tokens)

    def avgSyllablesPerWord(self, tokens):
        """Return the average number of syllables per word."""
        totalWords = len(tokens)
        totalSyllables = 0
        for word in tokens:
            syllablesInWord = syllableCount(word)
            #Ignore words not found in our dictinoary.
            if syllablesInWord is not None:
                totalSyllables += syllablesInWord
        return totalSyllables / totalWords

    def gunningFog(self, text, tokens):
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

    def characterSpace(self, text):
        """Return the total number of characters."""
        return len(count)

    def letterSpace(self, text):
        """Return the total number of letters (excludes spaces and punctuation)"""

        count = 0;
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        for char in tokens:
            if char in alphabet:
                count += 1
        return count

    def fleschReadingEase(self, text, tokens):
        """Return the Flesch reading ease score."""
        totalWords = len(tokens)
        totalSentences = sentenceCount(text)
        totalSyllables = 0
        for word in tokens:
            syllablesInWord = syllableCount(word)
            if syllablesInWord:
                totalSyllables += syllableCount(word)

        return (206.835 - ((1.015*totalWords) / totalSentences) - 84.6*(totalSyllables /
        totalWords))

    def extract(self, text):
        """Extract Basic-9 features from a given body of text."""
        # TODO: return a set of feature vectors?
        tokens = tokenize(text)
        features = []

        unique_words = unique_words(tokens)
        complexity = complexity(tokens)
        sentenceCount = sentenceCount(text)
        avgSentenceLength = avgSentenceLength(text)
        avgSyllablesPerWord = avgSyllablesPerWord(tokens)
        gunningFog = gunningFog(text, tokens)
        characterSpace = characterSpace(text)
        letterSpace = letterSpace(text)
        fleschReadingEase = fleschReadingEase(text, tokens)

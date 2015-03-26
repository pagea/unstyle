"""Module containing lexical feature extractors."""

import numpy
import nltk
import collections

from stylproj.features.featregister import register_feat
from stylproj import langtools

@register_feat
def unique_words(text):
    """Return the number of unique words."""
    tokens = langtools.tokenize(text)
    wordSet = set()
    for token in tokens:
        wordSet.add(token)
    return len(wordSet)

@register_feat
def complexity(text):
    """Return the ratio of unique words to total number of words in the
    document.
    """
    tokens = langtools.tokenize(text)
    unique = unique_words(text)
    wordCount = len(tokens)
    complexityRatio = unique / wordCount
    return complexityRatio

@register_feat
def sentenceCount(text):
    """Get the number of sentences using NLTK's sentence tokenizer.
    """
    return len(nltk.tokenize.sent_tokenize(text))
   
@register_feat
def avgSentenceLength(text):
    """Return the average length of a sentence."""
    tokens = langtools.tokenize(text)
    return len(tokens) / sentenceCount(text)

@register_feat
def avgSyllablesPerWord(text):
    """Return the average number of syllables per word."""
    tokens = langtools.tokenize(text)
    totalWords = len(tokens)
    totalSyllables = 0
    for word in tokens:
        syllablesInWord = langtools.syllableCount(word)
        #Ignore words not found in our dictinoary.
        if syllablesInWord is not None:
            totalSyllables += syllablesInWord
    return totalSyllables / totalWords

@register_feat
def gunningFog(text):
    """Return the Gunning-Fog readability measure."""
    tokens = langtools.tokenize(text)
    # Complex words are words with 3 or more syllables.
    #print(str(tokens))
    complexWords = 0;
    for word in tokens:
        syllables = langtools.syllableCount(word)
        if syllables is not None:
            if syllables >= 3:
                complexWords += 1
    totalWords = len(tokens)
    totalSentences = sentenceCount(text)
    return 0.4*((totalWords/totalSentences) + 100*(complexWords/totalWords))

@register_feat
def fleschReadingEase(text):
    """Return the Flesch reading ease score."""
    tokens = langtools.tokenize(text)
    totalWords = len(tokens)
    totalSentences = sentenceCount(text)
    totalSyllables = 0
    for word in tokens:
        syllablesInWord = langtools.syllableCount(word)
        if syllablesInWord:
            totalSyllables += langtools.syllableCount(word)

    return (206.835 - ((1.015*totalWords) / totalSentences) - 84.6*(totalSyllables /
    totalWords))

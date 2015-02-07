# features.py
# Module containing functions related to collecting stylometric features from
# text.

from langtools import syllableCount
import string
alphabet = string.ascii_lowercase + string.ascii_uppercase

# TODO: Each feature set should probably be a separate class in a separate file,
# all inside a "features" folder. Implement an "Extractor" class that calls
# these functions.
# TODO: PEP8 checks.

###############################################################################
############################# Basic-9 Feature Set #############################
###############################################################################

# Return a dictionary tracking unique word occurrences in the form of word :
# num_of_occurrences
def unique_words(tokens):
    wordTable = {}
    for token in tokens:
        if token not in wordTable:
            wordTable[token] = 1
        else:
            wordTable[token] += 1
    return wordTable

# Return the ratio of unique words to total number of words in the document.
def complexity(tokens):
    unique = unique_words(tokens)
    wordCount = len(tokens)
    complexityRatio = len(unique) / len(wordCount)
    return complexityRatio

# Naive sentence counter that treats periods as sentences.
# TODO: More sophisticated sentence detection.
def sentenceCount(tokens):
    return tokens.count('.')

# Returns the average length of a sentence (total words / total num of
# sentences).
def avgSentenceLength(tokens):
    return len(tokens) / sentenceCount(tokens)

# Return the average number of syllables per word.
# TODO: syllableCount is from another online source; make sure it actually works
# properly.
def avgSyllablesPerWord(tokens):
    totalWords = len(tokens)
    totalSyllables = 0
    
    for word in tokens:
        count += 1
        totalSyllables += syllableCount(word)

    return totalSyllables / totalWords

# Return the Gunning-Fog readability measure.
def gunningFog(tokens):
    # Complex words are words with 3 or more syllables.
    complexWords = 1;
    for word in tokens:
        if syllableCount(word) >= 3:
            complexWords += 1
    totalWords = len(tokens)
    totalSentences = sentenceCount(tokens)
    return 0.4*((totalWords/totalSentences) + 100*(complexWords/totalWords))

# Return the total number of characters
# TODO: This should include spaces. Tokenized words are probably not an
# appropriate input for this function.
def characterSpace(tokens):
    count = 0
    for word, char in tokens:
        count += 1

# Return the total number of letters (exlucdes spaces and punctuation)
def letterSpace(tokens):
    count = 0;
    for word, char in tokens:
        if char in alphabet:
            count += 1
    return count

# Return the Flesch reading ease score.
def fleschReadingEase(tokens):
    totalWords = len(tokens)
    totalSentences = sentenceCount(tokens)
    totalSyllables = 0

    for word in tokens:
        totalSyllables += syllableCount(word)
    return 206.835-1.015*(totalWords / totalSentences) - 84.6*(totalSyllables /
    totalWords)

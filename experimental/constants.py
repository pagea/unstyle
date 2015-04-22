# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import string

SPECIAL_CHARS = list(".,!?()-/&<>[]:;'" + '"') 
NORMAL_CHARS = list(string.ascii_lowercase) + [" "]
ALL_CHARS = SPECIAL_CHARS + NORMAL_CHARS
# Measurement. one sigma. 81 bigrams
BI_CHARS = [('e', ' '), (' ', 't'), ('s', ' '), ('t', 'h'), (' ', 'a'), ('h', 'e'), ('t', ' '), ('d', ' '), ('i', 'n'), ('n', ' '), (' ', 'i'), ('e', 'r'), ('a', 'n'), ('r', 'e'), (' ', 's'), (' ', 'o'), ('y', ' '), ('o', 'n'), (' ', 'w'), ('r', ' '), ('a', 't'), ('e', 'n'), ('e', 's'), (' ', 'c'), ('n', 'd'), ('o', 'r'), ('o', ' '), ('t', 'i'), ('i', 's'), (' ', 'h'), ('t', 'o'), (' ', 'b'), ('i', 't'), ('t', 'e'), ('n', 'g'), ('s', 't'), ('a', 'l'), (' ', 'm'), ('e', 'd'), ('a', 'r'), (' ', 'p'), (' ', 'f'), ('f', ' '), ('h', 'a'), ('n', 't'), ('o', 'f'), ('o', 'u'), ('s', 'e'), ('a', 's'), ('g', ' '), ('v', 'e'), ('l', 'e'), ('l', ' '), ('h', 'i'), (' ', 'd'), ('m', 'e'), ('a', ' '), ('e', 'a'), ('c', 'o'), ('d', 'e'), (' ', 'e'), ('r', 'o'), ('i', 'o'), (' ', 'r'), ('l', 'i'), ('h', ' '), ('n', 'e'), ('r', 'i'), (' ', 'l'), ('i', 'c'), ('r', 'a'), ('l', 'l'), ('b', 'e'), (' ', 'n'), ('c', 'e'), ('c', 'a'), ('e', 'l'), ('h', 'o'), ('m', 'a'), ('o', 'm'), ('c', 'h')]
# Measurement. 25% of character trigrams. 59 trigrams
TRI_CHARS = [(' ', 't', 'h'), ('t', 'h', 'e'), ('h', 'e', ' '), (' ', ',', ' '), (' ', '.', ' '), (' ', 'a', 'n'), ('n', 'd', ' '), (' ', 't', 'o'), ('a', 'n', 'd'), ('i', 'n', 'g'), (' ', 'o', 'f'), ('e', 'd', ' '), (' ', 'i', 'n'), ('t', 'o', ' '), ('n', 'g', ' '), ('o', 'f', ' '), ('i', 's', ' '), ('e', 'r', ' '), ('e', 's', ' '), ('o', 'n', ' '), ('i', 'n', ' '), ('r', 'e', ' '), (' ', 'a', ' '), ('a', 't', ' '), ('i', 'o', 'n'), (' ', 'c', 'o'), ('e', ' ', 't'), ('a', 's', ' '), (' ', 'b', 'e'), ('s', ' ', 'a'), ('e', 'n', 't'), ('t', 'i', 'o'), ('e', ' ', 'a'), ('l', 'y', ' '), ('s', ' ', 't'), (' ', 'r', 'e'), ('h', 'a', 't'), ('h', 'e', 'r'), ('n', ' ', 't'), ('t', 'h', 'a'), ('o', 'r', ' '), ('d', ' ', 't'), (' ', 'i', 's'), ('t', ' ', 't'), ('e', ' ', 's'), ('a', 'n', ' '), (' ', 'h', 'e'), ('a', 'l', ' '), ('f', 'o', 'r'), (' ', 'f', 'o'), ('e', 'n', ' '), (' ', 's', 't'), ('n', 't', ' '), ('l', 'e', ' '), ('a', 't', 'i'), ('h', 'i', 's'), (' ', 'w', 'a'), ('e', ' ', 'o'), (' ', 'w', 'h')]

# NLTK standard:
SIMPLE_TAGS = ('VERB','NOUN','PRON','ADJ','ADV','ADP','CONJ','DET','NUM','PRT','X','.')
# Measurement. two sigma. 78 bigrams
BI_TAGS = [('DET', 'NOUN'), ('NOUN', '.'), ('NOUN', 'ADP'), ('NOUN', 'NOUN'), ('.', '</s>'), ('ADJ', 'NOUN'), ('ADP', 'DET'), ('NOUN', 'VERB'), ('ADP', 'NOUN'), ('PRON', 'VERB'), ('VERB', 'VERB'), ('VERB', 'ADP'), ('DET', 'ADJ'), ('VERB', 'DET'), ('VERB', 'ADV'), ('PRT', 'VERB'), ('VERB', 'NOUN'), ('ADP', 'PRON'), ('NOUN', 'CONJ'), ('ADV', 'VERB'), ('PRON', 'NOUN'), ('VERB', 'PRT'), ('VERB', 'ADJ'), ('<s>', 'NOUN'), ('ADP', 'ADJ'), ('VERB', '.'), ('.', 'NOUN'), ('NOUN', 'PRT'), ('VERB', 'PRON'), ('<s>', 'DET'), ('CONJ', 'NOUN'), ('NOUN', 'DET'), ('<s>', 'PRON'), ('.', 'CONJ'), ('ADJ', '.'), ('DET', 'VERB'), ('ADJ', 'ADP'), ('NOUN', 'ADV'), ('ADV', 'ADJ'), ('<s>', 'ADP'), ('CONJ', 'VERB'), ('.', 'DET'), ('NOUN', 'PRON'), ('.', 'ADJ'), ('ADV', 'ADP'), ('.', 'VERB'), ('ADV', '.'), ('.', '.'), ('.', 'ADP'), ('.', 'PRON'), ('PRT', 'DET'), ('ADP', 'VERB'), ('PRT', 'NOUN'), ('ADJ', 'ADJ'), ('.', 'ADV'), ('ADV', 'ADV'), ('CONJ', 'ADJ'), ('CONJ', 'DET'), ('<s>', 'ADV'), ('NUM', 'NOUN'), ('PRON', '.'), ('ADV', 'DET'), ('NOUN', 'ADJ'), ('PRON', 'ADJ'), ('ADJ', 'PRT'), ('CONJ', 'ADV'), ('ADJ', 'CONJ'), ('ADV', 'PRON'), ('CONJ', 'PRON'), ('ADP', 'ADP'), ('PRON', 'ADV'), ('NUM', '.'), ('ADP', 'NUM'), ('ADP', 'ADV'), ('VERB', 'CONJ'), ('ADJ', 'VERB'), ('ADV', 'NOUN'), ('DET', 'ADV')]

# Pattern standard:
CHUNKS = (u'NP', u'VP', u'PP', u'ADVP', u'ADJP')
# All bigrams that occur more than 1%. 16
BI_CHUNKS = [(u'NP', u'VP'), (u'PP', u'NP'), (u'VP', u'NP'), (u'NP', u'PP'), (u'NP', u'NP'), (u'NP', '</s>')]

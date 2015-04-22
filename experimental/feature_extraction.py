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

from collections import defaultdict

from constants import *

def rvd(numbers):
	"""
		rvd - rich vector descriptor.
		Input: a list of at least 3 numbers.
		Returns a list with the following:
			- mean
			- median
			- median - mean
			- sigma
	"""
	from math import sqrt
	numbers = sorted(numbers)
	mean = float(sum(numbers)) / len(numbers)
	sigma = sqrt(sum([ (mean - n) ** 2 for n in numbers ]) / len(numbers))

	if len(numbers) % 2 == 1:
		median = numbers[len(numbers)/2]
	else:
		median = (numbers[(len(numbers)-1)/2] + numbers[len(numbers)/2]) / 2.0

	return [mean, median, median - mean, sigma]
	

def get_features(words, sentences, tags, chunks):
	"""
		Extracts features from words, sentences, tags, chunks triplet.
		Returns a dictionary with real vectors
	"""
	from itertools import chain
	flatten = lambda x : list(chain(*x))

	def get_legomena(words):
		# Returns the lowest three legomenon
		# https://en.wikipedia.org/wiki/Hapax_legomenon
		freqs = defaultdict(int)
		for word in words:
			freqs[word] += 1
		hapax = float(len([ w for (w, c) in freqs.items() if c == 1 ]))
		return [ len([ w for (w, c) in freqs.items() if c == i ]) / hapax for i in xrange(2,7) ]

	def get_readability(words, sentences):
		# Returns two readability scores
		# Calculate ARI - https://en.wikipedia.org/wiki/Automated_Readability_Index
		char_count = float(sum( [len(w) for w in words]))
		word_count = float(len(words))
		sentence_count = float(len(sentences))
		ARI = 4.71 * char_count / word_count  + 0.5 * word_count / sentence_count - 21.43

		# Calculate LIX - https://en.wikipedia.org/wiki/LIX
		long_word_count = float(sum([ len(w) for w in words if len(w) > 6]))
		LIX = word_count / sentence_count + 100 * long_word_count / word_count
		return [ARI, LIX]

	def get_word_length_distribution(words):
		# Returns the wordlength distribution
		# Projects all wordlengths larger than 12 to 12.
		max_len = 12
		freqs = dict( [ (i, 0) for i in xrange(1,max_len+1) ])
		for word in words:
			l = len(word)
			if max_len < l:
				l = max_len
			freqs[l] += 1
		total = float(len(words))
		return [ freqs[i] / total for i in xrange(1,max_len+1) ] + rvd([len(x) for x in words])
	
	def get_char_distribution(words):
		"""
			This functions reports on character distributions
			Reports rel. frequencies of:
			- sum special characters
			- sum normal characters
			- upper characters
			- all individual characters
			- common character bigrams
		"""
		special_char_set = set(SPECIAL_CHARS)
		normal_char_set = set(NORMAL_CHARS)

		letters = flatten([w + " " for w in words])

		special = 0
		normal = 0
		upper = 0
		char_dist = dict([ (char, 0) for char in ALL_CHARS ])
		bi_char_dist = dict([ (char, 0) for char in BI_CHARS ])
		tri_char_dist = dict([ (char, 0) for char in TRI_CHARS ])
		bigram = (None, None)
		trigram = (None, None, None)
		for l in letters:
			bigram = (bigram[1], l.lower())
			trigram = (trigram[1], trigram[2], l.lower())

			if bigram in bi_char_dist:
				bi_char_dist[bigram] += 1

			if trigram in tri_char_dist:
				tri_char_dist[trigram] += 1

			if l.isupper():
				upper += 1
			if l.lower() in normal_char_set:
				normal += 1
			elif l in special_char_set:
				special += 1
			if l.lower() in char_dist:
				char_dist[l.lower()] += 1

		lc = float(len(letters))
		specials = [special / lc, normal / lc, upper / float(len(words))] 

		lc = float(sum(char_dist.values()))
		char_dist = [ char_dist[char] / lc for char in ALL_CHARS ]

		lc = float(sum(bi_char_dist.values()))
		bi_char_dist = [ bi_char_dist[char] / lc for char in BI_CHARS ]

		lc = float(sum(tri_char_dist.values()))
		tri_char_dist = [ tri_char_dist[char] / lc for char in TRI_CHARS ]
		return specials + char_dist, bi_char_dist, tri_char_dist

	def get_tag_distribution(tags):
		"""
			Gives POS-tag distribution.
			Measures rel. frequencies of:
			- POS-tags
			- common POS-tag bigrams
		"""
		tags = flatten([ ['<s>'] + ts + ['</s>'] for ts in tags ])
		tag_bi_dist = dict([ (t, 0) for t in BI_TAGS ])
		tag_dist = dict([ (t, 0) for t in SIMPLE_TAGS ])
		bigram = (None, None)
		for t in tags:
			bigram = (bigram[1], t)
			if bigram in tag_bi_dist:
				tag_bi_dist[bigram] += 1
			if t in tag_dist:
				tag_dist[t] += 1
		tc = float(sum(tag_dist.values()))
		mono = [ tag_dist[tag] / tc for tag in SIMPLE_TAGS ]
		tc = float(sum(tag_bi_dist.values()))
		bi = [ tag_bi_dist[tag] / tc for tag in BI_TAGS ]
		return mono, bi

	def get_chunk_distribution(chunks):
		chunks = flatten([ ['<s>'] + cs + ['</s>'] for cs in chunks ])
		chunk_bi_dist = dict([ (c, 0) for c in BI_CHUNKS ])
		chunk_dist = dict([ (c, 0) for c in CHUNKS ])
		bigram = (None, None)
		for c in chunks:
			bigram = (bigram[1], c)
			if bigram in chunk_bi_dist:
				chunk_bi_dist[bigram] += 1
			if c in chunk_dist:
				chunk_dist[c] += 1
		cc = float(sum(chunk_dist.values()))
		mono = [ chunk_dist[chunk] / cc for chunk in CHUNKS ]
		cc = float(sum(chunk_bi_dist.values()))
		bi = [ chunk_bi_dist[chunk] / cc for chunk in BI_CHUNKS ]
		return mono, bi

	features = []
	feature_dic = dict()
	feature_dic_names = []

	def append_features(vector, name, features=features, feature_dic=feature_dic, feature_dic_names=feature_dic_names):
		features += vector
		feature_dic[name] = vector
		feature_dic_names.append(name)

	# Sentence length distribution
	sentence_length_f = rvd([len(x) for x in sentences])
	append_features(sentence_length_f, "sentence_length")

	# Word length distribution
	word_length_f = get_word_length_distribution(words)
	append_features(word_length_f, "word_length")

	# char distribution
	mono_char_dist, bi_char_dist, tri_char_dist = get_char_distribution(words)
	append_features(mono_char_dist, "mono_char_dist")
	append_features(bi_char_dist, "bi_char_dist")
	append_features(tri_char_dist, "tri_char_dist")

	# Tag distribution
	mono, bi = get_tag_distribution(tags)
	append_features(mono, "mono_tag_dist")
	append_features(bi, "bi_tag_dist")

	# Chunk distribution
	mono, bi = get_chunk_distribution(chunks)
	append_features(mono, "mono_chunk_dist")
	append_features(bi, "bi_chunk_dist")

	# Readability 
	readability_f = get_readability(words, sentences)
	append_features(readability_f, "readability")

	# Legomena
	legomena_f = get_legomena(words)
	append_features(legomena_f, "legomena")

	return features, feature_dic, feature_dic_names

def create_cached_features(data, filename="Cached_Features.py"):
	dataset = dict()
	for author in data.keys():
		print "Working on:", author
		dataset[author] = dict()
		for storyname, info in data[author].items():
			dataset[author][storyname] = get_features(*info)

	f = open(filename, 'w')
	f.write("# -*- coding: utf-8 -*-\n")
	f.write("data = " + str(dataset) + "\n")
	f.close()

def demo():
	from Dataset import data
	info = data[data.keys()[2]][data[data.keys()[2]].keys()[1]]
	features, feature_dic, feature_dic_names = get_features(*info)
	for key in feature_dic_names:
		print key, feature_dic[key]
		print
	print len(features)


if __name__ == '__main__':
	from Dataset import data
	create_cached_features(data)


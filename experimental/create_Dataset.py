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

def load_file(filename='text.txt'):
	"""
		Reads all text in filename, returns the following triplet:
		- list of all words
		- sentences (ordered list of words, per sentence)
		- POS-tags (ordered list of tags, per sentence)
		- chunks
	"""
	def process_raw_text(text):
		from nltk.tokenize import sent_tokenize, word_tokenize
		from nltk.tag import pos_tag, map_tag
		from itertools import chain
		from pattern.en import parsetree

		flatten = lambda x : list(chain(*x))
		simplify_tag = lambda t : map_tag('en-ptb', 'universal', t)


		text = text.decode("utf8")
		chunks = [ [ c.type for c in t.chunks ] for t in parsetree(text) ]
		sentences = sent_tokenize(text)
		sentences = [ word_tokenize(s) for s in sentences ]
		sentences_tags = [ [ (w, simplify_tag(t)) for w, t in pos_tag(s) ] for s in sentences ]
		
		sentences = [ [ w for w, _ in s] for s in sentences_tags ]
		tags = [ [ t for _, t in s] for s in sentences_tags ]
		words = flatten(sentences)
		
		return words, sentences, tags, chunks

	f = open(filename,'r')
	c = "".join([ x + " " for x in f.readlines() ])
	f.close()
	# Remove breaks and tabs
	for char in ["\t", "\n"]: 
		c = c.replace(char, " ")
	c = c.replace('."', '".')
	c = c.replace(".'", "'.")
	# Split special characters from words
	for char in ["'", '"', ",", ".", "?", "!", ";", ":"]:
		c = c.replace(char, " " + char + " ")
	# Magic to remove all multi-spaces
	return process_raw_text(' '.join(c.split()))

def create_cached_dataset():
	import os
	BASE = "../Data/Drexel-AMT-Corpus/"
	folders = filter(lambda x : x not in ['.DS_Store'], os.listdir(BASE))

	dataset = dict()
	for folder in folders:
		print "Working on:", folder
		dataset[folder] = dict()
		files = filter(lambda x : x not in ['.DS_Store'], os.listdir(BASE + folder))
		for f in files:
			if 'demographics' not in f:
				w, s, t, c = load_file(BASE + folder + "/" + f)
				dataset[folder][f] = (w, s, t, c)
	f = open("Dataset.py", 'w')
	f.write("# -*- coding: utf-8 -*-\n")
	f.write("data = " + str(dataset) + "\n")
	f.close()
	

if __name__ == '__main__':
	create_cached_dataset()

	

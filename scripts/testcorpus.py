# Run classifyTest.py on every author pair in the Reuters dataset.

import os
import subprocess
import sys

testDir = ("./datasets/C50test/")
authorPairs = set()
iterations = 0
for author1 in os.listdir("./datasets/C50train/"):
    iterations += 1
    for author2 in os.listdir("./datasets/C50train/"):
        # track our author pairs so we don't benchmark them twice
        authorPairs.add((author2, author1))

        first = "./datasets/C50train/" + author1
        second = "./datasets/C50train/" + author2

        firsttest = "./datasets/C50test/" + author1
        secondtest = "./datasets/C50test/" + author2

        if (first != second) and (author1, author2) not in authorPairs:
            subprocess.call(['python3', './scripts/filelistfromdir.py',
                             'trainingDocs.txt', first + '/', second + '/'])
            subprocess.call(['python3', './scripts/filelistfromdir.py',
                             'testDocs.txt', firsttest + '/', secondtest + '/'])
            print(first)
            print(second)
            subprocess.call(['python3', 'classifyTest.py'])

# Output a text file containing a list of all of the textfile paths in a given
# directory.
#
# USAGE: python filelistfromdir DIRECTORY

import os
import sys

for i in os.listdir(sys.argv[1]):
    if i.endswith(".txt"):
        print(sys.argv[1] + "/" + i)

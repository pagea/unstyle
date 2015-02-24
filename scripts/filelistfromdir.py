# Output a text file containing a list of all of the textfile paths in a given
# directory.
#
# USAGE: python filelistfromdir DIRECTORY

import os
import sys

files = []
for i in os.listdir(sys.argv[1]):
    if i.endswith(".txt"):
        files.append(sys.argv[1] + "/" + i + "\n")

with open("filelist.txt", "w") as filelist:
    filelist.writelines(files)

for path in files:
    print(path)

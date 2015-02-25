# Output a text file containing a list of all of the textfile paths in a given
# directory followed by their class label, delimited by a colon.
#
# Example output:
# ./datasets/C50train/AaronPressman/106247newsML.txt:AaronPressman
#
# USAGE: python filelistfromdir [WRITEOUTFILE] [DIRECTORY1] [DIRECTORY 2] ...

import os
import sys

files = []
for directory in sys.argv[2:]:
    for i in os.listdir(directory):
        if i.endswith(".txt"):
            files.append(directory + "/" + i + ":" +
            os.path.split(os.path.dirname(directory))[1]  + "\n")

with open(sys.argv[1], "w") as filelist:
    filelist.writelines(files)

for path in files:
    print(repr(path))

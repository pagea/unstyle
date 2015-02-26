# Load a testcorpus file. Print out some statistics.

import sys

lines = []
with open(sys.argv[1], "r") as datafile:
    lines = datafile.readlines()

#The sum of all accuracy measurements
accuracySum = 0
#The accuracy of the classifier across the entire dataset.
avgAccuracy = 0
#Lowest percentage found in document
lowest = 100
#Highest percentage found in document
highest = 0

#list of all accuacy measurements
accuracyList = []
for line in lines:
    if '%' in line:
        #Parse the accuracy percentage
        accuracy = float(line[:2])
        accuracyList.append(accuracy)

for num in accuracyList:
    accuracySum += num

for num in accuracyList:
    if num < lowest:
        lowest = num
    if highest < num:
        highest = num

avgaccuracy = accuracySum/len(accuracyList)

print("Average accuracy: " + str(avgaccuracy))
print("Highest accuracy: " + str(highest))
print("Lowest accuracy: " + str(lowest))
print("Number of samples: " + str(len(accuracyList)))

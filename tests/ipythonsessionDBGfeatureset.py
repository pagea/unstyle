# ipython session on 2/26/2015
# coding: utf-8

get_ipython().magic('ls ')
from stylproj.dochandler import DocumentExtractor
from stylproj.featuresets import basic9
from stylproj.featuresets.basic9 import Basic9Extractor
d = DocumentExtractor(
    Basic9Extractor(), "./datasets/C50train/LynneO\'Donnell/116963newsML.txt")
d.documents
d.docExtract
d.docExtract()
d2 = DocumentExtractor(
    Basic9Extractor(), "./datasets/C50train/MichaelConnor/22201newsML.txt")
d2.docExtract()
d2 = DocumentExtractor(Basic9Extractor(), "Wait a minute, what?")
d2.docExtract
d2.docExtract()
d2 = DocumentExtractor(
    Basic9Extractor(), ["Wait a minute, what?", "Test argument 2. What's going on?"])
d2.docExtract
d2.docExtract()
d2 = DocumentExtractor(Basic9Extractor(), ["Wait a minute, what?"])
d2.docExtract()
d.docExtract
d.docExtract()
d.documents
d.documents
d2.docExtract()
d2.documents
d.documents
d = DocumentExtractor(
    Basic9Extractor(), ["./datasets/C50train/LynneO\'Donnell/116963newsML.txt"])
d.documents
lynneDocs = ""
with open("./datasets/C50train/LynneO'Donnell/133490newsML.txt") as lynne:
    lynneDocs = lynne.readlines()

lynneDocs
d = DocumentExtractor(Basic9Extractor(), lynneDocs)
d.documents
# d.documents.docExtract()
d.docExtract
d.docExtract()
d = DocumentExtractor(Basic9Extractor(), lynneDocs, "Trying this again")
d = DocumentExtractor(Basic9Extractor(), [lynneDocs, "Trying this again"])
d.docExtract()
d = DocumentExtractor(Basic9Extractor(), [lynneDocs, "Trying this again"])
d.documents
lynneDocs
with open("./datasets/C50train/LynneO'Donnell/116963") as lynne:
    lynneDocs = lynne.read()

with open("./datasets/C50train/LynneO'Donnell/116963newsML.txt") as lynne:
    lynneDocs = lynne.read()

lynneDocs
d = DocumentExtractor(Basic9Extractor(), [lynneDocs, "This is another test."])
d.documents
d.docExtract()
with open("./datasets/C50train/WilliamKazer/101226newsML.txt") as williamk:
    williambad = williamk.read()

williambad
badext1 = DocumentExtractor(Basic9Extractor(), williambad)
badext1.docExtract()
# for num in badext1.docExtract()"
for num in badext1.docExtract():
    print(num)

williamk
williambad
badext1 = DocumentExtractor(Basic9Extractor(), [williambad])
badext1.docExtract()
for num in badext1.docExtract():
    print(num)

for num in badext1.docExtract():
    for char in num:
        print(char)

for num in badext1.docExtract():
    print(num)

badext1.docExtract()
williambad2 = ''
with open("./datasets/C50train/WilliamKazer/222819newsML.txt") as will:
    williambad2 = will.read()

williambad2
badext = DocumentExtractor(Basic9Extractor(), williambad, williambad2)
badext = DocumentExtractor(Basic9Extractor(), [williambad, williambad2])
badext.documents
badext.docExtract()
for list in badext.docExtract():
    for num in list:
        print(num)

for list in badext.docExtract():
    for num in list:
        print(num + '\n')

for list in badext.docExtract():
    for num in list:
        print(str(num) + '\n')

for list in badext.docExtract():
    print('\n')
    for num in list:
        print(str(num))


def printFeatures(featureset):
    for list in badext.docExtract():
        print('\n')
        for num in list:
            print(str(num))

printFeatures(badext.docExtract())
docList = []
loadedDocList = []
import os
os.listdir('./datasets/C50train/AaronPressman/')


def loadAuthorDocs(authordir):
    for doc in os.listdir(authordir):
        with open(doc) as openeddoc:
            loadedDocList.append(openneddoc.read())


def loadAuthorDocs(authordir):
    for doc in os.listdir(authordir):
        with open(doc) as openeddoc:
            loadedDocList.append(openneddoc.read())


def loadAuthorDocs(authordir):
    documents = []
    for doc in os.listdir(authordir):
        with open(doc) as openeddoc:
            documents.append(openeddoc.read())
    return documents
loadAuthorDocs("./datasets/C50train/WilliamKazer/")


def loadAuthorDocs(authordir):
    documents = []
    for doc in os.listdir(authordir):
        with open(authordir + doc) as openeddoc:
            documents.append(openeddoc.read())
    return documents
loadAuthorDocs("./datasets/C50train/WilliamKazer/")
len(loadAuthorDocs("./datasets/C50train/WilliamKazer/"))
d = DocumentExtractor(
    Basic9Extractor(), loadAuthorDocs("./datasets/C50train/WilliamKazer/"))
d.docExtract()
printFeature(d.docExtract())
printFeatures(d.docExtract())
d.docExtract()
d.docExtract()


def printFeatures(docextractor):
    for list in docextractor.docExtract():
        print('\n')
        for num in list:
            print(str(num))

printFeatures(d)
d
d2 = DocumentExtractor(
    Basic9Extractor(), loadAuthorDocs("./datasets/C50train/TanEeLyn/"))
get_ipython().magic('lsmagic')
[i for (i, l) in enumerate(_ih) if l.startswith('def ')][-1]
get_ipython().magic('edit 100')
[i for (i, l) in enumerate(_ih) if l.startswith('def loadDocList')][-1]
[i for (i, l) in enumerate(_ih) if l.startswith('def loadD')][-1]
[i for (i, l) in enumerate(_ih) if l.startswith('def')][-1]
[i for (i, l) in enumerate(_ih) if l.startswith('def')][-2]
[i for (i, l) in enumerate(_ih) if l.startswith('def')][-3]
_ih
[i for (i, l) in enumerate(_ih) if l.startswith('def load')][-1]
get_ipython().magic('edit 87')
get_ipython().magic('ls ')
get_ipython().magic('save ipythonsessionDBGfeatureset 0-116')
get_ipython().magic('edit 87')
docdir = "./datasets/C50train/"
d.docExtract()
d.docExtract()
import numpy as np
np.mean(d.docExtract(), axis=1)
np.mean(d.docExtract(), axis=0)
for x in np.mean(d.docExtract(), axis=0):
    print(x)

get_ipython().magic('edit 124')
printMean(d.docExtract())
# gap1 = good author 1, bap1 = bad author 1
gap1 = DocumentExtractor(
    Basic9Extractor(), loadAuthorDocs("./datasets/C50train/LynneO'Donnell/"))
printMean(gap1.docExtract())
gap2 = DocumentExtractor(
    Basic9Extractor(), loadAuthorDocs("./datasets/C50train/MichaelConnor/"))
printmean(gap2.docExtract())
printMean(gap2.docExtract())
bap1 = DocumentExtractor(
    Basic9Extractor(), loadAuthorDocs("./datasets/C50train/WilliamKazer/"))
bap2 = DocumentExtractor(
    Basic9Extractor(), loadAuthorDocs("./datasets/C50train/TanEeLyn/"))
printMean(bap1)
printMean(bap1.docExtract())
printMean(bap2.docExtract())
printMean(gap1.docExtract())
printMean(gap2.docExtract())
get_ipython().magic('save ipythonsessionDBGfeatureset.py 149')
get_ipython().magic('save ipythonsessionDBGfeatureset.py 0-149')

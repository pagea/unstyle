# coding: utf-8
# Generated from an ipython session. Played with cosine distance. Saved this for
# future reference when we implement authorship verification.
from stylproj.styl_math import cosine_distance
from stylproj.styl_math import cosine_distance
from stylproj.controller import load_document
from stylproj.featuresets.basic9 import Basic9Extractor
from stylproj.styl_math import cosine_distance
from stylproj.featuresets.basic9 import Basic9Extractor
from stylproj.dochandler import DocumentExtractor
from stylproj.controller import load_doc
from stylproj.controller import load_document
docs1 = load_document("home/pagea/Code/stylproj/datasets/drexel_1/f/f_01.txt")
docs1 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/f/f_01.txt")
docs2 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/f/f_02.txt")
docs3 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/f/f_03.txt")
docs4 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/f/f_04.txt")
doc = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/f/f_05.txt")
docs_features = DocumentExtractor(Basic9Extractor(), [docs1, docs2, docs3, docs4])
docs_features = DocumentExtractor(Basic9Extractor(), [docs1, docs2, docs3, docs4])
docs_features
docs_features = docs_features.docExtract()
docs_features
docs_means = docs_features.mean(axis=0)
docs_means
doc
doc_features = DocumentExtractor(Basic9Extractor(), doc)
doc_features = DocumentExtractor(Basic9Extractor(), [doc])
doc_features
doc_features = DocumentExtractor(Basic9Extractor(), [doc]).docExtract()
doc_features
cosine_distance(docs_means, doc_features)
from numpy.linalg import norm
len(m)
len(docs_means)
len(doc_features)
doc_features
doc_means
docs_means
doc_features = doc_features[0]
doc_features
get_ipython().magic('ls ')
cosine_distance(docs_means, doc_features)
distances = cosine_distance(docs_means, doc_features)
for x in distances:
    print(x)
    
define cosine_distance(m, f):
    return ((m * f/(norm(m) * norm(f)))
    
    )
define cosine_distance(m, f):
    return ((m * f)/(norm(m) * norm(f)))
def cosine_distance(m, f):
    return ((m * f)/(norm(m) * norm(f)))
cosine_distance(docs_means, doc_features)
distances =cosine_distance(docs_means, doc_features)
for x in distances:
    print(x)
    
cosine_distance([[1.29], [9.92]])
cosine_distance([[1.29], [9.92]], [[8.21],[2.98]])
cosine_distance(np.asmatrix([[1.29], [9.92]]), np.asmatrix([[8.21],[2.98]]))
import numpy as np
cosine_distance(np.asmatrix([[1.29], [9.92]]), np.asmatrix([[8.21],[2.98]]))
cosine_distance(np.asmatrix([ [1.29], [9.92] ]), np.asmatrix([ [8.21], [2.98] ]))
cosine_distance(np.asmatrix([ [1.29], [9.92] ]), np.asmatrix([ [8.21], [2.98] ]))
cosine_distance([[1.29], [9.92]], [[8.21], [2.98]])
cosine_distance(np.asmatrix([[1.29], [9.92]]), np.asmatrix([[8.21], [2.98]]))
cosine_distance(np.asmatrix([1.29], [9.92]), np.asmatrix([8.21], [2.98]))
cosine_distance(np.asmatrix([[1.29], [9.92]]), np.asmatrix([[8.21], [2.98]], [[2.3], [2.5]]))
cosine_distance(np.asmatrix([[1.29], [9.92]], [[2.4], 9.2]]), np.asmatrix([[8.21], [2.98]], [[2.3], [2.5]]))
doc_features
cosine_distance(np.array([2.3, 1.16]), np.array([5.6, 8.2]))
cosine_distance(np.array([2.3, 1.16]), np.array([5.6, 8.2])).sum()
def cosine_distance(m, f):
    return ((m * f)/(norm(m) * norm(f))).sum()
cosine_distance(docs_means, doc_features)
docs_means * doc_features
docs_means * doc_features / (norm(docs_means) * norm(doc_features))
(norm(docs_means) * norm(doc_features))
def cosine_distance(m, f):
    return ((m * f).sum()/(norm(m) * norm(f)))
cosine_distance(docs_means, doc_features)
cosine_distance(np.array([2.3, 1.16]), np.array([5.6, 8.2])).sum()
auth1 = load_document("/home/pagea/Coe/stylproj/datasets/drexel_1/k/k_01.txt")
auth1 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/k/k_01.txt")
auth1 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/k/k_01.txt")
auth2 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/k/k_02.txt")
auth3 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/k/k_03.txt")
auth4 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/k/k_04.txt")
auth_features = DocumentExtractor(Basic9Extractor(), [auth1, auth2, auth3, auth4]).docExtract()
auth_features
auth_means = auth_features.mean(axis=0)
auth_means
cosine_distance(auth_means, doc_features)
pair1 = 1 - cosine_distance(auth_means, doc_features)
pairs
pair1
pair2 = cosine_distance(docs_means, doc_features)
pair2 =1 - cosine_distance(docs_means, doc_features)
pair2
pair1 < pair2
pair2 < pair1
doc2 = load_document("/home/pagea/Code/stylproj/datasets/drexel_1/h/h_01.txt")
cosine_distance(docs_means, doc)
cosine_distance(docs_means, doc_features)
doc2_features = DocumentExtractor(Basic9Extractor(), [doc2])[0]
doc2_features = DocumentExtractor(Basic9Extractor(), [doc2]).docExtract()[0]
doc2_features
doc_features
cosine_distance(docs_means, doc_features)
cosine_distance(docs_means, doc2_features)
doc1_prob = cosine_distance(docs_means, doc_features)
doc2_prob = cosine_distance(docs_means, doc2_features)
doc1_prob = 1 - cosine_distance(docs_means, doc_features)
doc2_prob = 1 - cosine_distance(docs_means, doc2_features)
doc1_prob
doc2_prob
auth_features.std()
auth_features.std(axis=0)
docs_features.std(axis=0)
doc1_prob
doc1_prob < doc2_prob
t = .099387
t
doc1_prob > t
doc1_prob < t
doc2_prob < t
doc1_prob < doc2_prob
doc2_prob - doc1_prob
t
from nltk.util import ngrams
doc
list(ngrams(doc))
list(ngrams(doc), 2)
list(ngrams(doc, 2))
list(ngrams(doc, 50))
list(ngrams(doc, 2))
from sklearn.feature_extraction import ngrams
from sklearn.feature_extraction import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
doc1
docs1
corpus1 = [docs1, docs2, docs3, docs4)
corpus1 = [docs1, docs2, docs3, docs4]
corpus2 = [auth1, auth2, auth3, auth4]
X = vectorizer.fit_transform(corpus1)
X1 = vectorizer.fit_transform(corpus1)
X1
X1.toarray()
X1.shape
vectorizer
vectorizer = CountVectorizer()
docs_wordgrams = vectorizer.fit_transform(corpus1)
docs_wordgrams
auth_wordgrams = CountVectorizer().fit_transform(corpus2)
auth_wordgrams
doc_chargrams = CountVectorizer(analyzer='char').fit_transform(corpus1)
doc_chargrams
auth_chargrams = CountVectorizer(analyzer='char').fit_transform(corpus2)
auth_chargrams
auth_chargrams.shape
doc_chargrams.shape
doc_chargrams.toarray()
(doc_chargrams/4).toarray()
doc_chargrams.toarray()
(doc_chargrams/4).toarray()
docs_wordgrams_norm = None
docs_wordgrams_norm = []
for idx, x in enumerate(docs_wordgrams):
    docs_wordgrams_norm.append(x/len(corpus1[idx]))
    
docs_wordgrams_norm
docs_wordgrams_norm.toarray()
np.toarray(docs_wordgrams_norm)
np.array(docs_wordgrams_norm)
docs_wordgrams_norm
docs_wordgrams_norm.toarray()
docs_wordgrams_norm = np.array(docs_wordgrams_norm)
docs_wordgrams_norm.toarray()
docs_wordgrams_norm
type(docs_wordgrams_norm)
docs_wordgrams_norm.array()
docs_wordgrams_norm.array
docs_wordgrams_norm.tostring
docs_wordgrams_norm.tostring()
docs_wordgrams_norm.flatten()
docs_wordgrams_norm
docs_wordgrams_norm = None
docs_wordgrams_norm
docs_wordgrams
docs_wordgrams[0]
docs_wordgrams[0][0]
docs_wordgrams[0][0][0]
docs_wordgrams[0]/4
docs_chargrams = CountVectorizer(analyzer='char').fit_transform(corpus1)
docs_chargrams
docs_chargrams.shape
auth_chargrams.shape
doc_wordgrams.shape
docs_wordgrams.shape
docs_ngrams.shape
docs_chargrams.shape
docs
corpus1
len(corpus1)
len(corpus2)
len(corpus2[0])
len(corpus1[0])
len(corpus1[1])
len(corpus1[2])
len(corpus1[3])
len(corpus1[4])
len(corpus2[0])
len(corpus2[1])
len(corpus2[2])
len(corpus2[3])
len(corpus2[4])
doc_wordgrams = CountVectorizer().fit_transform(corpus1)
doc_wordgrams
doc_wordgrams.shape
auth_wordgrams = CountVectorizer().fit_transform(corpus2)
auth_wordgrams
auth_wordgrams.shape
doc_chargrams.shape
auth_chargrams.shape
docsgrams = np.concatenate(docs_wordgrams, docs_chargrams)
docsgrams = np.concatenate(docs_wordgrams, docs_chargrams, axis=1)
docsgrams = np.concatenate((docs_wordgrams, docs_chargrams), axis=1)
docs_wordgrams.shape
docs_chargrams.shape
docs_chargrams.shape
auth_chargrams.shape
vectorizer = CountVectorizer(analyzer='char')
docs_chargrams = vectorizer.fit_transform(corpus1)
docs_chargrams = vectorizer.transform(corpus2)
docs_chargrams.shape
docs_chargrams = vectorizer.fit_transform(corpus1)
vectorizer = CountVectorizer(analyzer='char')
vectorizer.fit_transform(corpus1)
vectorizer = CountVectorizer(analyzer='char')
docs_chargrams = vectorizer.fit_transform(corpus1)
auth_chargrams = vectorizer.fit_transform(corpus2)
vectorizer = CountVectorizer(analyzer='char')
docs_chargrams = vectorizer.fit_transform(corpus1)
auth_chargrams = vectorizer.transform(corpus2)
docs_chargrams.shape
auth_chargrams.shape
doc
docgrams = vectorizer.transform(doc)
docgrams
docgrams.shape
docs_chargrams.shape
vectorizer = CountVectorizer(analyzer='char')
docgrams = vectorizer.fit_transform(doc)
docgrams.shape
vectorizer = CountVectorizer(analyzer='char')
docgrams = vectorizer.fit_transform(list(doc))
docgrams
docgrams.shape
docgrams.toarray()
docgrams
vectorizer = CountVectorizer(analyzer='char')
corpus = [doc, docs1, docs2, docs3, docs4, auth1, auth2, auth3, auth4]
chargrams = vectorizer.fit_transform(corpus)
chargrams.shape
chargrams[0]
chargrams[0].toarray()
vectorizer
corpus
corpus = [doc, docs1, docs2, docs3, docs4, auth1, auth2, auth3, auth4]
corpuslabels = ["doc", "docs1", "docs2", "docs3", "docs4", "auth1", "auth2", "auth3", "auth"4]
corpus = [doc, docs1, docs2, docs3, docs4, auth1, auth2, auth3, auth4]
corpus = [doc, docs1, docs2, docs3, docs4, auth1, auth2, auth3, auth4]
corpuslabels = ["doc", "docs1", "docs2", "docs3", "docs4", "auth1", "auth2", "auth3", a"auth4"]
corpuslabels = ["doc", "docs1", "docs2", "docs3", "docs4", "auth1", "auth2", "auth3","auth4"]
corpuslabels
chargrams
chargrams.shape
corpuslabels
docsmean = [[chargrams[1], chargrams[2], chargrams[3], chargrams[4]]
]
docsmean
docsmean = np.asmatrix([[chargrams[1], chargrams[2], chargrams[3], chargrams[4]]
])
docsmean
docsmean
docsmean = [[chargrams[1], chargrams[2], chargrams[3], chargrams[4]]
]
docsmean
chargrams
docsmean = [[chargrams[:,1], chargrams[:,2], chargrams[:,3], chargrams[:,4]]
]
docsmean = [chargrams[:,1], chargrams[:,2], chargrams[:,3], chargrams[:,4]]
docsmean
chargrams
docsmean.mean()
docsmean = np.array([chargrams[:,1], chargrams[:,2], chargrams[:,3], chargrams[:,4]])
docsmean
docsmean.mean()
docsmean
chargrams
chargrams[0].toarray
chargrams[0].toarray()
chargrams[1].toarray()
chargrams[2].toarray()
chargrams[3].toarray()
allmeans = chargrams.mean(axis=0)
allmeans
allmeans.shape()
allmeans.shape
chargrams.shape()
chargrams.shape
chargrams[0]
chargrams[0].toarray
chargrams[0].toarray()
chargrams[0].shape
allmeans.shape
docchargrams = chargrams[0]
allmeans
chargrams
chargrams
docgrams
docchargrams = chargrams[0]
docchargrams
docchargrams.shape
allmeans.shape
corpuslabels
docmeans = doc[:, range(1, 5)]
docmeans = doc[:, [range(1, 5)]]
docmeans = doc[:, [1,2,3,4]]
docmeans = chargrams[:, [1,2,3,4]]
docmeans
docmeans.toarray()
docmeans.shape
authmeans = chargrams[:, [5,6,7,8]]
authmeans.shape
docchargrams.shape
docmeans = allmeans[:, [1,2,3,4]]
authmeans = allmeans[:, [5,6,7,8]]
authmeans
docmeans
docsmeans = allmeans[:, [1,2,3,4]]
docsmeans.shape
authmeans.shape
docchargrams.shape
allchargrams
chargrams
chargrams.shape
chargrams[:, 0]
chargrams[:, 0].shape
chargrams[:, 1].shape
chargrams[:, 2].shape
chargrams[:, 0].shape
chargrams.shape
chargrams[0]
chargrams[0].shape
chargrams.shape
chargrams[0, :]
chargrams[0, :].shape
chargrams[1, :].shape
chargrams[2, :].shape
chargrams[3, :].shape
chargrams[4, :].shape
np.mean(chargrams[1, :], chargrams[2, :])
np.mean((chargrams[1, :], chargrams[2, :]), axis=0)
np.mean((chargrams[1, :], chargrams[2, :]), axis=1)
np.mean(chargrams[1, :], chargrams[2,:])
chargrams
chargrams[1:4:1]
chargrams[1:4:1].shape
chargrams[1:4].shape
chargrams[1:5].shape
chargrams[0:1].shape
chargrams[0:2].shape
chargrams[0:3].shape
chargrams[0:4].shape
chargrams[0:4].shape.toarray()
chargrams[0:4]
chargrams[0:4].toarray()
chargrams[0:1].toarray()
chargrams[0:2].toarray()
chargrams[1:2].toarray()
chargrams[1:5].mean(0)
docmeans = chargrams[1:5].mean(0)
docmeans.shape
authmeans = chargrams[5:9].mean(0)
authmeans.shape
docchargrams.shape
cosine_distance(docmeans, docchargrams)
def cosine_distance(m, f):
    return ((m * f)/(norm(m) * norm(f))
    
    )
def cosine_distance(m, f):
    return ((m*f) / (norm(m)*norm(f)))
cosine_distance(docmeans, docchargrams)
docmeans.shape
docschargrams.shape
docchargrams.shape
cosine_distance(docmeans, docchargrams)
docmeans * docchargrams
docmeans
docchargrams
docchargrams.toarray()
docchargrams.shape
docmeans.shape
cosine_distance(docmeans, docchargrams)
np.multiply(docmeans, docchargrams)
np.multiply
docmeans
docchargrams
docmeans.toarray()
docchargrams.toarray()
docmeans.flatten()
docmeans.flatten() * docchargrams
docmeans.shape
docchargrams.shape
type(docmeans)
type(docmeans)
type(docchargrams)
type(docchargrams.toarray())
docchargrams.toarray()
docmeans.toarray()
docmeans
docmeans.shape
docmeans[0].shape
docchargrams[0]
docchargrams[0].shape
cosine_distance(docmeans[0], docchargrams[0])
docchargrams[0]
docmeans[0]
docmeans[0].toarray()
np.squeeze(np.asarray(docmeans))
docmeans = np.squeeze(np.asarray(docmeans))
type(docmeans)
type(docchargrams)
docchargrams = np.squeeze(np.asarray(docchargrams))
docchargrams
docchargrams * docmeans
cosine_distance(docmeans, docchargrams)
docchargrams * docmeans
docmeans * docchargrams
(docmeans * docchargrams)/(norm(docmeans) * norm(docchargrams))
(docmeans * docchargrams)
(norm(docmeans) * norm(docchargrams))
norm(docmeans)
norm(docchargrams)
docchargrams.shape
docchargrams
docchargrams.toarray
docchargrams.toarray()
docchargrams
docchargrams[0]
docchargrams = chargrams[:, 0]
docchargrams
docchargrams.toarray()
docchargrams = chargrams[0, :]
docchargrams
docchargrams.toarray()
docmeans
docchargrams.shape
docmeans.shape
type(docchargrams)
docmeans = np.asmatrix(chargrams[1, :], chargrams[2, :], chargrams[3, :], chargrams[4, :])
docmeans = np.vstack(chargrams[1, :], chargrams[2, :], chargrams[3, :], chargrams[4, :])
np.vstack(chargrams[1, :], chargrams[2, :])
np.vstack((chargrams[1, :], chargrams[2, :]))
np.vstack((chargrams[1, :], chargrams[2, :], chargrams[3, :], chargrams[4, :]))
np.vstack((chargrams[1, :], chargrams[2, :], chargrams[3, :], chargrams[4, :]))
docsgrams = np.vstack((chargrams[1, :], chargrams[2, :], chargrams[3, :], chargrams[4, :]))
docsgrams
docsgrams.means(0)
docsgrams.mean(0)
docsgrams.mean(0).toarray()
docsgrams.mean(0).shape
docsgrams.mean(1).shape
corpus1
corpus2
len(corpus1)
len(corpus2)
vectorizer = CountVectorizer(analyzer='char')
vectorizer = CountVectorizer(analyzer='chars')
vectorizer = CountVectorizer(analyzer='csadfsfasdf')
vectorizer = CountVectorizer(analyzer=chars)
vectorizer = CountVectorizer(analyzer='char')
corpus
len (corpus)
chargrams = vectorize.fit_transform(corpus)
chargrams = vectorizer.fit_transform(corpus)
chargrams
chargrams[0]
chargrams[0][0]
chargrams[0]
chargrams[0].toarray()
chargrams[0].toarray() * chargrams[1].toarray()
chargrams[0].toarray() * chargrams[1, :].toarray()
vectorizer = CountVectorizer(analyzer='char')
chargrams = vectorizer.fit_transform(corpus)
docchargrams = vectorizer.transform(doc)
docchargrams.shape
len(chargrams[0])
shape.chargrams[0]
chargrams[0].shape
vectorizer.transform(corpus[3])
vectorizer.transform(corpus[3]).shape
vectorizer.transform(corpus[0]).shape
vectorizer.transform(corpus[1]).shape
chargrams.toarray()
chargrams = chargrams.toarray()
chargrams[0]
chargrams[1]
chargrams[0] * chargrams[1]
docmeans = ((chargram[1] + chargram[2] + chargram[3] + chargram[4]) / 4)
docmeans = ((chargrams[1] + chargrams[2] + chargrams[3] + chargrams[4]) / 4)
docmeans
authmeans = ((chargrams[5] + chargrams[6] + chargrams[7] + chargrams[8])/4)
authmeans
authmeans.shape
docmeans.shape
docchargrams.shape
docchargrams = chargrams[0]
docchargrams
docmeans
len(docmeans)
len(docchargrams)
authmeans
docmeans
cosine_distance(docmeans, docchargrams)
cosine_distance(docmeans, docchargrams).sum()
cosine_distance(authmeans, docchargrams).sum()
for idx, x in enumerate(authmeans):
    print(x/len(corpus[idx+5])
    
    
    )
    
len(authmeans)
cosine_distance(docmeans, docchargrams)
cosine_distance(docmeans, docchargrams).sum()
cosine_distance(authmeans, docchargrams).sum()
docproba = cosine_distance(docmeans, docchargrams).sum()
authproba = cosine_distance(authmeans, docchargrams).sum()
authproba
docproba < authproba
1 - docproba
1 - authproba
docproba = 1 - docproba
authproba = 1 - authproba
import scipy
from scipy.spatial.distance import cosine
from scipy.spatial import distance
distance.cosine(authmeans, docchargrams))
distance.cosine(authmeans, docchargrams)
distance.cosine(authmeans, authmeans)
distance.cosine(authmeans, docchargrams)
distance.cosine(docmeans, docchargrams)
distance.cosine(docmeans, docchargrams)
distance.cosine(docmeans, docchargrams)
distance.cosine(authmeans, docchargrams)
distance.cosine(docmeans, docchargrams)
distance.cosine(docmeans, docchargrams)
docmeans = (chargrams[1]/len(corpus[1]) + chargrams[2]/len(corpus[2]) + chargrams[3]/len(corpus[4])
)
docmeans
docmeans = (chargrams[1]/len(corpus[1]) + chargrams[2]/len(corpus[2]) + chargrams[3]/len(corpus[4])
)/4
docmeans
authmeans = (chargrams[5]/len(corpus[5] + chargrams[6]/len(corpus[6] + chargrams[7]/len(corpus[7]) + chargrams[8]/len(corpus[8])/4
)
)
)
authmeans = (chargrams[5]/len(corpus[5]) + chargrams[6]/len(corpus[6] + chargrams[7]/len(corpus[7]) + chargrams[8]/len(corpus[8])
)
)
authmeans = (chargrams[5]/len(corpus[5]) + chargrams[6]/len(corpus[6] + chargrams[7]/len(corpus[7]) + chargrams[8]/len(corpus[8])
)
)
authmeans = (chargrams[5]/len(corpus[5]) + chargrams[6]/len(corpus[6] + chargrams[7]/len(corpus[7]) + chargrams[8]/len(corpus[8])

))
authmeans = (chargrams[5]/len(corpus[5]) + chargrams[6]/len(corpus[6]) + chargrams[7]/len(corpus[7]) + chargrams[8]/len(corpus[8]) / 4
)
authmeans
docmeans
docchargrams
docchargrams = (docchargrams/len(corpus[0]))
distance.cosine(authmeans, docchargrams)
distance.cosine(docmeans, docchargrams)
distance.cosine(chargrams[1], chargrams[2])
distance.cosine(chargrams[1], chargrams[3])
distance.cosine(chargrams[2], chargrams[3])
from itertools import permutations
for x, y in permutations(range(1, 5)):
    print(distance.cosine(chargrams[x], chargrams[y]))
    
permutations(range(1, 5))
for x in permutations(range(1, 5)):
    print(x)
    
for x, y in permutations(range(1, 5)):
    print(x)
    
for x in combinations(range(1, 5)):
    print(x)
    
from itertools import combinations
for x in combinations(range(1, 5)):
    print(x)
    
for x in combinations(range(1, 5), 2):
    print(x)
    
for x, y in permutations(range(1, 5), 2):
    print(x)
    
for x, y in permutations(range(1, 5), 2):
    print(x, y)
    
for x, y in permutations(range(1, 5), 2):
    print(distance.cosine(x, y))
    
for x, y in permutations(range(1, 5), 2):
    print("%6f", distance.cosine(x, y))
    
for x, y in permutations(range(1, 5), 2):
    print("%6f" % distance.cosine(x, y))
    
for x, y in permutations(range(1, 5), 2):
    print("%6f" % distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in permutations(range(1, 5), 2):
    print(distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in combinations(range(1, 5), 2):
    print(distance.cosine(chargrams[x], chargrams[y]))
    
print(range(1,5))
for x in (range(1,5)):
    print(x)
    
for x, y in combinations(range(1, 5), 2):
    print(distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in permutations(range(1, 5), 2):
    print(distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in combinations(range(1, 5), 2):
    print(distance.cosine(chargrams[x], chargrams[y]))
    
delta_array = np.array()
delta_array = np.empty()
delta_array = np.empty([0])
for x, y in combinations(range(1, 5), 2):
    append(distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in combinations(range(1, 5), 2):
    delta_array.append(distance.cosine(chargrams[x], chargrams[y]))
    
delta_array = np.empty(0)
for x, y in combinations(range(1, 5), 2):
    delta_array.append(distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in combinations(range(1, 5), 2):
    delta_array = np.hstack(delta_array, distance.cosine(chargrams[x], chargrams[y]))
    
for x, y in combinations(range(1, 5), 2):
    delta_array = np.hstack((delta_array, distance.cosine(chargrams[x], chargrams[y])))
    
delta_array
delta_array.mean()
delta_array.std()
docproba
delta_array.std()
docproba
delta_array.mean()
authproba
docproba/delta_array.mean() * 100
delta_array.mean()/docproba * 100
delta_array.std()
delta_array.mean() + delta_array.std()
get_ipython().magic('save cosine_distance_experimentation.py')
get_ipython().magic('ls ')
get_ipython().magic('save cosine_distance_experimentation.py 0 598')

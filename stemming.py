import nltk, re, pprint
from nltk import word_tokenize

a = "whatevr strange man, i'm not letting some faggoted girlish femboy take away my freedom of defending my country "
porter = nltk.PorterStemmer()
tokens = word_tokenize(a)
ported = [porter.stem(t) for t in tokens]
print(ported)

lancaster = nltk.LancasterStemmer()
lancastered = [lancaster.stem(t) for t in tokens]
print(lancastered)
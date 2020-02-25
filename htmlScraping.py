from bs4 import BeautifulSoup
from urllib import request
import nltk, re, pprint
from nltk import word_tokenize

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')

raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)

print(tokens)
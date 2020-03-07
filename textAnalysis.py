from bs4 import BeautifulSoup
from urllib import request
import nltk, re, pprint
from nltk import word_tokenize

class textAnalysis:
    
   
    #---------------------------------------------------------------------------------------------#
    
    def parseHTML(self, url):
        html = request.urlopen(url).read().decode('utf8')
        raw = BeautifulSoup(html, 'html.parser').get_text()
        with open ("rawText.txt", "w", encoding = "utf-8") as f:
            f.write(raw)
        self.processRaw(raw)
    
    
    #---------------------------------------------------------------------------------------------#
    
    def parseText(self, url):
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        with open ("rawText.txt", "w", encoding = "utf-8") as f:
            f.write(raw)
        self.processRaw(raw)
    
    #---------------------------------------------------------------------------------------------#
    
    def processRaw(self, raw):
        tokens = word_tokenize(raw)
        print(len(tokens))
    
    #---------------------------------------------------------------------------------------------#
    
    def __init__(self, url = None, text = None, website_with_html = None):
        if website_with_html == 1:
            self.parseHTML(url)
        elif website_with_html ==0:
            self.parseText(url)
        if text != None:
            with open ("rawText.txt", "w",  encoding = "utf-8") as f:
                f.write(text)
            self.processRaw(text)
            
    #---------------------------------------------------------------------------------------------#
            
    
textAnalysis(url = "https://www.goodreads.com/review/list/48483884-michael-finocchiaro?shelf=post-modern", website_with_html = 1)
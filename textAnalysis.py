from bs4 import BeautifulSoup
from urllib import request
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import stopwords

class textAnalysis():
    
   
    #---------------------------------------------------------------------------------------------#
    
    def parseHTML(self, url):
        html = request.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        raw = soup.get_text()
        with open ("rawText.txt", "w", encoding = "utf-8") as f:
            f.write(text)
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
        stop_words = list(set(stopwords.words('english')))
        filtered_tokens = [w for w in tokens if w not in stop_words] 
        print(filtered_tokens)
    
    #---------------------------------------------------------------------------------------------#
    
    def __init__(self, url = None, text = None):
        if url != None:
            self.parseHTML(url)
        if text != None:
            with open ("rawText.txt", "w",  encoding = "utf-8") as f:
                f.write(text)
            self.processRaw(text)
            
    #---------------------------------------------------------------------------------------------#
            
    
textAnalysis(text = "Whatever man, I don't care for your faggoted relationships.")
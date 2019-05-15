'''
Created on May 14, 2019

@author: benjaminlitvin

Program takes 100 news articles and prints the ten most common words for each one
'''
import feedparser
from newspaper import Article 
import re
import string

searchTerm = "USA"
stream = feedparser.parse("http://news.google.com/news?q={" + searchTerm + "}&output=rss")

for page in stream.entries:
    article = Article(page['link'])
    article.download()
    article.parse()
    
    print(page['title'])
    print(page['link'])
    
    textArr = re.sub('[' + string.punctuation + ']', '', article.text).lower().split()
    
    wordCounter = {}
    for word in textArr:
        if word not in wordCounter:
            wordCounter[word] = 0
        wordCounter[word] = wordCounter[word] + 1
    
    
    for i in range(0,10):
        if len(wordCounter) == 0:
            print("no text")
            break
        v=list(wordCounter.values())
        k=list(wordCounter.keys())
        maxWord = k[v.index(max(v))]
        print(maxWord, wordCounter[maxWord])
        wordCounter.pop(maxWord)
    print('')
    
        
    
            
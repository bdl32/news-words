'''
Created on May 14, 2019

@author: benjaminlitvin

Program takes news articles and prints the ten most common words for each one
'''
import feedparser
from newspaper import Article 
import re
import string

searchTerm = "Ronaldo"
beginDate = "2019-1-1"
endDate = "2019-3-1"
stream = feedparser.parse("http://news.google.com/news?q={}+after:{}+before:{}&output=rss".format(searchTerm, beginDate, endDate))

for page in stream.entries:
    print(page['title'])
    print(page['link'])
    print(page['published'])
    
    article = Article(page['link'])
    article.download()
    if article.download_state == 1:
        print("URL Error\n")
        continue
    article.parse()
    
    
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
    
        
    
            
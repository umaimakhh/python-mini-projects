'''
Assigment No:0501 -  Dice and Cups 
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/l9-6YLsmztg
Date: 05/12/2020
I have not given or received any unauthorized assistance on this assignment
'''

from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import re

wordDictionary = {}
def decodeURL(url):
    '''returns url link used by each webpage by using urllib for fetching data from world wide web'''
    response = urlopen(url) # open URL for reading
    html = response.read() # read URL
    content = html.decode().lower()
    parser = SurfWebPage(url) # pass URL to HTMLParser class
    parser.feed(content)
    return parser.getUrlLinksList()

class SurfWebPage(HTMLParser):
    '''this class reperents the object of HTMLParser'''
    
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.urlLinks = []
        self.invalidDataTag = False
        self.invalidDataTags = ['head', 'meta', 'script', 'style'] # no need to deal with these data

    def handle_starttag(self,tag,attrs): # over ridding methods 
        ''''handles the content within the tags'''
        self.invalidDataTag = False #intial invalid tag
        global webMainPage 
        if tag == 'a': #identifies the tag
            for attr in attrs:
                if attr[0] == 'href':
                    joinURL = urljoin(self.url, attr[1]) # urlparse includes urljoin() for constructing absolute URLs from relative fragments.
                    extract = urlparse(joinURL, allow_fragments=True) #Parse a URL into 6 components: <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
                    if extract[1] == webMainPage: # extracting extract[1] to get hostname 
                        self.urlLinks.append(joinURL) # add url to be searched only on these links that are from the hostname

        if tag in self.invalidDataTags:
            self.invalidDataTag = True # tag is on of the tags we dont need to deal with
    
    def handle_data(self, data):  # over ridding methods
        '''handles the content within the tags'''
        global wordDictionary 
        if self.invalidDataTag == True: # data not needed of this tag
            return   

        string = data.strip() # data in list format
        if len(string) == 0: # if no data found
            return

        words = re.findall(r'\w+', string) # finding matching text patterns as list of strings
        for words in words:
            wordDictionary[words] = wordDictionary.get(words, 0) + 1
  
    def handle_endtag(self, tag): # over ridding methods
        '''handles the end tags'''
        self.invalidDataTag == False

    def getUrlLinksList(self):
        '''returns links url list'''
        return self.urlLinks # return list 

visited = set() 

def webCrawl(url):
    '''add the website which is visited gets the url'''
    global visited
    visited.add(url) # add url to visited 
    #if len(visited) > 2: # taking too long to commpute the result. 
        #return
    linkList = decodeURL(url) # get decoded url 
    for link in linkList:
        if link not in visited: # if not visited yet
            try:
                webCrawl(link)
            except:
                pass

def main():
    '''commutes the word dictionary of top 25 words the occurred the most'''
    global webMainPage 
    webMainPage ='scps.depaul.edu' # host name to verify only word count computed from this website
    mainWebPage = 'https://scps.depaul.edu/Pages/default.aspx' # main web page 
    webCrawl(mainWebPage) # start web crawling
    sortedWordDictionary = sorted(wordDictionary.items(), key=lambda kv: kv[1], reverse=True) #sort the list from highest to lowest
    
    print('\nTop 25 Word count from webiste - ',mainWebPage) # main heading 
    print('\n{:25} {:16} \n'.format('word','count'))
    for Item in sortedWordDictionary[:25]:
        print('{:25}  {:7} times'.format(Item[0],Item[1]))
  



main()

# output
# Top 25 Word count from webiste -  https://scps.depaul.edu/Pages/default.aspx

# word                      count

# and                          33452 times
# the                          27604 times
# faculty                      24880 times
# resources                    24224 times
# of                           23594 times
# depaul                       22244 times
# to                           19380 times
# campus                       17084 times
# a                            16400 times
# staff                        15696 times
# university                   14970 times
# for                          13978 times
# in                           13186 times
# student                      12492 times
# academic                     11640 times
# students                     10618 times
# professional                 10470 times
# directory                    10280 times
# continuing                    9938 times
# graduate                      9824 times
# studies                       9426 times
# scps                          9350 times
# information                   8242 times
# undergraduate                 8014 times
# email                         7750 times








    

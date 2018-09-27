#

from HTMLParser import HTMLParser
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding("utf8")


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if 'href' == attr[0] and str(attr[1]).startswith("/wiki/"):
                self.links.append(attr[1])

def getContent(url):
    html_page = urllib2.urlopen(url)
    text = html_page.read()
    html_page.close()
    return text

def getHref(html_text):
    # html_page = getContent(url)
    parser = MyHTMLParser()
    parser.links = []

    parser.feed(html_text)
    return parser.links

# check if the goal page is reached
def isGoalFound(content, goal):
    if goal in content:
        return True
    return False

def bfs(ROOT_PAGE, INIT_PAGE, GOAL):
    visited = [INIT_PAGE]
    # initialize the queue
    queue = []
    queue.append([INIT_PAGE, []])

    num_visit = 0 # keep track of pages visited, start from 1 (first page)
    num_len = 0 # keep track of steps to reach the goal

    while queue:
        # get the item from queue
        page = queue.pop()
        num_visit+=1
        visited.append(page[0])
        content = getContent(ROOT_PAGE + page[0])
        print page[0]
        seq = list(page[1])
        if isGoalFound(content, GOAL):
            res_seq = list(seq)
            res_seq.append(page[0])

            # output the result sequence
            print "result ",res_seq
            # output the visited nodes and length of result path
            print num_visit, len(res_seq)-1
            break

        for href in getHref(content):
            if href in visited or href in [q[0] for q in queue]:
                continue
            temp_seq = list(seq)
            temp_seq.append(page[0])
            # add new ones to the queue
            queue = [[href,temp_seq]] + queue
        time.sleep(2)

if __name__ == '__main__':
    ROOT_PAGE = 'https://en.wikipedia.org'
    INIT_PAGE = '/wiki/Association_football'
    # GOAL = 'Cristiano Ronaldo'
    GOAL = 'Ricardo Izecson dos Santos Leite'
    # GOAL = 'Pitch'
    # print len(getHref("https://en.wikipedia.org/wiki/Association_football"))
    # print getHref(ROOT_PAGE+INIT_PAGE)
    bfs(ROOT_PAGE, INIT_PAGE, GOAL)
    # getContent(ROOT_PAGE+INIT_PAGE)





# import requests
# from bs4 import BeautifulSoup
# import urllib2
# import re
#
# import sys
# reload(sys)
# sys.setdefaultencoding("utf8")
#
# html_page = urllib2.urlopen("https://en.wikipedia.org/wiki/Sport")
#
# soup = BeautifulSoup(html_page, "lxml")
#
# links = []
# for link in soup.findAll('a'):
#     href = str(link.get('href'))
#     if href.startswith('/wiki/'):
#
#         links.append(href)
#
# print(links)

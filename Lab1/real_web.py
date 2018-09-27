# -*- coding: UTF-8 -*-

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

class ShowProcess():
    """
    Progress bar class
    """
    i = 0 # current progress
    max_steps = 0 # total steps
    max_arrow = 50 # max length of the progress bar
    infoDone = 'done'

    # Initialization, takes in totoal steps and done info
    def __init__(self, max_steps, infoDone = 'Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    # show progress
    # Effect: [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) # calculate num of '>'
        num_line = self.max_arrow - num_arrow # calculate num of '-'
        percent = self.i * 100.0 / self.max_steps # calculate percentage, format: xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' # output string，'\r' means do not create new line
        sys.stdout.write(process_bar) # print to screen
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0

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

    cnt = 1
    stage = 1
    print "stage 1, " + str(cnt) + " in total"
    process_bar = ShowProcess(cnt, 'Done')
    while queue:
        if cnt > 0:
            cnt -=1
            process_bar.show_process()
        else:
            cnt = len(queue)-1
            stage += 1
            print ''
            print "stage "+str(stage) + ", " + str(cnt) + " in total" 
            process_bar = ShowProcess(cnt, 'Done')
            process_bar.show_process()


        # get the item from queue
        page = queue.pop()
        num_visit+=1
        visited.append(page[0])
        content = getContent(ROOT_PAGE + page[0])
        # print page[0]
        seq = list(page[1])
        if isGoalFound(content, GOAL):
            res_seq = list(seq)
            res_seq.append(page[0])
            print ''
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
    # INIT_PAGE = '/wiki/Brazil_national_football_team'
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

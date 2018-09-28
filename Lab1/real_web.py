# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# initialize the reference map for score calculation
score_dict = {}

# parser class gets list of tuples: [(link, hypertext),...]
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print tag
        i = 0
        while i < len(attrs)-1:
            if 'href' == attrs[i][0] and str(attrs[i][1]).startswith("/wiki/"):
                self.links.append((attrs[i][1], attrs[i+1][1]))
            i += 1

# progress bar class
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

# get page content
def getContent(url):
    html_page = urllib2.urlopen(url)
    text = html_page.read()
    html_page.close()
    return text

# get href links out of html text
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

# BFS to get path to the goal page
# abandoned because of inefficiency
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
            if href[0] in visited or href[0] in [q[0] for q in queue]:
                continue
            temp_seq = list(seq)
            temp_seq.append(page[0])
            # add new ones to the queue
            queue = [[href[0], temp_seq]] + queue
        time.sleep(2)


#
# Code for BEAM search
#

# score calculation for beam search
def getScore(string):
    score = 0
    for s in score_dict.keys():
        if s in string.lower():
            score += score_dict[s]
    return score

## Beam search
## its basically a best-first search with ranked list no longer than N
## We pick N = 20 here
def beam(ROOT_PAGE, INIT_PAGE, GOAL):
    ranked_list = [(INIT_PAGE, 0, [])]
    added_list = [INIT_PAGE]

    visited_count = 0

    while ranked_list:
        # pop the one with highest score
        current = ranked_list.pop()
        content = getContent(ROOT_PAGE + current[0])
        pg_score = content.count("QUERY")
        visited_count += 1

        if isGoalFound(content, GOAL):
            # print "================"
            ## output the sequence
            print "Solution Path:\n", current[2]+[current[0]]
            ## output the nodes visited and length of the answer
            print 'Nodes visited:', visited_count
            print 'Length of path: ', len(current[2])
            # stop searching
            break

        for href in getHref(content):
            if href[0] in added_list:
                continue
            added_list.append(href[0])
            score = getScore(str(href[1]))
            ranked_list.append((href[0], score, current[2]+[current[0]]))
            added_list.append(href[0])

        # sort the list by the score
        # highest score at the end where will be popped up first
        ranked_list = sorted(ranked_list, key=lambda x: x[1])
        # keep items in the list less than 20 to save memory
        ranked_list = ranked_list[-20:]

# main function
if __name__ == '__main__':
    ROOT_PAGE = 'https://en.wikipedia.org'
    INIT_PAGE = '/wiki/Sports'
    GOAL = 'Paolo Cesare Maldini'
    score_dict = {'soccer': 3, 'football': 3, 'paolo': 5, 'maldini': 5, 'serie a': 5,
                    'italy': 4, 'milan': 5, 'world cup':5, 'association': 3}

    ## another trial run
    # INIT_PAGE = '/wiki/Main_Page'
    # GOAL = 'Cristiano Ronaldo dos Santos Aveiro'
    # score_dict = {'soccer': 3, 'football': 3, 'cristiano': 5, 'madrid': 5, 'la liga': 5,
    #                 'portugal': 4, 'ronaldo': 5, 'world cup':5, 'association': 3}

    print 'Start page: ' + ROOT_PAGE+INIT_PAGE
    print 'Query words: ' + GOAL

    beam(ROOT_PAGE, INIT_PAGE, GOAL)

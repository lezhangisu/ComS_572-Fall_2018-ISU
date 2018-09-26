import sys
import Queue

# get page content
def getContent(path):
    content=''
    with open(path, 'r') as content_file:
        content += content_file.read()
    return content

# check if the goal page is reached
def isGoalFound(content, goal):
    if goal in content:
        return True
    return False

# extract href links from a splited token list
def getHrefList(token_list):
    href_list = []
    while True:
        if "HREF" not in token_list:
            break
        ind = token_list.index("HREF")+2
        html = token_list[ind]
        mark = ind
        ind = token_list[mark:].index(">")+mark
        ind2 = token_list[mark:].index("</A>")+mark
        label = ""
        for term in token_list[ind+1:ind2]:
            label+=term+" "
        href_list.append([html, label.strip()])
        token_list = token_list[ind2+1:]
    return href_list

## BFS
def bfs(folder, INIT_PAGE, GOAL):
    visited = [INIT_PAGE]
    # initialize the queue
    q = []
    q.append([INIT_PAGE, []])

    num_visit = 1 # keep track of pages visited, start from 1 (first page)
    num_len = 0 # keep track of steps to reach the goal

    while q:
        # get the item from queue
        page = q.pop()
        if page[0] not in visited:
            num_visit+=1
            visited.append(page[0])
        content = getContent(folder + page[0])
        seq = list(page[1])
        if isGoalFound(content, GOAL):
            res_seq = list(seq)
            res_seq.append(page[0])

            # output the result sequence
            print "result ",res_seq
            # output the visited nodes and length of result path
            print num_visit, len(res_seq)-1
            break

        for href in getHrefList(content.split()):
            if href[0] not in visited:
                temp_seq = list(seq)
                temp_seq.append(page[0])
                # add new ones to the queue
                q = [[href[0],temp_seq]] + q

# DFS non-recursive
def dfs_nr(start, folder, GOAL):

    # stack, last in first out
    stack = []
    # initialize the stack
    stack += [(start,[])] # list of tuples (node, [path previous to this node])
    visited = []

    while stack:
        # get the item from stack
        current = stack.pop()
        visited.append(current[0])
        content = getContent(folder + current[0])

        if isGoalFound(content, GOAL):
            print "result ", current[1]+[current[0]]
            print len(visited), len(current[1])
            break

        # get all the neighbor links on current page
        href_list = getHrefList(content.split())
        for href in href_list:
            # check if it's in the visited or the stack
            if href[0] in visited or href[0] in [s[0] for s in stack]:
                continue
            # push it to the stack
            stack.append((href[0], current[1]+[current[0]]))


## DFS recursive
def dfs_r(seq, current, folder, GOAL, visited):

    content = getContent(folder + current)

    visited += [current]

    if isGoalFound(content, GOAL):
        print "result ", seq+[current]
        print len(visited), len(seq)
        return visited, True

    next_list = getHrefList(content.split())

    if len(next_list) > 0:
        for href in next_list:
            if href[0] not in visited:
                visited, flag = dfs(seq+[current], href[0], folder, GOAL, visited)
                if flag:
                    return visited, flag

    return visited, False

#########
# Best First Search
#########

# count number of consecutive QUERY words in numerical order
def consec_q(s):
    max = 0
    count = 0
    prev = -1
    for substr in s.split():
        if "QUERY" in substr:
            num = substr.replace("QUERY", "")
            if prev == -1:
                count = 1
            elif int(num) - prev == 1:
                count += 1
            else:
                count = 1
            prev = int(num)

            if count > max:
                max = count
        else:
            prev = -1
            count = 0

    return max

## Best first search guided by heuristic functions
## it collects information on each page it visits
## and rank all the links by their scores
## then, pick the highest scored link and collect new info on the new page
## together with all previously collected info, a new ranked list is generated
## then pick the top one from the new list and repeat the process
def best(folder, INIT_PAGE, GOAL):
    ranked_list = [(INIT_PAGE, 0, [])]
    added_list = [INIT_PAGE]

    visited_count = 0

    while ranked_list:
        # click on the one with highest score
        current = ranked_list.pop()
        content = getContent(folder + current[0])
        pg_score = content.count("QUERY")

        visited_count += 1

        if isGoalFound(content, GOAL):
            ## output the result sequence
            print "result ", current[2]+[current[0]]
            ## output the nodes visited and length of the answer
            print visited_count, len(current[2])
            # stop searching
            break

        href_list = getHrefList(content.split())
        for href in href_list:
            if href[0] in added_list:
                continue
            added_list.append(href[0])
            # calculate number of 'QUERY's in the link text
            href_score1 = href[1].count("QUERY")
            # count number of consecutive 'QUERY's in the link text
            href_score2 = consec_q(href[1])
            # calculate the score for heuristics
            score = href_score2*1000+href_score1*100+pg_score
            # add new member to the list
            ranked_list.append((href[0], score, current[2]+[current[0]]))

        # sort the list by scores
        # the ones with highest score should at the bottom of the list
        # (the bottom of a list will pop up first)
        ranked_list = sorted(ranked_list, key=lambda x: x[1])

## Beam search
## its basically a best-first search with ranked list no longer than N
## We pick N = 20 here
def beam(folder, INIT_PAGE, GOAL):
    ranked_list = [(INIT_PAGE, 0, [])]
    added_list = [INIT_PAGE]

    visited_count = 0

    while ranked_list:
        # pop the one with highest score
        current = ranked_list.pop()
        content = getContent(folder + current[0])
        pg_score = content.count("QUERY")
        visited_count += 1

        if isGoalFound(content, GOAL):
            # print "================"
            ## output the sequence
            print "result ", current[2]+[current[0]]
            ## output the nodes visited and length of the answer
            print visited_count, len(current[2])
            # stop searching
            break

        href_list = getHrefList(content.split())
        for href in href_list:
            if href[0] in added_list:
                continue
            added_list.append(href[0])
            # calculate number of 'QUERY's in the link text
            href_score1 = href[1].count("QUERY")
            # count number of consecutive 'QUERY's in the link text
            href_score2 = consec_q(href[1])
            # calculate the score for heuristics
            score = href_score2*1000+href_score1*100+pg_score*1
            # add new member to the list
            ranked_list.append((href[0], score, current[2]+[current[0]]))

        # sort the list by the score
        # highest score at the end where will be popped up first
        ranked_list = sorted(ranked_list, key=lambda x: x[1])
        # keep items in the list less than 20 to save memory
        ranked_list = ranked_list[-20:]

def main(folder, INIT_PAGE, GOAL, usrInput, num):
    if num > 10: # Limit of invalid inputs. To avoid stack overflow
        sys.exit("Too many invalid inputs, terminate.")
    if usrInput == "1" or usrInput.lower() == "bfs":
        print "========BFS========"
        bfs(folder, INIT_PAGE, GOAL)
    elif usrInput == "2" or usrInput.lower() == "dfs":
        print "========DFS========"
        # dfs_r([], INIT_PAGE, folder, GOAL, [])
        dfs_nr(INIT_PAGE, folder, GOAL)
    elif usrInput == "3" or usrInput.lower() == "best":
        print "========BEST========"
        best(folder, INIT_PAGE, GOAL)
    elif usrInput == "4" or usrInput.lower() == "beam":
        print "========BEAM========"
        beam(folder, INIT_PAGE, GOAL)
    else: # re-prompt input from user
        print "** Invalid input **"
        print "Pick an algorithm:"
        print "(1.BFS; 2.DFS; 3.BEST; 4.BEAM)"
        reInput = str(raw_input())
        main(folder, INIT_PAGE, GOAL, reInput, num+1)

if __name__ == '__main__':
    intranet_num = sys.argv[1]
    mode = int(sys.argv[2])

    folder = 'given/intranets/intranet'+intranet_num+'/'
    INIT_PAGE = 'page1.html'
    GOAL = 'QUERY1 QUERY2 QUERY3 QUERY4'

    ## single run with user input
    if mode == 0:
        print "Pick an algorithm:"
        print "(1.BFS; 2.DFS; 3.BEST; 4.BEAM)"
        usrInput = str(raw_input())
        main(folder, INIT_PAGE, GOAL, usrInput, 0)
    ## multi runs all algorithms for one intranet
    else:
        print "***** Intranet_" + intranet_num + " *****"
        print "========BFS========"
        bfs(folder, INIT_PAGE, GOAL)
        print "========DFS========"
        dfs_nr(INIT_PAGE, folder, GOAL)
        print "========BEST========"
        best(folder, INIT_PAGE, GOAL)
        print "========BEAM========"
        beam(folder, INIT_PAGE, GOAL)

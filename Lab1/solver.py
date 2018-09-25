import sys
def getContent(path):
    content=''
    with open(path, 'r') as content_file:
        content += content_file.read()
    return content

def isGoalFound(content, goal):
    if goal in content:
        return True
    return False

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
    current_list = [[INIT_PAGE, []]]
    next_list = []

    # print current_list

    num_visit = 1 # keep track of pages visited, start from 1 (first page)
    num_len = 0 # keep track of steps to reach the goal
    while len(current_list) > 0:
        for page in current_list:
            if page[0] not in visited:
                num_visit+=1
                visited.append(page[0])
            content = getContent(folder + page[0])
            seq = list(page[1])
            if isGoalFound(content, GOAL):
                res_seq = list(seq)
                res_seq.append(page[0])
                print "================"
                print "result ",res_seq
                print num_visit, num_len
                next_list = []
                break

            for href in getHrefList(content.split()):
                if href[0] not in visited:
                    # next_list.append([href[0],list(seq).append(page[0])])
                    temp_seq = list(seq)
                    temp_seq.append(page[0])
                    next_list.append([href[0],temp_seq])
                    # print next_list



        current_list = list(next_list)
        next_list = []
        num_len+=1

## DFS recursive
def dfs(seq, current, folder, GOAL, visited):

    visited += [current]

    content = getContent(folder + current)

    if isGoalFound(content, GOAL):
        print "================"
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

## DFS non-recursive
def dfs_nr(current, folder, GOAL):
    stack, visited = [current], []

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.append(current)
        content = getContent(folder + current)

        if isGoalFound(content, GOAL):
            print "================"
            print current
            print len(visited)
            break

        next_list = getHrefList(content.split())

        for href in next_list:
            stack.append(href[0])


def main(folder, INIT_PAGE, GOAL, usrInput, num):
    if num > 10: # Limit of invalid inputs. To avoid stack overflow
        sys.exit("Too many invalid inputs, terminate.")

    if usrInput == "1" or usrInput.lower() == "bfs":
        bfs(folder, INIT_PAGE, GOAL)
    elif usrInput == "2" or usrInput.lower() == "dfs":
        dfs([], INIT_PAGE, folder, GOAL, [])
        # dfs_nr(INIT_PAGE, folder, GOAL)
    elif usrInput == "3" or usrInput.lower() == "best":
        print "BEST"
    elif usrInput == "4" or usrInput.lower() == "beam":
        print "BEAM"
    else:
        print "** Invalid input **"
        print "Pick an algorithm:"
        print "(1.BFS; 2.DFS; 3.BEST; 4.BEAM)"
        reInput = str(raw_input())
        main(folder, INIT_PAGE, GOAL, reInput, num+1)
    # content = getContent(INIT_URL)
    #
    # content_split = getContent(INIT_URL).split()
    #
    # print getHrefList(content_split)

    # DFS
    visited = []





if __name__ == '__main__':
    # folder = raw_input("Enter the target folder:\n")
    # print str(folder)
    folder = 'given/intranets/intranet1/'
    INIT_PAGE = 'page1.html'
    GOAL = 'QUERY1 QUERY2 QUERY3 QUERY4'

    print "Pick an algorithm:"
    print "(1.BFS; 2.DFS; 3.BEST; 4.BEAM)"
    usrInput = str(raw_input())
    main(folder, INIT_PAGE, GOAL, usrInput, 0)

#
# a = content_split.index("HREF")
# # print content_split[a+2]
#
# temp = a
# a = content_split[a+1:].index("HREF")
# # print content_split[temp+1+a+2]
#
# word = "QUERY1"
#
# # print isGoalFound(content, word)
#
# word = "QUERY1 QUERY2 QUERY3 QUERY4"
#
# # print isGoalFound(content, word)

# This is a problem solver written by Le Zhang, September, 2018
# It solves the Missionaries and Cannibals problem
# The states are in this format: 
#   [num_missionaries_left, num_cannibals_left, 
#                    num_missionaries_right, num_cannibals_right]
# Each move indicates the number of people changed on both sides within one step
# It uses BFS to give a shortest solution, may not be the only solution

# change the boat position
def change_boat_pos(flag):
    if flag:
        flag = False
    else:
        flag = True
    return flag    

# determin the direction of a move
def direct_a_move(flag, move):
    if flag:
        return move
    else:
        ret = []
        for num in move:
            ret.append(-num)
        return ret

# compute next state based on current state and move
def compute_state(state, move):
    ret = []
    for i in xrange(len(state)):
        ret.append(state[i]+move[i])
    return ret
        
# determin if a state is a valid state
def is_valid_state(state):
    for i in xrange(len(state)):
        if state[i] <0:
            return False
    if state[0] < state[1] and state[0] > 0:
        return False
    if state[2] < state[3] and state[2] > 0:
        return False
    return True

# determin if a state is a goal state
def terminate_state(state, goal_state):
  if len(state) != len(goal_state):
    return False
  for i in xrange(len(goal_state)):
    if state[i] != goal_state[i]:
      return False
  return True


init_state = [3,3,0,0] # initially everyone on the left side
goal_state = [0,0,3,3] # eventually everyone on the right side
init_boat_pos = True # it begin with a boat on the left side of the river

# positive moves are from left to right, negative moves are from right to left
# controled by the "make_a_move()" function
moves = [[0,-1,0,1],[0,-2,0,2],[-1,0,1,0],[-2,0,2,0],[-1,-1,1,1]]

# initialize current states
# format: [[state_1,[move_sequence_1]],[state_2,[move_sequence_2],...]
curr_states = []
curr_states.append([init_state,[]])

# initialize next states, empty
next_states = []

# initialize boat position
curr_boat_pos = init_boat_pos

# initialize solution
solution = []

# BFS algorithm to find a solution
solve_flag = False # flag indicates if it is solved
while not solve_flag:
  # go through each current state
  for i in xrange(len(curr_states)):
    state = list(curr_states[i][0])
    # try to apply all possible moves
    for j in xrange(len(moves)):
      move = direct_a_move(curr_boat_pos, moves[j])
      new_state = compute_state(state,move)
      # proceed only if the new state is valid
      if is_valid_state(new_state):
        # if it is a valid state, update the sequence of moves
        seq = list(curr_states[i][1])
        seq.append(j)
        # update the next_states list with current info
        next_states.append([new_state, seq])
        # check if this state is the goal state
        if terminate_state(new_state,goal_state):
          # if true, flip the flag
          solve_flag = True
          # save the move sequence as solution
          solution = list(seq)
          #break when solved
          break
    if solve_flag:
      #break when solved
      break
  # update boat position and current states
  curr_boat_pos=change_boat_pos(curr_boat_pos)
  curr_states = list(next_states)
  next_states = []
    
# Reproduce the move sequence
state = list(init_state)
print '0. init state',state
curr_boat_pos = True
# for each sequence id in solution, reproduce the move and its corresponding state
for i in xrange(len(solution)):
  move = direct_a_move(curr_boat_pos, moves[solution[i]])
  state = compute_state(state,move)
  print str(i+1)+'. action',move,', state',state
  curr_boat_pos = change_boat_pos(curr_boat_pos)

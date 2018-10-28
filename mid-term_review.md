# 2018 Fall ComS 572 Mid-Term Review

## 1. Intro to AI

### Turing Test

### What is AI

Thinking humanly, or Thinking rationally

Acting humanly, or Acting rationally


## 2. Intelligent Agents

### Rational Agent

Rational behavior: doing the right thing

The right thing: that which is expected to maximize goal
achievement, given the available information

An agent is an entity that perceives and acts

A rational agent is one that acts so as to achieve the best outcome

#### Rationality != omniscience != perfection
An omniscient agent knows the actual outcome of its
actions.

Rationality maximizes expected performance

Perfection maximizes actual performance.

#### Rationality requires:
1. Information gathering/exploration  To maximize future rewards
2. Learn from percepts
3. Extending prior knowledge
4. Being autonomous
5. Compensate for partial prior knowledge, adapt

### Environment Types
 Types | Chess | Backgammon | Taxi Driving
------ | ----- | ---------- | ------------
Observable?? | Full | Full | Partial
Deterministic?? | Yes | No | No
Static?? | Yes/Semi | Yes | No
Discrete?? | Yes | Yes | No
Single-agent?? | No | No | No

The simplest environment is Fully observable, deterministic, static, discrete, and single-agent.

Most real situations are: Partially observable, stochastic, dynamic, continuous, and multi-agent.

### Possible Questions:

HW1 Problem 2 (T/F)

1. An agent that senses only partial information about the state cannot be perfectly rational.

<details><summary>answer</summary>
<p>

**False**.
```
The vacuum-cleaning agent example from textbook at page 38 is rational but doesnt observe the state of the square that is adjacent to it. Thus, it is not true.
```

</p>
</details>

2. There exist task environments in which no pure reflex agent can behave rationally.

<details><summary>answer</summary>
<p>

**True**.
```
Pure reflex agent will not be rational in any task where memory of previous moves is required. For instance, a battleship game.
```

</p>
</details>

3. There exists a task environment in which every agent is rational.

<details><summary>answer</summary>
<p>

**True**.
```
Assume we have a task environment in which all actions (including no action) give the same reward, then every agent is rational at this point of view.
```

</p>
</details>

4. The input to an agent program is the same as the input to the agent function.

<details><summary>answer</summary>
<p>

**False**.
```
The input to an agent function is the percept history. However, the input to an agent program is only the current percept; it is up to the agent’s program to record any relevant history needed to make decisions.
```

</p>
</details>

5. Every agent function is implementable by some program/machine combination.

<details><summary>answer</summary>
<p>

**False**.
```
An agent function is an abstract mathematical description while the agent program is a concrete implementation running within some physical system. Since the agent function is just an abstract description it is completely possible that there exists cases in which an agent program will fail due to memory limitation.
```

</p>
</details>

6. Suppose an agent selects its action uniformly at random from the set of possible actions. There exists a deterministic task environment in which this agent is rational.

<details><summary>answer</summary>
<p>

**True**.
```
Again, like assertion c, considering an environment where all actions always give equal reward. In this case, the agent is still rational because it gets same reward for any sequence of actions.
```

</p>
</details>

7. It is possible for a given agent to be perfectly rational in two distinct task environments.

<details><summary>answer</summary>
<p>

**True**.
```
Consider two environments based on betting on the outcomes of tossing two coins. In environment A, the coins are fair, in environment B, the coins are biased to always give heads. The agent can bet on what the sum of the heads appears in each toss, with equal reward on all possible outcomes for guessing correctly. The agent that always bets on 2 will be rational in both cases.
```

</p>
</details>

8. Every agent is rational in an unobservable environment.

<details><summary>answer</summary>
<p>

**False**.
```
Built-in knowledge can give a rational agent in an unobservable environment. A vacuum-agent that cleans, moves, cleans moves would be rational, but one that never moves would not be.
```

</p>
</details>

9. A perfectly playing poker-playing agent never loses.

<details><summary>answer</summary>
<p>

**False**.
```
For example, let two perfectly playing agents play against each other. One of them must lose, otherwise it is not a poker game.
```

</p>
</details>

## 3. Solving Problems by Searching

### Problem Formulation

1. An initial state
2. Actions: ACTIONS(s) applicable actions in s
3. Transition model (or Successor function, or Operators)
4. Goal test
5. Path Cost

### Search Algorithms

#### Tree Search Algorithm

Root to leaves

Failure to detect repeated states can turn a solvable problems into unsolvable ones.

#### Graph Search Algorithm

Node to its neighbors, repeat.

#### BFS, DFS
Traditional search algorithms

#### Depth-Limited Search
DFS with limited depth k

#### Iterative Deepening DFS
Multi iterations of DLS from k=1 to k=n

### Informed Search (Heuristic)

#### Greedy Search
Expand node that appears to be closest to goal

#### A* Search
Avoid expanding paths that are already expensive

### Possible Questions
HW3 Problem 2

Given a graph or tree, show the paths for BFS/DFS/DLS/IDS...

## 4. Beyond Classical Search

### Local Search

Local search: keep a single current state and move to neighboring states to improve it

### Local Beam Search
Keep track of k states instead of one
1. Initially: k random states
2. Next: determine all successors of k states
3. If any of successors is goal  finished
4. Else select k best from successors and repeat.

### Possible Questions
None

## 5. Adversarial Search

### Games

Games of deterministic, perfect information: chess, checkers

Stochastic games: backgammon

Partially observable games: bridge, poker

### Min-max Algorithm

Self move: Max

Opponent move: Min

### Alpha-Beta Search

Altered version of Min-Max, if min > max, means we are losing at this branch, stop.

### Possible Questions
None

## 6. Constraint Satisfaction Problems

### CSP Formulation
1. Variables
2. Domains
3. Constraints

### Possible Questions
HW4 Problem 1

## 7. Logical Agents

### CNF (Conjunctive normal form)
~(A and B) = ~A or ~B

~(A or B) = ~A and ~B

A => B = A and B

### Resolution
To prove A->B, you need to show that A and ~B is empty clause or cannot be satisfied.

### Possible Questions
HW4 Problem 3 and 4


## 8. First-Order Logic

### Possible Questions
HW5 Problem 1


## 9. Inference in First-Order Logic

### Unification

Match variables between two expressions, from left to right.

e.g.

P(A, B), P(x, y) we have {x/A, y/B}

P(A, Q(y)), P(x, y) we cannot unify y/Q(y)


### Possible Questions
HW5 Problem 2

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

HW1 Problem2 (T/F)

1. An agent that senses only partial information about the state cannot be perfectly rational.
**False**. The vacuum-cleaning agent example from textbook at page 38 is rational but doesnt observe the state of the square that is adjacent to it. Thus, it is not true.
2. There exist task environments in which no pure reflex agent can behave rationally.
**True**. Pure reflex agent will be rational in any task where memory of previous moves is required. For instance, a battleship game.
3. There exists a task environment in which every agent is rational.
**True**. Assume we have a task environment in which all actions (including no action) give the same reward, then every agent is rational at this point of view.
4. The input to an agent program is the same as the input to the agent function.
**False**. The input to an agent function is the percept history. However, the input to an agent program is only the current percept; it is up to the agent’s program to record any relevant history needed to make decisions.
5. Every agent function is implementable by some program/machine combination.
**False**. An agent function is an abstract mathematical description while the agent program is a concrete implementation running within some physical system. Since the agent function is just an abstract description it is completely possible that there exists cases in which an agent program will fail due to memory limitation.
6. Suppose an agent selects its action uniformly at random from the set of possible actions. There exists a deterministic task environment in which this agent is rational.
**True**. Again, like assertion c, considering an environment where all actions always give equal reward. In this case, the agent is still rational because it gets same reward for any sequence of actions.
7. It is possible for a given agent to be perfectly rational in two distinct task environments.
**True**. Consider two environments based on betting on the outcomes of tossing two coins. In environ- ment A, the coins are fair, in environment B, the coins are biased to always give heads. The agent can bet on what the sum of the heads appears in each toss, with equal reward on all possible outcomes for guessing correctly. The agent that always bets on 2 will be rational in both cases.
8. Every agent is rational in an unobservable environment.
**False**. There is a simple case in which this can be proven false; the vacuum agent that cleans. If the agent moves but does not clean, it would not be rational.
9. A perfectly playing poker-playing agent never loses.
**False**. For example, let two perfectly playing agents play against each other. One of them must lose, otherwise it is not a poker game.

## 3. Solving Problems by Searching

## 4. Beyond Classical Search

## 5. Adversarial Search

## 6. Constraint Satisfaction Problems

## 7. Logical Agents

## 8. First-Order Logic

## 9. Inference in First-Order Logic

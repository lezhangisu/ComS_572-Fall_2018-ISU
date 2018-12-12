**2018 Fall ComS 572 Final Exam Review**

## Ch13. Quantifying Uncertainty

### Basic Probability Notation

P(A|B) = P(A and B)/P(B)

P(A and B) = P(A|B)P(B)

### Bayes Rule

P(A|B) = P(B|A)P(A) / P(B)

### Joint Distribution

P(x_1,...,x_n) =PI_i P(x_i | x_1, ... x_(n-1))

## Ch14. Bayesian Networks

### Bayesian Network

Bayesian network is a directed acyclic graph.

- Nodes: random variables of interest
- Edges: direct (causal) influences
- Each node is annotated with a conditional distribution P(Xi | Parents(Xi))
- Each variable is asserted to be conditionally independent of its non-descendants given its parents.

### Markov blanket

A **Markov Blanket** for X is a set of variables B which, when known, will render every other variable irrelevant to X, i.e., I(X, B, R), where R is the set of all variables other than X and B → feature selection

Each node is conditionally independent of all others given its Markov blanket: parents + children + children’s parents

Queries can be posed to a BN: **Probability of Evidence query**, the probability of some variable instantiation e, Pr(e)

### Reasoning with BNs

**Most probable explanation** (MPE): identify an instantiation x1,...,xn for which P(x1,...,xn | e) is maximal.

**Maximum a posteriori hypothesis** (MAP): find an instantiation
m of variables M ⊂ V for which P(m | e) is maximal

## Ch18-1. Machine Learning

AI is the enterprise of design and analysis of intelligent agents.

They acquire knowledge by learning.

### Data Mining

Raw data is useless: need techniques to automatically extract information from it.

Machine learning techniques: automatically
finding patterns in data.

**Supervised Learning**: given examples of inputs and corresponding desired outputs, predict outputs on future inputs.

- Classification: target has finite domain - categories
- Regression: target has continuous domain

**Unsupervised Learning**: given only inputs, automatically discover representations, features, structure, etc.

- Clustering: group similar instances, e.g. automatically group
(unlabeled) handwritten digits

**Reinforcement Learning**: occasional rewards or punishments

## Ch18-2. Decision Trees

- Each internal node tests on an attribute
- Each branch corresponds to an attribute value
- Each leaf node corresponds to a class label

### Constructing decision trees

- First consider discrete valued attributes
 - Aim: find a small tree consistent with the training
examples
 - Idea: (recursively) choose "most significant" attribute as
root of (sub)tree

- Strategy: top down learning using recursive divide-andconquer
process
 - First: select attribute for root nod. Create branch for each possible attribute value
 - Then: split instances into subsets.
One for each branch extending from the node
 - Finally: repeat recursively for each branch, using only instances that reach the branch
 - Stop if all instances have the same class

### Entropy

The expected information required to determine an outcome
(i.e., class value) of a random variable, is its entropy

Entropy(p1,...,pn) = -p1 log p1 - ... - pn log pn

Less entropy, purer the result is.

**Information gain** (mutual information): information
before splitting – information after splitting

Select attribute with most gain as root, then select second most gain as second layer... so on ....

### Overfitting in Decision Trees

- The algorithm grows each branch of the tree to
perfectly classify the training examples
- When there is noise in the data -- adding an
incorrect example leads to a more complex tree
with irrelevant attributes
- When the number of training examples in a
branch is too small -- poor estimates of entropy,
irrelevant attributes may partition the examples
well by accident

Prevent overfitting the training data: “prune” the
decision tree

Two strategies:

-  Prepruning
 - stop growing a branch when information becomes
unreliable, based on statistical significance test
- Postpruning
 - take a fully-grown decision tree and discard unreliable
parts

Postpruning is preferred in practice—prepruning
can “stop early”

### Other trees

Regression tree: “decision tree” where each leaf
predicts a numeric quantity

Model tree: “regression tree” with linear
regression models at the leaf nodes

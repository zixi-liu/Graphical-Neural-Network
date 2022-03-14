# Message Passing & Node Classification

**Semi-supervised Node Classification:** Given a network with labels on some labels, how do we assign labels to all other nodes in the network?

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/node-corr.PNG" alt="Node Correlation"/>

## Collective Classification

**Intuition:** Simultaneous classification of interlinked nodes using correlations;

**Markov Assumption:** The label Y of one node v depends on the labels of its neighbors Nvs:
- P(Yv) = P(Yv | Nv)

### Collective Classification involves 3 steps:
- **Local Classifier:** Predict labels based on node features;
- **Relational Classifier:** Learns a classifier to label one node based on the labels/attributes of its neighbors;
- **Collective Inference:** Apply relational classifier to each node iteratively; Iterate until the inconsistency between neighboring labels is minimized;

## Relational Classification
 
**Idea:** Class probability Yv of node v is a weighted average of class probabilities of its neighbors.

- For labeled nodes v, initialize label Yv with ground-truth label Yv∗.
- For unlabeled nodes, initialize Yv = 0.5.
- Update all nodes in a random order until convergence or until maximum number of iterations is reached.

## Iterative Classifiction

**Idea:** Classify node v based on its attributes fv as well as labels Zv of neighbor set Nv.

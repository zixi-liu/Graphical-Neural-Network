# Message Passing & Node Classification

**Semi-supervised Node Classification:** Given a network with labels on some labels, how do we assign labels to all other nodes in the network?

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/node-corr.PNG" alt="Node Correlation"/>

## Collective Classification

**Intuition:** Simultaneous classification of interlinked nodes using correlations

**Markov Assumption:** The label Y of one node v depends on the labels of its neighbors Nvs:
- P(Yv) = P(Yv | Nv)

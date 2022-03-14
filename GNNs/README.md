# GNNs

### Tasks on Networks

- **Node classification:** Predict a type of a given node;
- **Link prediction:** Predict whether two nodes are linked;
- **Community detection:** Identify densely linked clusters of nodes;
- **Network similarity:** How similar are two (sub)networks;

## Deep Graph Encoder

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-encoder.PNG" alt="Deep Graph Encoder"/>

## Graphical Neural Networks

**Idea:** Node's neighborhood defines a computatinoal graph.

### Aggregate Neighbors

**Basic approach:** Average neighbor messages and apply a neural network.

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/neighbor-agg.PNG" alt="Neighborhood Aggregation" width = "600px"/>

### Unsupervised Training

**“Similar” nodes have similar embeddings**
 
<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/gnn-embedding.PNG" alt="Unsupervised embedding" width = "400px"/>

- Where yu,v = 1 when node u and v are similar;
- CE is the cross entropy;
- DEC is the decoder such as inner product;

**Node similarity can be anything from:**
- Random walks (node2vec, DeepWalk, struc2vec);
- Matrix factorization;
- Node proximity in the graph;

### Supervised Training

**Directly train the model for a supervised task (e.g., node classification).**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/cross-entropy.PNG" alt="Cross Entropy Loss" width = "500px"/>


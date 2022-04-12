# GNNs

- [[GCN] Graph Convolutional Network](#Graph-Convolutional-Network)

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/gnn_categories.png" alt="GNN Categories"/>


### Tasks on Networks

- **Node classification:** Predict a type of a given node;
- **Link prediction:** Predict whether two nodes are linked;
- **Community detection:** Identify densely linked clusters of nodes;
- **Network similarity:** How similar are two (sub)networks;

## Deep Graph Encoder

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-encoder.PNG" alt="Deep Graph Encoder"/>

## Graphical Convolutional Networks

**Idea:** Node's neighborhood defines a computational graph.

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

### Model Design

1. Define a neighborhood aggregation function;
2. Define a loss function on the embeddings;
3. Train on a set of nodes, i.e., a batch of compute graphs;
4. Generate embeddings for nodes as needed;

## GNN Frameworks

### A Single GNN Layer 

GNN = Message + Aggregation

- **Message:**  Each node will create a message, which will be sent to other nodes later; m(l) = MSG(l) * h(l-1)

- **Aggregation:** Each node will aggregate the messages from node v’s neighbors

- **Nonlinearity (activation function)** 

### Graph Convolutional Network 

[[arXiv]](https://arxiv.org/pdf/1609.02907.pdf)

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/gcn.PNG" alt="GCN" width = "400px"/>

GCN model scales linearly in the number of graph edges and learns hidden layer representations that encode both local graph structure and features of nodes.

Traditional graph-based semi-supervised learning: classifying nodes where labels are only available for a small subset of nodes.
- Label information is smoothed over the graph via some form of implicit graph-based regularization.

**GCN:** Encode graph structure directly using a neural network model f(X, A) and train on a supervised target L0 for all nodes with labels (avoiding graph-based regularization in the loss function).

**Fast Approximate Convolutions on Graphs**

- Multi-layer Graph Convolutional Network (GCN)
  
<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/multi-gcn.png" alt="GCN" width = "400px"/>

- Spectral Graph Convolutions
  - Spectral convolutions on graphs defined as the multiplication of a signal x ∈ RN (a scalar for every node) with a filter gθ = diag(θ) parameterized by θ ∈ RN in the Fourier domain: gθ * x = Ugθ UTx.

- Layer-Wise Linear Model
  - A neural network model based on graph convolutions can therefore be built by stacking multiple convolutional layers, each layer followed by a point-wise non-linearity. We intuitively expect that such a model can alleviate the problem of overfitting on local neighborhood structures for graphs with very wide node degree distributions, such as social networks, citation networks, knowledge graphs and many other real-world graph datasets. Additionally, for a fixed computational budget, this layer-wise linear formulation allows us to build deeper models, a practice that is known to improve modeling capacity on a number of domains.

**Semi-Supervised Node Classification**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/gcn-visualization.png" alt="GCN Visualization" width = "800px"/>

[**Code Example**](https://github.com/tkipf/gcn)

**GraphSage** [[arXiv]](https://arxiv.org/pdf/1706.02216.pdf)

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/graphsage.PNG" alt="GraphSage" width = "600px"/>

**Graph Attention Networks** [[arXiv]](https://arxiv.org/pdf/1710.10903.pdf)

**Idea:** Compute embeddin of each node in the graph following an attention strategy:
- Nodes attend over their neighborhoods’ message;
- Implicitly specifying different weights to different nodes in a neighborhood;

### Stacking Layers of a GNN

**The over-smoothing problem**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/over-smooth.PNG" alt="Over Smooth" />

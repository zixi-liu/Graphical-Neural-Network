# GNNs Roadmap 

Table of Content

- [A Refresher on Graph Learning](#A-Refresher-on-Graph-Learning)
- [GNN Model](#Graphical-Convolutional-Networks)
- [Frequent Subgraph Mining with GNNs](#Frequent-Subgraph-Mining-with-GNNs)

## A Refresher on Graph Learning

- [[IEEE] Graph Learning, A survey (2021)](https://arxiv.org/pdf/2105.00696.pdf)


This paper catogorize eisting graph learning methods into the following four categories: graph signal processing (GSP) based methods, matrix factorization based methods, random walk based methods, and deep learning based methods.

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/graph-learning.png" alt="Graph learning"/>

According to the attributes of vertices, edges and subgraph, graph learning tasks can be divided into three categories, which are *vertices based*,
*edges based*, and *subgraph based*, respectively.

- The relationships among vertices in a graph can be exploited for, e.g.,classification, risk identification, clustering, and community detection. 
- By judging the presence of edges between two vertices in graphs, we can perform recommendation and knowledge reasoning, for instance. 
- Based on the classification of subgraphs, the graph can be used for, e.g., polymer classification, 3D visual classification, etc.

**Graph Signal Processing (GSP)**

Design suitable graph sampling methods to preserve the features of the original graph, which aims at recovering the original graph efficiently.

- [[IEEE] Learning Laplacian Matrix in Smooth Graph Signal Representations (2016)](https://www.oxford-man.ox.ac.uk/wp-content/uploads/2020/03/Learning-Laplacian-Matrix-in-Smooth-Graph-Signal-Representations.pdf)

**Matrix Factorization Based Methods**

**Random Walk Based Methods**

Generally, random walk can be regarded as a Markov process. The next state of the process is only related to last state, which is known as Markov chain.
- 1） Structure Based Random Walks: Deep Walk, Node2vec, LINE etc.
- 2） Structure and Vertex Information Based Random Walk: Struc2vec
- 3） Random Walks in Heterogeneous Networks:
  - 3 common inference method in general: statistical relational learning (SRL), latent factor models (LFM) and random walk models (RWM). 
  - Path ranking algorithm (PRA) is a path finding method using random walks to generate relational features on graph data. However, PRA cannot predict - connection between two vertices if there does not exist a path between them. 
- 4） Random Walks in Time-varying Networks: 
  - CTDNE model for continuous dynamic network embedding based on random walk with ”chronological” paths which can only move forward as time goes on.
  - HTNE can well integrate the Hawkes process into network embedding so that the influence of historical neighbors on the current neighbors can be accurately captured.
  - GraphSAGE was presented to efficiently generate embeddings for new vertices in a dynamical network. GraphSAGE designs a function to generate embedding for a vertex with features of the neighborhoods locally. After sampling neighbors of a vertex, GraphSAGE uses different aggregators to update the embedding of the vertex. However, current graph neural methods are proficient of only learning local neighborhood information and cannot directly explore the higher-order proximity and the community structure of graphs.

**Deep Learning on Graphs**

A brief history of algorithms of deep learning on graphs.

![image](https://user-images.githubusercontent.com/46979228/170844170-f91588b5-7da1-4d09-84d2-9a1f4e03305f.png)

- 1） [[GCN] Graph Convolutional Network](#Graphical-Convolutional-Networks)
  - Time Domain and Spectral Methods: graph Laplacian matrix (spectral graph CNN), spectral based methods have many applications, such as vertex classification, traffic forecasting, and action recognition etc.
  - Space Domain and Spatial Methods: [Large scale graph convolution network (LGCN)](https://arxiv.org/pdf/1808.03965.pdf), [Neural FP](https://papers.nips.cc/paper/2015/file/f9be311e65d81a9ad8150a60844bb94c-Paper.pdf)
- 2） Graph Attention Networks
- 3） Graph Auto-Encoders
- 4） Graph Generative Networks
- 5） Graph Spatial-Temporal Networks


[**Graph neural networks: A review of methods and applications (Page 14 for a list of applications)**](https://arxiv.org/pdf/1812.08434.pdf)

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/gnn_categories.png" alt="GNN Categories"/>


### Tasks on Networks

- **Node classification:** Predict a type of a given node;
- **Link prediction:** Predict whether two nodes are linked;
- **Community detection:** Identify densely linked clusters of nodes;
- **Network similarity:** How similar are two (sub)networks;

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

[A Short Intro](https://tkipf.github.io/graph-convolutional-networks/)

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

[**Code Example**](https://github.com/tkipf/pygcn/)

### GraphSage 

[[arXiv]](https://arxiv.org/pdf/1706.02216.pdf)

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/graphsage.PNG" alt="GraphSage" width = "600px"/>

**Graph Attention Networks** [[arXiv]](https://arxiv.org/pdf/1710.10903.pdf)

**Idea:** Compute embeddin of each node in the graph following an attention strategy:
- Nodes attend over their neighborhoods’ message;
- Implicitly specifying different weights to different nodes in a neighborhood;

### Stacking Layers of a GNN

**The over-smoothing problem**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/over-smooth.PNG" alt="Over Smooth" />


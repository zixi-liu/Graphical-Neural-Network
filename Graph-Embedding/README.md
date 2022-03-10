# Node Embeddings

**Map nodes into a d-dimensional embedding space such that similar nodes in the network are mebedded close together.**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-example.PNG" alt="Deep Walk"/>

A first step in machine learning for graphs is to extract graph features.

## Methods

1) Vector Point–Based Graph Embedding Methods
  - **Random Walk**
    - **Deep Walk** [KDD 2014] [DeepWalk: Online Learning of Social Representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf)
    - **Node2Vec** [KDD 2016] [node2vec: Scalable Feature Learning for Networks](https://www.kdd.org/kdd2016/papers/files/rfp0218-groverA.pdf)
    - **LINE** [WWW 2015] [LINE: Large-scale Information Network Embedding](https://arxiv.org/pdf/1503.03578.pdf)
    - **SDNE** [KDD2016] [Structural Deep Network Embedding]https://arxiv.org/pdf/1503.03578.pdf)
    - **Struc2Vec** [KDD 2017] [struc2vec: Learning Node Representations from Structural Identity](https://arxiv.org/pdf/1704.03165.pdf)
 
2) Gaussian Distribution–Based Graph Embedding

3) Dynamic Graph Embedding

## Deep Walk [[Video]](https://www.youtube.com/watch?v=aZNtHJwfIVg)

**Deep Walk** learns representation for vertices from a stream of short random walks, using optimization techniques originally designed for language modeling (skip gram).

**Overview of Deep Walk**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/overview-deep-walk.PNG" alt="Overview" width = "900px" />

Note: The representation Φ is updated to maximize the probability of v1 co-occurring with its context {v3, v5}.

**Algorithms**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-algorithm-1.PNG" alt="Deep Walk Algorithm 1" />

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-algorithm-2.PNG" alt="Deep Walk Algorithm 2" />

**Examples - wiki data**

 <img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-plot.PNG" alt="Overview" width = "300px" />
 
 ## Node2Vec

**Node2Vec** define a flexible notion of a node’s network neighborhood and design a biased random walk procedure, which efficiently explores diverse neighborhoods. The neighborhoods Ns(u) are not restricted to just immediate neighbors but can have vastly different structures depending on the sampling strategy S.

**Classic Search Strategies**

- **Breadth-first Sampling (BFS)** The neighborhood Ns is restricted to nodes which are immediate neighbors of the source.
- **Depth-first Sampling (DFS)** The neighborhood consists of nodes sequentially sampled at increasing distances from the source node. 

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/sampling-strategy.PNG" alt="Overview" width = "400px" />

**Homophily and Structural Equivalence**

- Under the homophily hypothesis, nodes that are highly interconnected and belong to similar network clusters or communities should be embedded closely together. BFS lead to embeddings that correspond closely to structural equivalence. By restricting search to nearby nodes, BFS obtains a microscopic view of the neighborhood of every node.

- Under the structural equivalence hypothesis, nodes that have similar structural roles in networks should be embedded closely together. DFS can explore larger parts of
the network as it can move further away from the source node u. In DFS, the sampled nodes more accurately reflect a macro-view of the neighborhood.

**A Flexible Biased Random Walk**

- The simplest way to bias our random walks would be to sample the next node based on the static edge weights.

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/random-walk-node2vec.PNG" alt="random walk" width = "300px" />

- **Return parameter, p** Parameter p controls the likelihood of immediately revisiting a node in the walk.

- **In-out parameter, q** Parameter q allows the search to differentiate between “inward” and “outward” nodes. 

**Algorithms**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/node2vec.PNG" alt="node2vec"  />

[[More Resources]](http://snap.stanford.edu/node2vec/)

[[Github]](https://github.com/aditya-grover/node2vec)

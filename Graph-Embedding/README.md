# Node Embeddings

**Map nodes into a d-dimensional embedding space such that similar nodes in the network are mebedded close together.**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/node-embeddings.png" alt="GNN" width = "500px"/>

## Methods

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-example.PNG" alt="Deep Walk"/>

- **Shallow Encoding**
- **Random Walk**
  - **Deep Walk** [KDD 2014] [DeepWalk: Online Learning of Social Representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf)
  - **Node2Vec** [KDD 2016] [node2vec: Scalable Feature Learning for Networks](https://www.kdd.org/kdd2016/papers/files/rfp0218-groverA.pdf)
  - **LINE**
  - **SDNE**
  - **Struc2Vec**


## Deep Walk

**Deep Walk** learns representation for vertices from a stream of short random walks, using optimization techniques originally designed for language modeling.

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/overview-deep-walk.PNG" alt="Overview" width = "800px"/>



**Algorithm**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-algorithm-1.PNG" alt="Deep Walk Algorithm 1" />

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-algorithm-2.PNG" alt="Deep Walk Algorithm 2" />

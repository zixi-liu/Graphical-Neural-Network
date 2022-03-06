# Node Embeddings

**Map nodes into a d-dimensional embedding space such that similar nodes in the network are mebedded close together.**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/node-embeddings.png" alt="GNN" width = "600"/>

## Methods

- **Shallow Encoding**
- **Random Walk**
  - **Deep Walk** [KDD 2014] [DeepWalk: Online Learning of Social Representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf)
  - **Node2Vec** [KDD 2016] [node2vec: Scalable Feature Learning for Networks](https://www.kdd.org/kdd2016/papers/files/rfp0218-groverA.pdf)


### Deep Walk

**Deep Walk** learn representation for vertices from a stream of short random walks, using optimization techniques originally designed for language modeling.

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-example.PNG" alt="Deep Walk" width = "600"/>

**Algorithm**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/deep-walk-algorithm-1.PNG" alt="Deep Walk Algorithm" />

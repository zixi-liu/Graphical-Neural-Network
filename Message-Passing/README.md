# Message Passing & Node Classification

**Semi-supervised Node Classification** 

- Given a network with labels on some labels, how do we assign labels to all other nodes in the network?

**Two explanations for why behaviors of nodes in networks are correlated**

- Homophily
- Influence

**Classification label of a node in network may depend on:**
- Features of *v*
- Labels of the nodes in *v*’s neighborhood
- Features of the nodes in *v*’s neighborhood

**Common Applications**

- Document classification
- Part of speech tagging
- Spam and fraud detection

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/node-corr.PNG" alt="Node Correlation" width = '400px'/>


## Semi-supervised binary node classification

- Relational Classification
- Iterative Classification
- Correct& Smooth


### 1. Relational Classification
 
**Idea:** Class probability Yv of node v is a weighted average of class probabilities of its neighbors.

- For labeled nodes v, initialize label Yv with ground-truth label Yv∗.
- For unlabeled nodes, initialize Yv = 0.5.
- Update all nodes in a random order until convergence or until maximum number of iterations is reached.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/46979228/177005644-537b5998-6084-46f2-9673-6def04cfd7ab.png">

- If edges have strength/weight information, Av,u can be the edge weight between v and u.


### 2. Iterative Classifiction

- Relational classifier does not use node attributes. 

**Idea:** Classify node v based on its attributes fv as well as labels Zv of neighbor set Nv.

**Input:** Graph
- fv: feature vector for node v;
- Some nodes v are labeled with Yv;

**Task:** Predict label of unlabeled nodes;

**Approach:** Train two classifiers:
- Predict node label based on node feature vector fv. This is called *base classifier*.
- Predict label based on node feature vector fv and summary Zv of labels of v’s neighbors. This is called *relational classifier*.

**Example** Web Page Classification

Predict the topic of the webpage with nodes as webpages, edges as hyperlinks and node features as webpage descriptions.

### Summary Note

Relational classification
- Iteratively update probabilities of node belonging to a label class based on its neighbors.

Iterative classification
- Improve over collective classification to handle attribute/feature information.
- Classify node v based on its features as well as labels of neighbors.

### 3. Collective Classification (C&S)

**Intuition:** Simultaneous classification of interlinked nodes using correlations;

**Markov Assumption:** The label Y of one node v depends on the labels of its neighbors Nvs:
- P(Yv) = P(Yv | Nv)

### Collective Classification involves 3 steps:
- **Local Classifier:** Predict labels based on *node features*;
  - Base predictor can be simple: Linear model/Multi-Layer-Perceptron(MLP) over node features.
- **Relational Classifier:** Learns a classifier to label one node based on the labels/attributes of its neighbors;
  - Use graph structure to post-process the predictions to make them more accurate.
- **Collective Inference:** Apply relational classifier to each node iteratively; Iterate until the inconsistency between neighboring labels is minimized;
  - Correct and smooth to post-process soft predictions.
  
**C&S:**

Key idea is that we expect errors in the base prediction to be positively correlated along edges in the graph.
- In other words, an error at node v increases the chance of a similar error at neighbors of u. 
  - The degree of the errors of the soft labels are biased: Diffuse training errors along the edges.
  - The predicted soft labels may not be smooth over the graph.




**Message Passing**

<img width="400" img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/belief-prop.PNG" alt="Belief Propagation" />

**Loopy Belief Propagation**




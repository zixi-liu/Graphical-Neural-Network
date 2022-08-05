## Frequent Subgraph Mining with GNNs

Subgraphs are the building blocks of networks: they have the power to characterize and discriminate networks.

Def 1. Node-induced subgraph (focus on functional groups)

Def 2. Edge-induced subgraph (focus on edges representing logical relations)

**Graph Isomorphism**
<img width="878" alt="image" src="https://user-images.githubusercontent.com/46979228/170879680-451c7153-6f2e-42da-8dd6-da0c019d9aa6.png">

**Network Motifs**

- Pattern: small (node-induced) subgraph
- Recurring: found many times, i.e., with high frequency
- Significant: more frequent than expected

**Subgraph Frequency**
- Graph-level subgraph frequency 
- Node-level subgraph frequency

**Defining Motif Significance**
- [Key Idea] Subgraphs that occur in a real network much more often than in a random network have functional significance.
- [Baseline] Random Graph: Create n nodes, for each pair of nodes (u, v) flip a biased coin with bias p.
- [Method 1] We can compare the real network $G^{real}$ and a “random” graph $Gr^{andom}$ which has the same degree sequence as $G^{real}$.
- [Method 2] We select a pair of edges at random and exchange the endpoints, and the result is a randomly rewired graph with same node degrees, but randomly rewired edges.

An Example of Method 1:
![image](https://user-images.githubusercontent.com/46979228/183100586-93bb6578-d43f-4400-8873-4c61fffbfc93.png)

[Intuition] Motifs are overrepresented in a network when compared to random graphs.

[Procedure for 
- Step 1: Count motifs in the given graph 
- Step 2: Generate random graphs with similar statistics (e.g. number of nodes, edges, degree sequence), and count motifs in the random graphs
- Step 3: Use statistical measures to evaluate how significant is each motif
  - Use Z-score $Z_i = (N_i^{real} - \bar{N_i}^{random})/std(N_i^{random})$
  - Negative z-score indicate under-representation
  - Positive z-score indicate over-representation 
  
  
**Subgraph Matching**

Use GNN to predict subgraph isomorphism.
- [Intuition] Exploit the geometric shape of embedding space to capture the properties of subgraph isomorphism.

Architecture:

![image](https://user-images.githubusercontent.com/46979228/183103956-b4efe99f-f013-43e0-aa71-6e3c8d065c5a.png)


- Step 1: Use GNN to obtain representations of u and v. i.e. compute embeddings for u and v using GNN.
- Step 2: Use embedding to decide if node u’s neighborhood is isomorphic to node v’s neighborhood.

As shown in the architecture, we 1) decompose graph $G^{Target}$ into neighborhoods.
- For each node in $G^{Target}$:
  - Obtain a k-hop neighborhood around the anchor
  - Can be performed using breadth-first search (BFS)
  - The depth k is a hyper-parameter (e.g. 3) (Larger depth results in more expensive model)
- Same procedure applies to $G^{Query}$, to obtain the neighborhoods.
- Embed the neighborhoods using a GNN by computing the embeddings for the anchor nodes in their respective neighborhoods.

Then, 2) we map graph A to a point $Z_A$ into a high dimensional (e.g. 64-dim) embedding space, such that $Z_A$ is non-negative in all dimensions.
- Subgraph is to the lower-left of its supergraph (in 2D space).

3) Design loss function should we use, so that the learned order embedding reflects the subgraph relationship.

![image](https://user-images.githubusercontent.com/46979228/183107255-14b7fa6f-85b2-46b5-8e15-6192c13d5d30.png)

**Training a Subgraph Mining GNN**
- For positive examples: Minimize $E(G_T, G_Q)$ when $G_Q$ is a subgraph of $G_T$.
- For negative examples: Minimize $max(0, \alpha − E(G_T, G_Q))$

Training Sample Construction
- Step 1: Get $G_T$ by choosing a random anchor v and taking all nodes in G within distance K from v to be in $G_T$.
- Step 2: Get Positive examples using BFS sampling.
- Step 3: Get negative examples ($G_Q$ not subgraph of $G_T$): “corrupt” $G_Q$ by adding/removing nodes/edges so it’s no longer a subgraph.

An Example of BFS Sampling:

![image](https://user-images.githubusercontent.com/46979228/183109587-07b4dd50-b5af-4da6-8071-036196ef0638.png)


**Mining Frequent Subgraphs**

[Goal] Identify, among all possible graphs of k nodes, the r graphs with the highest frequency in $G_T$.

Representation Leaning
- Step 1: Counting #(occurrences of each subgraph type)
  -  Solution: Use GNN to “predict” the frequency of the subgraph.
- Step 2: Enumerating all size-k connected subgraphs
  - Solution: Don’t enumerate subgraphs but construct a size-k subgraph incrementally.

Overview:

![image](https://user-images.githubusercontent.com/46979228/183111421-fd9613b8-3f59-476b-81ce-ac584d959f22.png)

[Iteratively] Grow a motif by iteratively choosing a neighbor in $G_T$ of a node in S and add that node to S.
We grow the motif S to find larger frequent motifs.

![image](https://user-images.githubusercontent.com/46979228/183112304-86772277-56ea-41ea-9d9a-936cd9e76d7b.png)


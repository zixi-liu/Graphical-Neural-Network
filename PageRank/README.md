# Link Analysis 

Link Analysis allow us to measure importance of nodes in a graph using the link structure of the web.

## Methods

- **PageRank**
- **Personalized PageRank**
- **Random Walk with Restarts**

## PageRank

### The "Flow" Model

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/page-rank.PNG" alt="Page Rank" width = "200px" />

**Stochastic adjacency matrix**

- Let page j has dj out-links and j -> i, then Mij = 1/dj. M is a column stochatic matrix where columns sum to 1.

### Problems When Solving PageRank

- **Dead Ends** (have no out-links)
- **Spider Traps** (all out-links are within the group)

**Solution for Spider Traps:** At each time step, the random surfer has two options
-  With prob. b, follow a link at random;
-  With prob. 1-b, jump to a random page;
-  Common values for b are in the range 0.8 to 0.9;

Surfer will teleport out of spider trap within a few time steps.

**Solution for Dead Ends:** : Follow random teleport links with total probability 1.0 from dead-ends.

### Summary

- PageRank solves for 𝒓 = 𝑮𝒓 and can be efficiently computed by power iteration of the stochastic adjacency matrix (𝑮);
- Adding random uniform teleportation solves issues of dead-ends and spider-traps;

## Random Walk with Restarts

### Bipartite Graph

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/bipartite-graph.PNG" alt="Bipartite Graph" width = "800px" />

- Teleports to the starting node S.

- Given a set of QUERY NODES Q, simulate a random walk and get number of visits by random walks starting at Q:

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/random-walk-restarts.PNG" alt="Bipartite Graph" width = "800px" />

**Pseudo Code**

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/pseudo-code.PNG" alt="Pseudo Code"  />


## Personalized Page Rank

- Ranks proximity of nodes to the teleport nodes S.


## Summary

### PageRank:
- Teleports to any node
- Nodes can have the same probability of the surfer landing:

          𝑺 = [0.1,0.1,0.1, 0.1,0.1,0.1, 0.1,0.1,0.1, 0.1]
   
### Topic-Specific PageRank aka Personalized PageRank:
- Teleports to a specific set of nodes
- Nodes can have different probabilities of the surfer landing there:

          𝑺 = [0.1,0, 0,0.2, 0, 0,0.5,0,0, 0.2]
          
### Random Walk with Restarts:
- Topic-Specific PageRank where teleport is always to the same node:

         𝑺 = [0,0, 0,0, 𝟏, 0, 0, 0, 0, 0,0]

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

- **Dead Ends**
- **Spider Traps**

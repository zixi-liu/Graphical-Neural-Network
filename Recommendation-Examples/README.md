# Personalized Product Recommendations


[Cypher Cheatsheet](https://neo4j.com/docs/cypher-refcard/current/?ref=browser-guide)

**Example of Neo4j Movie Recommendations**

```
CALL db.schema.visualization()
```

<img src="https://github.com/zixi-liu/Graphical-Neural-Network/blob/main/Img/recommendation-movie.png" alt="recommendation"/>

## Content-Based Filtering

Recommend items that are similar to those that a user is viewing, rated highly or purchased previously.

## Collaborative Filtering

Use the preferences, ratings and actions of other users in the network to find items to recommend.

# Neo4j Graph Data Science (GDS) 

The Neo4j Graph Data Science (GDS) library provides extensive analytical capabilities centered around graph algorithms. The library includes algorithms for community detection, centrality, node similarity, path finding, and link prediction, as well as graph catalog procedures designed to support data science workflows and machine learning tasks over your graphs. 

Neo4j Graph Data Science library supports the random walk algorithm, which makes it very easy for us to implement the node2vec algorithm. 


[Graph Embeddings](https://towardsdatascience.com/node-embeddings-node2vec-with-neo4j-5152d3472d8e)

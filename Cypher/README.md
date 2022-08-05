This repository is dedicated to Neo4j 😎

### PageRank

PageRank is defined in the original Google paper as follows: $PR(A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))$ where,
we assume that a page A has pages $T1$ to $Tn$ which point to it (i.e., are citations).
d is a damping factor which is set between 0 and 1. It is usually set to 0.85.
$C(A)$ is defined as the number of links going out of page A.

**A Fraud Detection Example using GDS 2.1.2 PageRank**
```
// Data Curation
CREATE
  (Adams:Accounts {name:'Adams'}),
  (Lily:Accounts {name:'Lily'}),
  (Sam:Accounts {name:'Sam'}),
  (Peter:Accounts {name:'Peter'}),
  (Jason:Accounts {name:'Jason'}),
  (Kim:Accounts {name:'Kim'}),
  (Tyler:Accounts {name:'Tyler'}),
  (Chip:Accounts {name:'Chip'}),

  (Adams)-[:SHARED_DEVICEID {weight: 2}]->(Lily),
  (Adams)-[:SHARED_DEVICEID {weight: 3}]->(Peter),
  (Adams)-[:SHARED_DEVICEID {weight: 1}]->(Sam),
  (Lily)-[:SHARED_DEVICEID {weight: 1}]->(Tyler),
  (Sam)-[:SHARED_DEVICEID {weight: 1}]->(Chip),
  (Sam)-[:SHARED_DEVICEID {weight: 2}]->(Tyler),
  (Peter)-[:SHARED_DEVICEID {weight: 6}]->(Tyler),
  (Jason)-[:SHARED_DEVICEID {weight: 1}]->(Chip),
  (Kim)-[:SHARED_DEVICEID {weight: 1}]->(Jason),
  (Kim)-[:SHARED_DEVICEID {weight: 2}]->(Chip);
  
// Graph Projection
CALL gds.graph.project(
  'PageRankGraph',
  'Accounts',
  'SHARED_DEVICEID',
  {
    relationshipProperties: 'weight'
  }
)

// Memory Estimation
CALL gds.pageRank.write.estimate('PageRankGraph', {
  writeProperty: 'pageRank',
  maxIterations: 20,
  dampingFactor: 0.85
})
YIELD nodeCount, relationshipCount, bytesMin, bytesMax, requiredMemory

// Run PageRank
CALL gds.pageRank.stream('PageRankGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC, name ASC
```

Outputs PageRank Score:

<img src="https://user-images.githubusercontent.com/46979228/183001454-21cf1a50-b8d0-456f-970d-a5cd84e7a019.png" alt="GNN" width = "600"/>


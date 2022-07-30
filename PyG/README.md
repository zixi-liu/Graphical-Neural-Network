## Quick Start on Pytorch-Geometrics

![image](https://user-images.githubusercontent.com/46979228/181924617-1a36612e-8bc8-4dcc-9f14-e0f927d871e5.png)


[**PyG Documentation**](https://pytorch-geometric.readthedocs.io/en/latest/)

### What is PyG?

PyG (PyTorch Geometric) is a library built upon PyTorch to easily write and train Graph Neural Networks (GNNs) for a wide range of applications related to structured data.

### How to create your own PyG graph?

Let's suppose we have our own nodes, edges, and labels data, here're the steps to create our own pyg format graph.

- nodes.csv
- edges.csv
- labels.csv

**nodes**
| node_id  | node_type | node_attributes | 
| :---: | :---: | :---: | 
| 14  | 'item' | '0.00250581:0.00000000:0.00543360:...:0.00378898' |

- node_id [int], 
- node_type [string], 
- node_atts [string] (notice that node_atts are 256-dimensional feature vector strings with delimiter ":")

**edges**
| source_node_id  | target_node_id | source_node_type | target_node_type | edge_type | 
| :---: | :---: | :---: | :---: | :---: |
| 23  | 7261518 | 'user' | 'item' | 'has_transaction' |

- source_node_id [int], 
- target_node_id [int], 
- source_node_type [string], 
- target_node_type [string], 
- edge_type [string]

**labels**
| node_id  | label |
| :---: | :---: |
| 14  | 0 |

- item_id [int], 
- label [int]

**Creating Heterogeneous Graphs**

Most graphs in the area of recommendation, such as social graphs, are heterogeneous, as they store information about different types of entities and their different types of relations.

Looking at an example on PyG official documentation, for each node type, we need to define a node index and a node attribute. Similarly, for each edge type, we also need to define a edge index and a edge attribute.

```
from torch_geometric.data import HeteroData

data = HeteroData()

data['paper'].x = ... # [num_papers, num_features_paper]
data['author'].x = ... # [num_authors, num_features_author]
data['institution'].x = ... # [num_institutions, num_features_institution]
data['field_of_study'].x = ... # [num_field, num_features_field]

data['paper', 'cites', 'paper'].edge_index = ... # [2, num_edges_cites]
data['author', 'writes', 'paper'].edge_index = ... # [2, num_edges_writes]
data['author', 'affiliated_with', 'institution'].edge_index = ... # [2, num_edges_affiliated]
data['paper', 'has_topic', 'field_of_study'].edge_index = ... # [2, num_edges_topic]

data['paper', 'cites', 'paper'].edge_attr = ... # [num_edges_cites, num_features_cites]
data['author', 'writes', 'paper'].edge_attr = ... # [num_edges_writes, num_features_writes]
data['author', 'affiliated_with', 'institution'].edge_attr = ... # [num_edges_affiliated, num_features_affiliated]
data['paper', 'has_topic', 'field_of_study'].edge_attr = ... # [num_edges_topic, num_features_topic]
```

To start with, we can first create a data object of type torch_geometric.data.HeteroData:

```
from torch_geometric.data import HeteroData

data = HeteroData()
```

It's important to note that node or edge tensors will be automatically created upon first access and indexed by string keys. So if our nodes file contains node_id already, we can add extra handling to map node_id to a consecutive value in the range { 0, ..., num_rows - 1 }. For example, in *format_pyg.py*, the following chunk of code creates a dictionary node mapping to re-define node index when loading *node.csv*.


```
  line = rf.readline()
  if line is None or len(line) == 0:
       break
  info = line.strip().split(",")

  node_id = int(info[0])
  node_type = info[1].strip()

  node_maps.setdefault(node_type, {})
  node_id_v2 = len(node_maps[node_type])
  node_maps[node_type][node_id] = node_id_v2
```

Then we load node attributes/embeddings and labels sequentially. In order to create a pyG graph, we also need to load the *edge.csv* to connect the source node and the target node. 

```
for edge_type in edges:
        source_type = edges[edge_type]['source_type']
        dest_type = edges[edge_type]['dest_type']
        source = torch.tensor(edges[edge_type]['source'], dtype=torch.long)
        dest = torch.tensor(edges[edge_type]['dest'], dtype=torch.long)
        graph[(source_type, edge_type, dest_type)].edge_index = torch.vstack([source, dest])

for edge_type in [('b', 'A_1', 'item'),
                  ('f', 'B', 'item'),
                  ('a', 'G_1', 'f'),
                  ('f', 'G', 'a'),
                  ('a', 'H_1', 'e'),
                  ('f', 'C', 'd'),
                  ('f', 'D', 'c'),
                  ('c', 'D_1', 'f'),
                  ('f', 'F', 'e'),
                  ('item', 'B_1', 'f'),
                  ('item', 'A', 'b'),
                  ('e', 'F_1', 'f'),
                  ('e', 'H', 'a'),
                  ('d', 'C_1', 'f')]:
        temp = graph[edge_type].edge_index
        del graph[edge_type]
        graph[edge_type].edge_index = temp
```

Finally, we can save our PyG graph in pickle format.

```
 torch.save(graph, pyg_file + ".pt")
```

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

**Creating Heterogeneous Graphs**

Most graphs in the area of recommendation, such as social graphs, are heterogeneous, as they store information about different types of entities and their different types of relations.

We can create a data object of type torch_geometric.data.HeteroData:

```
from torch_geometric.data import HeteroData

data = HeteroData()
```

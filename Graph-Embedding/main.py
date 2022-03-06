from deepwalk import DeepWalk
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.manifold import TSNE
import numpy as np


# Utils
def read_node_label(filename, skip_head=False):
    fin = open(filename, 'r')
    X = []
    Y = []
    while 1:
        if skip_head:
            fin.readline()
        l = fin.readline()
        if l == '':
            break
        vec = l.strip().split(' ')
        X.append(vec[0])
        Y.append(vec[1:])
    fin.close()
    return X, Y


def plot_embeddings(embeddings,):
    X, Y = read_node_label('./example-data/wiki/wiki_labels.txt')

    emb_list = []
    for k in X:
        emb_list.append(embeddings[k])
    emb_list = np.array(emb_list)

    model = TSNE(n_components=2)
    node_pos = model.fit_transform(emb_list)

    color_idx = {}
    for i in range(len(X)):
        color_idx.setdefault(Y[i][0], [])
        color_idx[Y[i][0]].append(i)

    for c, idx in color_idx.items():
        plt.scatter(node_pos[idx, 0], node_pos[idx, 1], label=c)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    G = nx.read_edgelist('./example-data/wiki/wiki_edgelist.txt', create_using=nx.DiGraph(), nodetype=None,
                         data=[('weight', int)])  # Read graph

    model = DeepWalk(G, walk_length=10, num_walks=80, workers=1)  # init model
    model.train(window_size=5, iter=3)  # train model
    embeddings = model.get_embeddings()  # get embedding vectors
    plot_embeddings(embeddings)


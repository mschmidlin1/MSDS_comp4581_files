from collections import defaultdict
import numpy as np
import os

def loadGraph(edgeFilename):
    """
    Loads edges from edgeFilename.
    """
    with open(edgeFilename) as f:
        lines = f.readlines()
    edges = []
    d = defaultdict(list)
    for line in lines:
        verts = line.split()
        if len(verts)!=2:
            raise ValueError("Edge cannot have more or less than vertices.")
        verts = int(verts[0]), int(verts[1])
        d[verts[0]].append(verts[1])
        d[verts[1]].append(verts[0])
        edges.append(verts)
    return (edges, d)

def unique_tuples(tuples):
    all = []
    for tuple in tuples:
        all.append(tuple[0])
        all.append(tuple[1])
    return set(all)

def BFS(G, s):
    q = MyQueue()
    q.enqueue(s)
    visited = set()
    vertex_distances = {}
    vertex_distances[s] = 0
    while not q.empty():
        vertex = q.dequeue()
        visited.add(vertex)
        for i in G[vertex]:
            if i not in visited and i not in q.queue:
                q.enqueue(i)
                vertex_distances[i] = vertex_distances[vertex] + 1
    return sorted(vertex_distances.items())

def distanceDistribution(G):
    unique_verts = set(G.keys())
    dists=np.array([], dtype=int)
    for s in unique_verts:
        verts_dists = BFS(G, s)
        # verts = np.array(verts_dists)[:, 0] 
        dists = np.append(dists, np.array([v[1] for v in verts_dists]))
    uniques = np.unique(dists, return_counts=True)[0]
    counts = np.unique(dists, return_counts=True)[1]
    percent_frequencies = counts[1:]*100/np.sum(counts)
    freq_dict = { u:p for u, p in zip(uniques[1:], percent_frequencies) }
    return freq_dict


class MyQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
    def dequeue(self):
        return self.queue.pop(0)
    def empty(self):
        return not bool(len(self.queue))


def main():
    edges, G = loadGraph(os.path.join(os.path.dirname(__file__), "edges.txt"))
    distance_dict = distanceDistribution(G)
    print(distance_dict)




if __name__ == "__main__":
    main()



#{1: 1.081728463156421, 2: 16.649587786719984, 3: 24.408292973662768, 4: 35.930685962889314, 5: 15.724195898604599, 6: 4.151243621778524, 7: 1.933757893222438, 8: 0.0957487963511985}
# ~97% of people are 6 or less degrees of separation away
"""
Single Source Shortest Path
Only difference with Prim is there we consider only weight of edges
Here we consider weight of vertex to which ech is connected and edge weight for minimization

The principle behind Dijkstra's algorithm is that if s...x...t is the shortest path from s to t,
then s...x had better be the shortest path from s to x

NOTE:
- Add cnstant weight to each edge may change shortest path
- Time Complexity: O(n^2)
- Improved version: O(mlgn) - using a heap of vertices ordered by distance
                            - faster on sparse graphs
                            - updating the distance to each vertex in O(lgn) time
                            - distance is heap
- O(nlgn+m) - fibonacci heaps, since they permit one to do a decrease key operation in
  O(1) amortized time
- All Pairs Shortest Path: run dijkstra n times - O(n^3)
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v, w):
        self.g[u].append((v, w))
        #self.g[v].append((u, w))

    def neighbors(self, u):
        return self.g[u]

    def vertices(self):
        return self.g.keys()

    def dijkstra(self, start):
        parent = dict()
        frontier = set()
        distance = dict()

        u = start
        distance[u] = 0

        while u not in frontier:
            frontier.add(u)

            for v, wt in self.neighbors(u):
                if v in frontier: continue
                if distance.get(v, float('inf')) > distance[u] + wt:
                    distance[v] = distance[u] + wt
                    parent[v] = u

            u, minWt = start, float('inf')
            for n in self.vertices():
                if n not in frontier and distance[n] < minWt:
                    u, minWt = n, distance[n]
        return distance, parent
                    
g = Graph()
g.edge('s', 'v', 1)
g.edge('s', 'w', 4)
g.edge('v', 'w', 2)
g.edge('v', 't', 6)
g.edge('w', 't', 3)
print(g.dijkstra('s'))




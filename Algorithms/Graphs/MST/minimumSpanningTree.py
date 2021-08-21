"""
Minimum Spanning Tree: [Subset of edges]
    -A tree is a connected graph with no cycles
    - A spanning tree is a subgraph of G which has same set of vertices of G and is a tree
    - A minimum spanning tree of a weighted graph G is the spanning tree of G whose edges sum to minimum weight
    - Tree has 1 MST
    - Complete graph has n! MST (atleast n^(n-1/2) MST)
    Applications:
    - Data clustering problems narrow to MST
    - Do a MST and remove the longest edge

Prim's algorithm:
    - If G is connected, every vertex will appear in minimum spanning tree.
    - If not, we can talk about minimum spanning forest
    - Prim's algorithm start from one vertex and grows the rest of the tree
      an edge at a time
    - Greedy Algorithm: Cheapest edge which can grow tree by one vertex
                        without creating a cycle
    - A frontier is maintained and best edge among all the edges across frontier are considered
    - Two ways of proving the correctness - induction or contradiction
    - Lets proof this by contradiction:
      > Suppose Prim's algorithm doesn't always give the minimum cost spanning tree on some graph
      > If so there is a graph on which it fails
      > If so, there must be a first edge (x, y) Prim adds such that the partial tree V' cannot be
        extended into a minimum spanning tree
      > There must be an edge (v1, v2) which should be selected to keep the tree subtree of MST
      > But why would Prim select an edge (x, y) over (v1, v2) if (v1, v2) is less
      > Hence choice of (x, y) is not fatal, therfore by contradiction Prim's algorithm must be generating MST.

Time complexity:
    - select an arbitrary vertex to start
    - while (there are non-tree vertices)
          select minimum weight edge between tree and fringe
          add the selected edge and vertex  to the tree
    - This can be done in O(nm) time, by doing a DFS or BFS to loop through all the edges,
      with a constant time test per edge and a total of n iterations
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, w))

    def neighbors(self, u):
        return self.g[u]

    def vertices(self):
        return self.g.keys()

    def prim(self, start):
        """
        Idea:
        - Lets start with a vertex s and maintain a frontier
        - For each vertex see all edges in its neighbors, and find min
        - Move the vertex in discovered and the edge in spanning tree path
        
        Data Structures:
        - discovered: a set keeping track of discovered vertices starting with a vertex s
        - 

        """
    
        def minEdge(u):
            minEdgeWt, minEdgeV = float('inf'), None
            for v, wt in self.neighbors(u):
                if v not in frontier:
                    if wt < minEdgeWt:
                        minEdgeWt, minEdgeV = wt, v
            return minEdgeWt, minEdgeV
        
        frontier, edges, weight = set(), list(), 0
        frontier.add(start)

        while True:
            # while there is an edge(u, v) with u in X and v not in X
            # All vertices have moved from non tree vertices to tree vertices
            if len(frontier) == len(self.g): break

            minWt, u, v = float('inf'), None, None # Non Tree element
            for tv in frontier: # Tree vertex
                wt, ntv = minEdge(tv)
                if wt < minWt:
                    minWt, u, v = wt, tv, ntv

            frontier.add(v)
            weight += minWt
            edges.append((u, v))
    
        return "Edges: {}, Weight: {}".format(edges, weight)

    def primv2(self, start):
        """
        - See through all the vertices of graph if they are undiscovered
        - Initialize all of them for parent set as None and distance set as inf
        - For each vertex if undiscovered, check its neighbors and get the min weight edge
          and update distance and parent for v

        - Keep track of cheapest edge linking every nontree vertex in the tree
        - The cheapest such edge over all remaining non-tree vertices gets added in each iteration
        - Update cost of reaching non-tree vertices after each iteration
        - Most recently inserted vertex is the only chnage in the tree, all possible edge-weight updates
          must come from its outgoing edges
        - Time Complexity: 
          > Avoid testing all m edges on each pass
          > Only considers <= n cheapest known edges represented in parent array and <= n edges out of the
            new tree vertex v to update parent
          > We test an edge connects tree and non-tree vertex in constant time O(n^2)
        """
        frontier = set()
        N = len(self.vertices())
        parent = dict() 
        distance = dict()

        u, distance[u] = start, 0

        while u not in frontier:
            frontier.add(u)
            # For each new vertex added in frontier
            # Update its distance with its neighbors
            # and add vertex as parent
            # This first part considers the consequences of adding u into tree
            for v, wt in self.neighbors(u):
                if v in frontier: continue
                if wt < distance.get(v, float('inf')):
                    distance[v] = wt
                    parent[v] = u

            # find min distance with all the nontree elements
            u, minDist = start, float('inf')
            for i in self.vertices():
                if i not in frontier and distance.get(i, float('inf')) < minDist:
                    minDist, u = distance[i], i

        edges = list()
        for k, v in parent.items():
            # v is parent, k is child
            edges.append((v, k))
        return edges



g = Graph()
g.edge('a', 'b', 1)
g.edge('a', 'c', 4)
g.edge('a', 'd', 3)
g.edge('b', 'd', 2)
g.edge('c', 'd', 5)
#print(g.prim('b'))
print(g.primv2('b'))

Graph Theory
------------
Mathematical theory of the properties and applications of graphs(networks)
G(V, E)

Types of graph
--------------
> Undirected: Graph in which edges have no orientation. {u, v} is same as {v, u} - set of unordered pairs
> Directed: Graph in which edges have orientations.(Digraph) - (u, v) - set of ordered pairs
> Weighted: Edges having weights representing an arbitrary value (cost, distance, quantity etc.) (u, v, w)

Special Graphs
--------------
Trees:
- A tree is an undirected graph with no cycles
- Connected graph with N nodes and N-1 edges

Rooted Trees:
- A rooted tree is a tree with a designated root node where every edge either points away from or towards the root node
- When edges point away from the root: arborescence (out tree)
- When edges point towards the root: anti-arborscence (in tree)

Directed Acyclic Graphs(DAGs):
- DAGs are directed graphs with no cycles
- These graphs play important role in representing structures with dependencies
- All out trees are DAGs, but not all DAGs are out trees

Bipartite Graph:
- A bipartite graph is one whose vertices could be split into two independent groups
- Every edge connects between U and V
- Graph is two colourable
- No odd length cycle

Complete Graph:
- Worst case graphs
- Where there is a unique edge between every pair of nodes
- A complete graph with n vertices is represented as kn

Representations
---------------
Adjacency Matrix:
- Cell m[i][j] represents the edge weight of edge going from node i to node j
- Pros:
  > Space efficient for dense graphs
  > Edge weight lookup is O(1)
- Cons:
  > Requires O(V^2) space
  > Iterating over all edges takes O(V^2) time

Adjacency list:
--------------
- Represented as a map from nodes to list of edges
- Array adj of |V| linked lists
- For each vertex u element of V adj(u) stores neighbors
- A -> [(B, 4), (C, 1)]
- Sometimes we don't want to maintain adjacency list, but create it on the fly as 
  storing all the states might not be possible (Rubic's cube), hence we have function call
  v.neighbors(), generating neighbors and returning it on the fly
- Space: O(V+E): Linear in size of graph
- Pros:
  > Space efficient for representing sparse graphs
  > Iterating over all the edges is efficient
- Cons:
  > Edge wight lookup is O(E)

Edge List:
---------
- Represented as an unordered list of edges
- [(u, v, w), ...] where (u, v, w) represent the cost from node u to node v is w
- Pros:
  > Space efficient for sparse graphs
  > Iterating over all the edges is efficient
- Cons:
  > Edge weight lookup is O(E)

Applications
------------
 > Web Crawling
 > Social Networking
 > Network broadcast
 > Garbage collection
 > Model checking - states model
 > Checking mathematical conjecture 
 > Solving puzzles and games

Common Graph Theory Problems
----------------------------
Shortest Path Problem:
 > BFS (unweighed graph)
 > Dijkstra's
 > Bellman Ford
 > Floyd-Warshall
 > A*

Connectivity:
 > Does there exist a path between node A and B?
 > Solution: Use union find data structure or any other search algorithm (DFS)

Negative Cycles:
 > Does my weighed digraph have any negative cycles? If so, where?
 > Negative cycles are trap
 > Bellman Ford and Floyd Warshall

Strongly Connected Components (SCCs):
 > SCCs can be thought of as self-contained cycles within a directed graph
   where every vertex in a given cycle can reach every other vertex in same cycle 
 > Tarjan's and Kosaraju's

Travelling Salesman Problem:
 > Given a list of cities and the distances between each pair of cities,
   what is the shortest possible route that visits each city exactly once
   and return to the origin city
 > Held-karp, branch and bound and many approximation algorithms

Bridges/Cutedge:
 > Is any edge in a graph whose removal increases the number of connected components
 > Bridges are important in graph theory because they often hint at weakpoints, bottlenecks or vulnerabilities in a graph.

Articulation Points/Cut vertex:
 > Is any node in a graph whose removal increases the number of connected components

Minimum Spanning Tree:
 > Subset of the edges of a connected, edge weighted graph that connects all the vertices together,
   without any cycles and with the minimum possible total weight
 > Kruskal's, Prim's and Boruvka's
 > All MST on a graph are not unique

Network flow:
 > With an infinite input source how much "flow" can be pushed through the network?
 > Ford-Fulkerson, Edmonds-Karp, Dinic's 

NOTES:
- Cycles could not be identified always from one point, but we need to consider all points

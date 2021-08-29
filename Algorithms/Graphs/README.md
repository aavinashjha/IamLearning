Graph Theory
------------
Mathematical theory of the properties and applications of graphs(networks)
G(V, E)

Types of graph
--------------
> Undirected: Graph in which edges have no orientation. {u, v} is same as {v, u} - set of unordered pairs
              If represented in adjacency matrix half of space could be used in case of undirected graph
> Directed: Graph in which edges have orientations.(Digraph) - (u, v) - set of ordered pairs
> Weighted: Edges having weights representing an arbitrary value (cost, distance, quantity etc.) (u, v, w)
> Simple/Non-Simple: Certain types of edges complicate the task of working with graphs.
                     A self loop is an edge (x, x) involving only one vertex
                     An edge (x, y) is a multi-edge if it occurs more than once in the graph
                     Any graph which avoids these strcurctures is called simple
> Sparse/Dense: N vertices then O(N) edges is sparse, O(N^2) edges is dense
> Labeled/Unlabeled: Each vertex is assigned a unique name or identifier to distinguish it from all other vertices
                     An important graph problem is isomorphism testing, determining whether the topological strcuture
                     of the two graphs are in fact identical if we ignore the labels 

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

Planar Graph:
- Can it be drawn on paper without crossing the edges
- Some algorithms run faster on planar graphs
- Max Cut: Splitting the graph into two parts and getting maximum number of edges that connect the two parts
	   NP Complete problem but polynomial time on planar graphs
 
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
- Represents vertex adjacent to a vertex
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
  > Actually it is degree 
- Convert from adjacency matrix to adjacency list -> O(N^2)
- Adjacency list will have twice number of elements as number of edges in undirected graph
  as one edge is represented twice

Incident Matrix
---------------
    M
N -----

N row * M columns
An incidence matrix has a row for each vertex and a column for each edge,
such that M[i, j] = 1 if vertex i is part of edge j, otherwise M[i, j] = 0
- Convert from adjacency list to incedence matrix O(NM)
- Convert from incidence matrix to adjacency list O(NM)

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
 > Social Networking: Sparse Graph as there are few friends of each person
 > Network broadcast
 > Garbage collection
 > Model checking - states model
 > Checking mathematical conjecture 
 > Solving puzzles and games
 > Road Networks (Weight: cost of toll, distance, time taken)
                 Multiple lanes (service lane) could represent multi-edge
		 Sparse graphs
 > Electronic circuit: Sparse graphs
 > Callgraph: Testing if every function is called
              Piece of code is never used (dead code)
              This is directed graph
	      Unweighted
	      With recursion Non-Simple
> Cell networks: Dense graph (Any person can call anyone)
              

Flavors of graph
-----------------
- The first step in any graph problem is determining which flavor of graph you are dealing with
- Learning to talk the talk is an important part of walking the walk
- The flavor of graph has big impact on which algorithms are appropriate and efficient

Traversing the graph
--------------------
- Traverse every edge and vertex
- For efficiency, Visit each edge atmost twice
- For correctness, do traversal in a systematic way so that we don't miss anything

Marking the vertices
- The key idea is we must mark each vertex when we first visit it, and keep track
  of what have not yet completely explored 
Each vertex will be in one of the three states:
- undiscovered: vertex is in initial state
- discovered: the vertex after we have encountered it, but before we have checked out all its incident edges
- processed: the vertex after we have visited all its incident edges 

A vertex cannot be processed before we discover it, so the course of traversal of the state of each vertex progresses
from undiscovered to discovered to processed
 
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
- Complement of a dense graph is sparse graph

Edges are upperbounded by E = O(V^2)
BFS space complexity is proportional to breadth of tree
- Moving down a level doubles number of nodes
DFS space complexity depends on height of tree
- O(lgN) in case of balanced tree
- DFS is superior in case of balance search tree

Sometimes given a problem, like finding a cycle in graph is so intuitive (just by looking at it) that
we are not able to think that how we would implement it or there is a method which will solve that problem
- If adjacency list is given and human has to solve the problem, it would be done by converting to picture

e < n^2 n(n-1)/2 [undirected graph]
- adjacency list takes less space

There is always a tradeoff between data structures and algorithms
The more fancy data structures you keep, less work algorithm has to do.
More preprocessing you do less work need to be done at runtime. [More you sweat in peace, less you bleed in war :)]

BFS also does connected component.
We can do everything with BFS if we want entry time, algorithms dependent on exit time require DFS

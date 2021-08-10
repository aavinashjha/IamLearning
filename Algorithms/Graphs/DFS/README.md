Depth First Search
------------------
- If there is a vertex from v which is unreachable from s, then shortest path is infinity (with BFS)
- DFS helps in exploring the whole graph and not only the part reachable from s 
- Recursively explore graph, backtracking as necessary
- Careful not to repeat

- DFS varies from BFS in 2 ways:
  > Use stack instead of queue
  > Postpone checking if the vertex is explored until we remove it from stack
    In BFS as soon as we encounter a node we check if it is explored earlier or not

- In BFS as soon as we encounter neighbors, we know that those are to be considered
  So we could check if they are not visited and add them
  But in DFS, we want to reach the farthest node possible and hence we mark is explored only when we are removing it
  and not adding it as we have to go more in depth

Edge Classification
-------------------
- DFS Trees: Obtained by DFS traversal
             After building the DFS tree, we have edges classified as tree edges, forward edges, backward edges and cross edges
- Back edge: Edge that is connecting one of the vertices to its parent in the DFS tree: node -> ancestor in tree
- Forward edge: Edge connecting a parent to one of the non direct children in DFS tree: node -> descendant in tree
- Tree edge: Main edges visited to make DFS tree: Visit new vertex via edges (Parent structure)
- Cross edge: Edge connecting vertex from one of the DFS trees to another DFS tree: Between two non-ancestor related subtrees
	      (x, y): x is neither ancestor not descedant of y

- Each back edge introduces a cycle
- Removal of back edges in graph make it DAG
- Multiple DFS runs leads to multiple DFS trees (If some node are missed by previous DFS runs)

- Running Time:
  > visit each vertex in outer loop O(V)
  > Sum Adj(v) = O(E)
  > O(V+E)

- Only tree edges and backward edges can exist in undirected graph

Cycle Detection
---------------
- If DFS has a back edge, G has a cycle
  Ancestor ----> Tree Edges ----> Descendant
   <------------- Back Edge -----------
  This indicates a directed cycle
- G has a cycle, then DFS has a back edge
  Assume vo is the first vertex in the cycle visited by DFS than edge connecting vk to v0 is backedge
- v1 is visited first before we finish visiting v0
- vi is visited before we finish vi-1 
- start v0
  start vk
  finish vk
  finish v0
- Similar to balanced parenthesis
- (vk, v0) is a backedge as v0 is still under processing and we have an edge to it (ancestor)

Job Scheduling
--------------
- Given Directed Acyclic Graph order vertices so that all edges point from lower order to higher order

Topological Sort
----------------
- Left to Right
- Left most vertex has indegree 0
- Precedence Constraints: We cannot start some tasks until others are completed
- G = (V, E) is a directed graph
- A topological ordering of G is an assignment f(u) of every vertex to a different number
  such that for every (u, w), f(u) < f(v)
- Only graphs without directed cycles can have a topological ordering
- Every DAG has atleast 1 topological ordering
- Source vertex: No incoming edges
- Sink vertex: No outgoing edges
- Every DAG has atleast one source vertex
- Run DFS
- Output reverse of finishing times of vertices
- Correctness
  > For any edge e = (u, v), v finishes before u finishes (reverse order)
  > Case 1: u starts before v (visit v before u finishes)
  > Case 2: v starts before u (This can't happen as there will be a back edge and hence a cycle)
            v finishes before u

- In DFS of an undirected graph, we assign a direction to each edge, from the vertex we discover it
- DFS edges: Tree Edges and Back Edges Only

- A directed graph is a DAG if and only if no back edges are encountered during a depth first search
- Pluck indegree 0, repeatedly and remove dependent edges
- Other way DFS, reverse processed order (Push on stack)

Applications
> Finding cycles
  - Back edges are key for finding a cycle in an undirected graph
  - Any back edge going from x to an ancestor y with a path in tree from y to x
> Articulation vertices can be found in O(n(m+n)) - just delete each vertex to do
  a DFS on the remaining graph see if its connected
  - NOTE: DFS backedge is like a rope holding the mountaineer, so even if he fails to climb that keeps him away from falling
  - In a DFS tree, a vertex v (other than the root) is an articulation vertex if v is not a leaf and some subtree of v has no
    back edge incident until a proper ancestor of v - O(m+n) solution

- Complete Graph with N vertices can have (N-1)! cycles
  > Difficult with DFS, backtracking is better

Entry time and exit time:
Entry Time(Discovery)
Exit Time (Explored)
        1,14 (Any node starts before its descendants and finishes after its descendants - LIFO)
      /  \
     2,11 12,13 
    / \
   3,8 9,10
  / \
 4,5 6,7
Number of descendants: Half the difference between entry and exit times of each node 

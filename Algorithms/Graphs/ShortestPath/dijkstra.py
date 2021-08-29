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

- d[v]: Length of curretn shortest path from source S to V
- S(s, v): delta: length of a shortest path
- Relaxation: d to S(delta)
Relax(u, v, w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        p[v] = u
Should not reduce smaller than S(delta): Relaxation is safe
Relaxation operation maintains the invariant that d[v] >= S(s, v) for all v E V
Relax edges of source node - outgoing edges
Relax(u, v, w): v is impacted
Priorities are d's values
BFS in frontier and Greedy

O(V) - Insert operatins
O(V) - Heap pop extract min
O(E) - relaxation - decrease key

Arrays used as priority Queue:
    - Extract Min: O(V)
    - Decrease Key = O(1), just change value
    - O(V.V + E.1) = O(V^2)
Binary Min Heap:
    - Extract Min: O(1) update O(lgV)
    - O(lg V) for decrease key
    - O(VlgV + ElgV)
Fibonacci heap:
    - Extract Min : O(lgV)
    - Decrease Key: O(1) amortized
    - O(VlgV + E)
DAGs:
- Can't have negative cycles
- Topologocal sort the DAG path from u to v implies that u is before v in the ordering
- One pass over vertices in topologically sorted order relaxing each edge that leaves eac vertex
- O(V+E) linear time

-> Dijkstra/BellmanFord - Single source any/all destination problem
-> Single source specific target
Initialize() <- d[s] = 0, d[u != s] = inf
Q <- V[G]
while Q is not empty:
    do u <- EXTRACT_MIN(Q)
    for each vertex v E Adj[u]:
        do relax(u, v, w)
        stop when u == t # specific target

->Bidirectional Search
  - Alternate forward search from s
  -           backward search from t
  - d[s] and d[t] = 0
  - Termination Condition: Some vertex u has been processed both in the forward search and backward search
                           Deleted from both Qf and Qb (w)

  - x minimizing shortest path [db[u] + df[u]]

- Goal Dircted Searhc
  > Modify edge weights with potential functions
  > W(u, v) = w(u, v) - lambda(u) + lambda(v)i
  > shortest path modified between s and t will not be impacted
  > Discover it faster
"""
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, float('inf')))

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
                if distance.get(v, float('inf')) > distance[u] + wt: # Relaxation
                    distance[v] = distance[u] + wt
                    parent[v] = u

            u, minWt = start, float('inf')
            for n in self.vertices():
                if n not in frontier and distance[n] < minWt:
                    u, minWt = n, distance[n]
        return distance, parent

    def dijkstraHeap(self, start):
        """
        - Get minimum distance element from heap in a loop
        - Run till heap is empty
        - Relax all its neighbors
        """
        def get_vertex(v):
            for index, (dv, vertex) in enumerate(distance):
                if vertex == v:
                    return index
        
        def relax(u, v, w, du):
            index = get_vertex(v)
            #print(index, v, distance)
            # TODO: assuming it would always be found
            print(v, index, distance)
            dv, _ = distance[index]
            if dv > du + w:
                distance[index] = (du+w, v)
                parent[v] = u

        # Distance is stored as priority in heap
        # No key in heapify hence store in (priority, data) for,
        distance = [(float('inf'), v) for v in self.vertices()]
        parent = dict()
        index = get_vertex(start)
        distance[index] = (0, start)
        heapq.heapify(distance)


        while distance:
            print("##", distance)
            du, u = heapq.heappop(distance)
            print(u)
            for v, w in self.neighbors(u):
                print(u, v, w)
                relax(u, v, w, du)
        return parent

g = Graph()
g.edge('s', 'v', 1)
g.edge('s', 'w', 4)
g.edge('v', 'w', 2)
g.edge('v', 't', 6)
g.edge('w', 't', 3)
#print(g.dijkstra('s'))
print(g.dijkstraHeap('s'))




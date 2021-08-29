"""
Positive and negative weights
O(VE) = O(V^3)
path p = <vo, v1, ..., vk>
(vi, vi+1) E e for 0 <= i < k

w(p) = Sum(i=0 to k-1) w(vi, vi+1)
find p with min weight

Complexity doesn't depend on weight
dynamic range of weights could be very very large

For weighted graphs, it is not true that shortest path gave minimum weight path
    10
A------>B
|       |  
-->C-----
 2   4
Negative weights are not problem but negative cycles are.

General stcucture:
    Initialize: for u E V , d[u] <- inf, p[u] = None
    d[s] <- 0

    Relax: chosse better value
    Repeat select edge (u, v) [Some how]
    if d[v] > d[u] + w(u, v)
        "Relax" edge (u, v)
        d[v] = d[u] + w(u, v)
        p[v] = u
    until all edges have d[v] <= d[u] + w(u, v)

    Termination: No more edges could be relaxed

Exponential range of weights (2^n/2)
Pathological ordering - relaxing edges order of weights exponential time

Optimal Substructure:
    - Subpaths of shortest paths are shortest paths themselves.
Polynomial time algorithm
Detects cycle and sets for every node in that case after the cyle as undefined

Problem with generic graph shortest path:                             ----------> 
    - complexity could be exponential time (2^n/2 - pathological path A--->B--->C---->)
      [This is solved by Dijkstra]
    - will not end if negative cycles are present
Bellman-Ford(G,W, S):
    Initialize()
    for i = 1 to |V|-1:
        for each edge (u, v) E edges:
            Relax(u, v, w)
    for each edge (u, v) E edges: # Vth pass where V is number of vertices
        if d[v] > d[u] + w(u, v): # Check
            Then report negative cycle exists
    O(VE + E) ~ O(V^3)

Done by bellman ford: Polynomial time
- If no negative cycles present -> Shortest simple path
- Detecting cycle and saying undefined

Ask slightly more?
- Give simple path with negative cycles
- Tell longest path
- These problems are NP hard problem - we don't have polynomial time solution but exponential time algorithm is known
"""

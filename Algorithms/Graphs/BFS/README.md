Pocket Cube
-----------
- 2*2*2
- Configuration graph: Vertex for each possible state of cube
- Edges for each possible move
- Vertices: 8! (8 places for each cube) * 3^8 (3 sides for each cube and there are 8 cubes)
            8! * 3^8 = 264 million

             Diameter
  <---------------------------------->
                 --------
         ------N1---------  
- Solved ------N2
         ------N3
- 2*2*2 : Diameter: 11 moves
- 4*4*4 : Diameter: 20 moves
- n*n*n : n^2/lgn

Breadth First Search
--------------------
- Visit all nodes reachable from a given node s (element of) V
- O(V+E) time
- Look at nodes reachable in 0 moves, 1 moves, ...
- Careful to avoid duplicates (don't visit again) [as we can do that infinite time and never end]
- Works for both directed and undirected graph
- Layer-i vertices are the neighbors of Layer-(i-1) vertices that do not appear in any earlier layer
- BFS gives shortest path as we are traversing nodes layer by layer and that could be shortest way to reach a node
- Shortest Path
  > v <- parent[v]
  > If we move in that fashion till we reach s, its shortest path from s to v
  > Length of path will be level[v]
- Running Time: Sum v (is element) V |adj(v)| = 2.|E| (undirected) and |E| (directed)
                And we touch each vertex, therefore O(|V| + |E|)

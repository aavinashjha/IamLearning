Finding all spanning trees and looking for minimum is O(4^N) algorithm - Exponential
Optimal substructure of MST:
 - if e = {u, v} is an edge of some MST
 - contract e so G becomes G/e: e compressed that is u and v merged into single vertex
 - u and v are not removed
 - If T' is MST of G/e then T' U {e} is MST of G
 - Dynamic Program:
   > Guess edge e in a  MST
   > Contract e
   > recurse
   > Decontract
   > Add e to T

Both are greedy techniques
Prim:
- Suggests to be connected to the tree you are growing
- Choose any random node as root, need not have minimum connected edge
- Heap maintains candidates for next node [Start with all other nodes except root - O(N)]
- Inverted index in heap
- For every edge we will update heap seeing its value O(MlgN)
- O(N) + O(M) + O(MlgN)
- O(N^2) -> Dense
- O(MlgN) -> Sparse

Kruskal:
- Let it happen in parallel, disjoint trees or forest and let the forest grow together
- Amortized analysis is better than Prim

"""
- If DFS tree represents the entirety of graph, all internal (nonleaf) nodes would be articulation
  vertices, since deleting any one of them would separate a leaf from a root.

- The root of the search tree is a special case. If it has only one child, it functions as a leaf otherwise AP.
- DFS Traversal(Search) of general graph partitions the edges into tree edges and back edges

- Finding AV requires maintaining the extent to which back edges (i.e. security cables) link
  chunks of the DFS tree back to ancestor nodes.
- Let reachableAncestor denote the earliest reachable ancestor of v, meaning the oldest ancestor
  of v that we can reach by a combination of tree edges and back edges.
- Update reachableAncestor[v] whenever we encounter a back edge that takes us to an earlier
  ancestor that we have previously seen.
- The relative age/rank of our ancestors can be determined from the entryTime


Connectivity is 1 if articulation vertex is present
If no articulation vertex then graph is called biconnected

Articulation vertex or cut vertex: Removing it and all its edges increase number of connected components
- root is an articulation vertex if it has more than 1 child
- leaf is never an articulation vertex
- no back edge exists for non-root and non-leaf vertex, then it is an articulation vertex

In a DFS tree, a vertex v (other than the root) is an articulation vertex if v is not a leaf and some subtree
of v has no backedge incident until a proper ancestor of v
- Finding articulation point requires maintaining the extent to which back edges (i.e. security cables) link
  chunks of the dfs tree back to ancestor node
- reachable_ancestor[v]: Denotes the earliest reachable ancestor of vertex v, meaning the oldest ancestor of v
                         that we can reach by a combination of tree edges and back edges. Initially reachable_ancestor[v] = v

  A
 / \
B - C 
A is root
B-C form single subtree, as DFS traversal traverses C as well. (Only 1 child)

How to detect AP for Case 1: 
    - Keep children counter for each node
    - On calling DFS on each edge, mark the entire subgraph
    - Call DFS on other nodes only if node is not visited
    - Increment child count on each unique DFS call
    - ID children > 1 then vertex is AP

Case 2: Node u is not root of DFS tree and it has child v such that
        no vertex is subtree rooted with v has a backedge to one of its ancestors of u
    - We need to find order of vertices from earliest to latest to detect back edges
      > We use timestamp to mark nodes with increasing value
      > We can do this by assigning discovery time
    - We need to maintain earliest possible node accessible for a given node which
      will indicate if we have any back edge
      For that we will assign low value to each node

processVertexEarly: Marks the reachable ancestor as current vertex
processEdge       : Identify edge as tree/back edge and if tree edge increase
                    outgoing edge and if back edge set oldest ancestor
processVertexLate : Systematically evaluates each of the three conditions as we backup
                    from the vertex after traversing all outgoing edges.
                    - Root cut-nodes: Root of DFS tree have two or more children
                    - Bridge cut-nodes: If the earliest reachable vertex from v is v,
                      then deleting the single edge (parent[v], v) disconnects the graph.
                      parent[v] must be AP
                    - Parent cut-nodes: If the earliest reachable vertex from v is parent of v,
                                        then deleting the parent must separate v from the tree unless
                                        the parent is the root
                    The reachability time time_v calculated below denotes the oldest vertex that can be
                    reached using back edges
                    Getting back to an ancestor above v rules out the possibility of v being a cut-node
                    - Parent of v < 1 # Its root
                        > Check outDegree > 1 # This is an AP
                    - Is Parent[v] root?
                      root = parent[parent[v]] < 1
                      if reachableAncestor[v] == parent[v] # Bridge articulation vertex
                    - if reachableAncestor[v] == v
                      > parent[v] # parent[v] is AP
                      > outDegree[v] > 0 # not leaf, bridge articulation vertex
                    - Backup node's highest reachable ancestor to its parent, namely whenever it is higher than
                      the parent's earliest ancestor to date
"""
from collections import defaultdict, namedtuple

UNDISCOVERED = 1
DISCOVERED   = 2
EXPLORED     = 3

TREE=1
BACK=2
FORWARD=3
CROSS=4

VERTEX = namedtuple('vertex', ['val', 'state', 'parent', 'ancestor', 'outdegree'])

class Graph:

    def __init__(self):
        self.g = defaultdict(list)
        self.time = 0

    def edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def neighbors(self, u):
        return self.g[u]

    def _dfs(self, u, state, entryTime, parent, outdegree, ancestor, ap):
        undiscovered = lambda u: u not in state
        discovered = lambda u: u in state and state[u] == DISCOVERED
        explored = lambda u: u in state and state[u] == EXPLORED

        def processVertexEarly(u):
            state[u] = DISCOVERED
            self.time += 1
            entryTime[u] = self.time
            ancestor[u] = u

        def processVertexLate(u):
            state[u] = EXPLORED
            root = parent[u] is None
            parentIsRoot = parent[u] is not None and parent[parent[u]] is None

            # root cut-node
            if root and outdegree[u] > 1:
                print('root cut-node: {}'.format(u))
                ap.add(u)
            # parent cut-node
            elif not parentIsRoot and ancestor[u] == parent[u]:
                ap.add(parent[u])
                print('parent cut-node: {}'.format(parent[u]))
            # bridge cut-node
            elif not root and not parentIsRoot and ancestor[u] == u:
                ap.add(parent[u])
                print('bridge cut-node: {}'.format(parent[u]))
                if outdegree[u] > 0:
                    print('bridge cut-node non leaf: {}'.format(u))
                    ap.add(u)

            # Update ancestor of parent vertex
            if not root and entryTime[ancestor[u]] < entryTime[ancestor[parent[u]]]:
                ancestor[parent[u]] = ancestor[u]

        def processEdge(u, v):
            #print("Processing edge: {}".format((u, v)))
            edgeType = None
            if undiscovered(v): edgeType = TREE
            elif discovered(v): edgeType = BACK
            elif explored(v) and entryTime[v] > entryTime[u]: edgeType = FORWARD
            elif explored(v) and entryTime[v] < entryTime[u]: edgeType = CROSS

            if edgeType == BACK and parent[u] != v:
                if entryTime[v] < entryTime[ancestor[u]]: ancestor[u] = v
            elif edgeType == TREE:
                outdegree[u] += 1

        processVertexEarly(u)

        for v in self.neighbors(u):
            processEdge(u, v)
            if undiscovered(v):
                parent[v] = u
                self._dfs(v, state, entryTime, parent, outdegree, ancestor, ap)

        processVertexLate(u)

    def dfs(self):
        ap, state, entryTime, parent, outdegree, ancestor = set(), {}, {}, {}, defaultdict(int), {}
        for u in self.g.keys():
            if u not in state:
                parent[u] = None
                self._dfs(u, state, entryTime, parent, outdegree, ancestor, ap)
        return ap

g = Graph()
g.edge(1, 2)
g.edge(1, 3)
g.edge(1, 4)
g.edge(1, 5)
g.edge(2, 4)
g.edge(3, 5)
g.edge(4, 6)
g.edge(5, 9)
g.edge(5, 10)
g.edge(6, 7)
g.edge(6, 8)
g.edge(7, 8)
g.edge(9, 10)
g.edge(9, 11)
g.edge(10, 11)
print(g.dfs())
"""
g = Graph()
g.edge(1, 2)
g.edge(2, 3)
g.edge(3, 4)
print(g.dfs())
"""

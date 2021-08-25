"""
Topological Sort of graph is an ordering on vertices so that all edges go from left to right
Makes sense only for directed graph not having cycle (DAGs)
DAGs have atleast one topological sort
Directed graph is a DAG if and only if no backedges are encountered during a depth first search
Labelling each of the vertices in reverse order that they are marked processed finds a topological sort of DAG 
Leftmost node has to have indegreee of 0

Naive way:
    - Find all nodes that have no nodes going into them [indegree = 0]
      [N+M - go through all nodes and also through all edges, consider
      first node has all edges and others have no edges - M for first
      and move over other nodes to see their ebtries which is N]
    - Delete it output it
    - Repeat till graph has nodes (or is not empty)
    - N(N+M) ~O(N^3)
Better Way:
    - Calculate indegree in advance [N+M]
      Move across adjacency lists of edges and whenever encounter a node increment indegree

      A-->B
      ^   ^
      |   |
      C---

      A -> B
      B -> 
      C -> A, B
               A  B C
      indegree 1  2 0
      No need to see left node, just adjacency list
    - Look through indegree 0 and see its linked list and whatever nodes are there decrement its indegree
      C has indegree 0 [first result]
      Its adjacency list has 2 elements, reduce those nodes by 1
               A  B  C
      indegree 0  1  0
      A not added and indegree 0 [second result]
      A's adjacency list has B
               A  B  C
      indegree 0  0  0 
      C -> A -> B
    - A queue could be used to add element whever they turn 0 on indegree subtraction
    - Every single node goes to queue only once (when indegree reaches 0) [O(N)]
    - We are deleting all edges when we pull element out of queue O(M)
"""
from collections import defaultdict, deque

class Stack:
    def __init__(self):
        self.s = list()

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def isEmpty(self):
        return len(self.s) == 0

class Queue:
    def __init__(self):
        self.q = deque()

    def enque(self, x):
        self.q.append(x)

    def deque(self):
        return self.q.popleft()

    def isEmpty(self):
        return len(self.q) == 0

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        #self.exitTime = dict()
        self.discovered = set()
        #self.time = 0

    def edge(self, u, v):
        self.g[u].append(v)

    def neighbors(self, u):
        return self.g[u]

    def _dfs(self, u, s):
        def processVertexEarly(u):
            self.discovered.add(u)
            #self.time += 1

        def processVertexLate(u):
            #self.time += 1
            #self.exitTime[u] = self.time
            s.push(u)
            

        processVertexEarly(u)
        for v in self.neighbors(u):
            if v not in self.discovered:
                self._dfs(v, s)
        processVertexLate(u)

    def topologicalSort(self):
        s = Stack()
        for u in self.g.keys():
            if u not in self.discovered:
                self._dfs(u, s)
        #return [i[0] for i in sorted(self.exitTime.items(), key=lambda x: x[1])][::-1]

        topSort = list()
        while not s.isEmpty():
            topSort.append(s.pop())
        return topSort

    def topologicalSortAugmented(self):
        indegree = defaultdict(int)
        q = Queue()
        sol = list()

        # Read all the edges and right side of adjacency list shows edges coming to those nodes
        for vs in self.g.values(): # O(N+M)
            for v in vs:
                indegree[v] += 1

        for u in self.g.keys():
            if indegree[u] == 0: q.enque(u)

        while not q.isEmpty():
            u = q.deque()
            sol.append(u)
            # Pulled the node from graph, remove edges connected to it
            for v in self.neighbors(u):
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.enque(v)
        return sol


g = Graph()
g.edge('A', 'B')
g.edge('A', 'C')
g.edge('B', 'C')
g.edge('B', 'D')
g.edge('C', 'E')
g.edge('C', 'F')
g.edge('E', 'D')
g.edge('F', 'E')
g.edge('G', 'A')
g.edge('G', 'F')
print(g.topologicalSort())
print(g.topologicalSortAugmented())

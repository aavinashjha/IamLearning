from collections import defaultdict

class Stack:
    def __init__(self):
        self.s = list()

    def push(self, e):
        self.s.append(e)

    def pop(self):
        return self.s.pop()

    def isEmpty(self):
        return len(self.s) == 0

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v):
        self.g[u].append(v)

    def __str__(self):
        return "\n".join(["{} -> {}".format(str(k), str(v)) for k, v in self.g.items()])

    def neighbors(self, u):
        return self.g[u]

    def vertices(self):
        return self.g.keys()

    def dfsS(self, s):
        stack = Stack()
        stack.push(s)
        sol = []
        explored = set()

        while not stack.isEmpty():
            u = stack.pop()
            if u not in explored:
                explored.add(u)
                sol.append(u) # Postpone checking if its unexplored till we remove it

                for v in self.neighbors(u):
                    stack.push(v)

        return sol

    def dfs(self):
        parent = dict()
        def dfsvisit(u):
            for v in self.neighbors(u):
                if v not in parent:
                    parent[v] = u
                    dfsvisit(v)

        for s in self.vertices():
            if s not in parent:
                parent[s] = None
                dfsvisit(s)

        return parent

    def 

g = Graph()
g.edge('a', 'b')
g.edge('a', 'd')
g.edge('b', 'e')
g.edge('c', 'e')
g.edge('c', 'f')
g.edge('d', 'b')
g.edge('e', 'd')
g.edge('f', 'f')

print(g)
print("DFS Stack: {}".format(g.dfsS('s')))
print("DFS Stack: {}".format(g.dfs()))


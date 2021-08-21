from collections import defaultdict

DISCOVERED=1
EXPLORED=2

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.time = 0

    def edge(self, u, v):
        self.g[u].append(v)

    def neighbors(self, u):
        return self.g[u]

    def _dfs(self, u, state, entryTime, parent, edges):
        undiscovered = lambda u: u not in state
        discovered = lambda u: u in state and state[u] == DISCOVERED
        explored = lambda u: u in state and state[u] == EXPLORED

        def processVertexEarly(u):
            state[u] = DISCOVERED
            self.time += 1
            entryTime[u] = self.time

        def processVertexLate(u):
            state[u] = EXPLORED

        def processEdge(u, v):
            parent[v] = u
            if undiscovered(v): edges['Tree'].append((u, v))
            elif discovered(v): edges['Back'].append((u, v))
            elif explored(v) and entryTime[v] > entryTime[u]: edges['Forward'].append((u, v)) 
            elif explored(v) and entryTime[v] < entryTime[u]: edges['Cross'].append((u, v))
            else: edges['Unidentified'].append((u, v))

        processVertexEarly(u)

        for v in self.neighbors(u):
            processEdge(u, v)
            if undiscovered(v):
                self._dfs(v, state, entryTime, parent, edges)


        processVertexLate(u)

    def dfs(self):

        state, entryTime, parent = {}, {}, {}
        edges = {'Tree': [], 'Back': [], 'Forward': [], 'Cross': [], 'Unidentified': []}
        for u in self.g.keys():
            if u not in state:
                parent[u] = None
                self._dfs(u, state, entryTime, parent, edges)
        return edges

g = Graph()
g.edge(1, 2)
g.edge(1, 3)
g.edge(1, 8)
g.edge(2, 4)
g.edge(4, 6)
g.edge(6, 2)
g.edge(3, 5)
g.edge(5, 4)
g.edge(5, 7)
g.edge(5, 8)
print(g.dfs())


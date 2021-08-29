"""
- Sort the edges (MlogM = N^2 log N^2 = MlogN)
- {x, y} form a cycle?
  Data Structure - Union Find
    Find: find whether the element is of a group/set or not
    Union: Combine the two sets
- If x,y are in same set then new edge will introduce cycle
  for x, y in sorted order:
      if not (find(x) == find(y)) then union(find(x), find(y))

- Each set is called equivalence class and elements in a class are called
  coequivalent classes

- Union: Parent Array holding pointers for each pointer
- Initializing: O(N)
- Find: Move up the parent till NIL O(N)
- Union: O(1)
This takes MN time slower than prim

Weighted union- see height and make find O(N)
Kepp as bushy as possible for lgN and its not binary tree
Heurestic: Thumb Rule
Path Compression:
    - Worst case is still O(lgN) for find
    - Worst case for p find is not plgN but is better
    - This is amortized cost, not single instance but run multiple times
    - average is better than lgN
    - p lg*N tiny as compared to lgN
    - lg*N is height of stack of 2^2^2^2^...
    - Very slow growing function

makeSet: Initializes one element sets, with each one representing its own class
findSet: Returns representative element of the group
union  : Combines two groups

- Union arbitrarily: Height will increase -- find(O(1)), union(O(N))
- Weighted Union: Put smaller below larger -- union(O(lg(N)))
- Union by rank (same as height)
- Path Compression: When doing find update node's parent to the actual representaive parent

1 2 3
1: Element(1, 1, 0)
2: Element(2, 2, 0)
3: Element(3, 3, 0)

1-2

Quick Find:
    Integer array id[] of size N
    Interpretation: p and q are connected if they have same id
    Check p and q have same id
    > Union: To merge components containing p and q, change all entries whose id equals id[p] to id[q]
             for i in range(N):
                if id[i] == pid: id[i] = qid
             Many values can change
    > Find/Connected : id[p] == id[q]

    Cost Model: Number of array acceses (for read or write)
    Initialize O(N)
    Union      O(N)
    Find       O(1)

    To process M union commands, O(MN) array acceses would be done
    Trees are flat but too expensive to keep them flat
"""
class QuickFind:
    def __init__(self, elements):
        self.id = dict()
        self.makeSet(elements) # O(N)

    def makeSet(self, elements):
        for i in elements: self.id[i] = i

    def union(self, p, q):
        # from p to q
        pid, qid = self.id[p], self.id[q]
        print("Union {}({}) - {}({})".format(p, pid, q, qid))
        for i in self.id:
            if self.id[i] == pid:
                self.id[i] = qid

    def find(self, x):
        return self.id[x]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

a = [1, 2, 3, 4, 5]
qf = QuickFind(a)
assert not qf.connected(1, 2)
assert not qf.connected(4, 5)
qf.union(1, 2)
assert qf.connected(1, 2)
qf.union(4, 5)
assert qf.connected(4, 5)
qf.union(1, 4)
assert not qf.connected(3, 4)
qf.union(4, 3)
assert qf.connected(2, 3)

"""
QuickUnion:
    - Integer array id[] of size N
    - Interpretation: id[i] is parent of i
    - Root of i is id[id[id[...]]] keep going until it doesn't change
    Find : Check if p and q have same root
    Union: To merge components containing p and q, set the id of p's root to the id of q's root

    Trees can get tall, find too expensive
"""

class QuickUnion:
    def __init__(self, elements):
        self.id = dict()
        self.makeSet(elements)

    def makeSet(self, elements):
        for i in elements:
            self.id[i] = i

    def find(self, x):
        if self.id[x] == x: return x
        return self.find(self.id[x])

    def union(self, p, q):
        pr = self.find(p)
        qr = self.find(q)

        self.id[pr] = qr # root of p's parent becomes q's root

    def connected(self, x, y):
        return self.find(x) == self.find(y)

a = [1, 2, 3, 4, 5]
qu = QuickUnion(a)
assert not qu.connected(1, 2)
assert not qu.connected(4, 5)
qu.union(1, 2)
assert qu.connected(1, 2)
qu.union(4, 5)
assert qu.connected(4, 5)
qu.union(1, 4)
assert not qu.connected(3, 4)
qu.union(4, 3)
assert qu.connected(2, 3)


class WeightedQuickUnion: # Path Compression added
    def __init__(self, elements):
        self.id = dict()
        self.makeSet(elements)

    def makeSet(self, elements):
        for i in elements:
            self.id[i] = [i, 0]

    def find(self, x):
        p, height = self.id[x]
        if p != x:
            return self.find(p)
            #self.id[p] = self.find(p)  # Path compression
            
        return [p, height]


    def union(self, p, q):
        pr, pheight = self.find(p)
        qr, qheight = self.find(q)
        if pheight > qheight:
            self.id[qr] = [pr, pheight]
        elif pheight < qheight:
            self.id[pr] = [qr, qheight]
        else: # pheight == qheight:
            self.id[pr] = [qr, pheight] # root of p's parent becomes q's root
            self.id[qr][1] += 1

    def connected(self, x, y):
        return self.find(x)[0] == self.find(y)[0]

a = [1, 2, 3, 4, 5]
wqu = WeightedQuickUnion(a)
assert not wqu.connected(1, 2)
assert not wqu.connected(4, 5)
wqu.union(1, 2)
assert wqu.connected(1, 2)
wqu.union(4, 5)
assert wqu.connected(4, 5)
wqu.union(1, 4)
assert not wqu.connected(3, 4)
wqu.union(4, 3)
assert wqu.connected(2, 3)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, w))

    def neighbors(self, u):
        return self.g[u]

    def kruskal(self):
        edges = list()
        for u, edge in self.g.items():
            for e in edge:
                edges.append((u, e[0], e[1]))

        edges = sorted(edges, key=lambda x: x[2])
        
        vertices = [u for u in self.g]
        wqu = WeightedQuickUnion(vertices)
        print(edges)
        for u, v, w in edges:
            if not wqu.connected(u, v):
                wqu.union(u, v)
                print("Adding ({}, {}, {}) to MST".format(u, v, w))

g = Graph()
g.edge('a', 'b', 1)
g.edge('a', 'c', 4)
g.edge('a', 'd', 3)
g.edge('b', 'd', 2)
g.edge('c', 'd', 5)
g.kruskal()


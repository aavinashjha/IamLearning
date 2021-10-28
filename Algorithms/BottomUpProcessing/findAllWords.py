ROOT = 1
class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.eow = False
        self.par = None

    def isRoot(self):
        return self.value == ROOT
    
    def add(self, child):
        self.children[child.value] = child
        child.par = self
    
    def child(self, value):
        return self.children[value]
    
    def present(self, c):
        return c in self.children
    
    def setEOW(self):
        self.eow = True
    
    def isEOW(self):
        return self.eow

    def parent(self):
        return self.par
    
class Trie:
    def __init__(self):
        self.root = Node(ROOT)
        self.mover = self.root

    def addWord(self, word):
        parent = self.root
        for c in word:
            if parent.present(c):
                parent = parent.child(c)
                continue
            child = Node(c)
            parent.add(child)
            parent = child
        parent.setEOW()
    
    def reset(self):
        self.mover = self.root
        
    def char(self, c): # Increments mover
        parent = self.mover
        #print("Current Node: {}. Char searched: {}".format(parent.value, c))
        if not parent.present(c):
            return False
        parent = parent.child(c)
        self.mover = parent    
        return True
    
    def rollback(self):
        self.mover = self.mover.parent()
    
    def eow(self):
        return self.mover.isEOW()
    
    def resetEOW(self):
        self.mover.eow = False
    
    def word(self):
        cache = []
        m = self.mover
        while not m.isRoot():
            cache.append(m.value)
            m = m.parent()
        return "".join(cache[::-1])
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        - DFS has to be done from each node as word can start from anywhere
        - Make a trie for words
        
        """
        def neighbors(u):
            r, c = u
            n = []
            d = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in d:
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr > M-1 or nc > N-1: continue
                if (nr, nc) in discovered: continue
                n.append((nr, nc))
            return n
        
        def pe(u, trie):
            r, c = u
            if not trie.char(board[r][c]): return False
            if trie.eow():
                sol.append(trie.word())
                trie.resetEOW()
                # Pruning is required in trie
                if len(trie.mover.parent().children[board[r][c]].children) == 0:
                    del trie.mover.parent().children[board[r][c]]
            discovered.add(u)
            return True
        
        def pl(u, trie):
            trie.rollback()
            discovered.remove(u)
        
        def dfs(u, trie):
            r, c = u
            if not pe(u, trie): return
                
            for v in neighbors(u):
                dfs(v, trie)
                
            pl(u, trie)

        M, N = len(board), len(board[0])
        discovered = set()
        sol = []
        trie = Trie()
        for w in words: trie.addWord(w)
            
        for r in range(M):
            for c in range(N):
                #trie.reset()
                #print("dfs on {}".format((r,c)))
                dfs((r, c), trie)
        return sol

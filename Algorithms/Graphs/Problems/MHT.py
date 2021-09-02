from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Constraints:
        - Given a tree of n nodes [0, n-1]
        - Array of n-1 edges
        - edges[i] = [ai, bi] # Undirected edge
        - Any node could be root
        - Minimum height trees
        Goal:
        - Return MHTs root label
        Idea:
        - Run DFS
        - Diff between entry and exit time // 2 tells number of nodes below it
        - O(N^2)

        """

        
        def dfs(root, al): # O(M+N)
        
            def neighbors(u):
                return al[u]
            
            def processVertexEarly(u):
                discovered.add(u)
                nonlocal time
                time += 1
                entryTimeStore[u] = time

            def processVertexLate(u):
                nonlocal time
                time += 1
                exitTimeStore[u] = time

                
            def _dfs(u):
                processVertexEarly(u)
                for v in neighbors(u):
                    if v not in discovered:
                        _dfs(v)

                processVertexLate(u)
            
            def height(u, seen, known):
                if u in known: return known[u]
                seen.add(u)
                # Leaf Node
                if exitTimeStore[u] - entryTimeStore[u] == 1: return 0
                
                h = float('-inf')
                for n in neighbors(u):
                    if n not in seen:
                        ch = height(n, seen, known)
                        known[n] = ch
                        h = max(h, ch)

                return 1+h

            time = 0
            entryTimeStore, exitTimeStore = dict(), dict()
            discovered = set()
            _dfs(root)
            seen = set()
            known = dict()
            return height(root, seen, known)


        def createAL(): # O(M)
            al = defaultdict(list)
            for u, v in edges:
                al[u].append(v)
                al[v].append(u)
            return al
        
        al = createAL()
        if not al: return [0]
        
        roots = list()
        minHt = float('inf')
        for root in list(al.keys()):
            h = dfs(root, al)
            minHt = min(minHt, h)
            roots.append((root, h))

        result = []
        for r, h in roots:
            if h == minHt:
                result.append(r)
        return result

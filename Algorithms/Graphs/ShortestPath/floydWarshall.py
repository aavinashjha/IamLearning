"""
All Pair Shortest Path:
Make a facility in between so that its near to everything
d[i, j]k : distance of reaching from i to j considering only k vertices
k is not number of vertices but index of vertex (upto that vertex)

Let d[i, j]^k be the shortest path from i to j using only vertces from
1, 2, ..k as possible intermediate values
d[i, j] ^ 0 -> No intermediate edge w[i, j]
d[j, j] ^ 0 -> 0

3D matrix n * n * n that acts as a memo table
dp[k][i][j] = shortest path from i to j routing through nodes {0, 1, .., k-1, k}

dp[k][i][j] = min(dp[k-1][i][j], # Reuse the best distance from i to j with values routing through 0, 1, ..k-1
                    dp[k-1][i][k]+dp[k-1][k][j]) # find best distance from i to j through node k reusing best solution from {0, 1, ..k-1}
              m[i][j] if k = 0

  dp[k-1][i][k] dp[k-1][k][j]
->-------------k------------->|
|                             |
|                             |   
i---------------------------->j
        dp[k-1][i][j]

We need state k-1 to compute k, it is possible to compute the solution for k in place
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
"""
from collections import defaultdict
class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v, w):
        self.g[u].append((v, w))

    def neighbors(self, u):
        return self.g[u]

    def floydWarshall(self):
        n = len(self.g)
        cache = [[float('inf') for _ in range(n)] for _ in range(n)]
        for u, (v, w)  in self.g.items():
            cache[u][v] = w
        for 

        for k in range(1, n):
            for i in range(n):
                for j in range(n):
                    cache[i][j] = min(cache[i][j], cache[i][k] + cache[k][j])

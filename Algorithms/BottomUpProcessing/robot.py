"""
Constraints:
    - Start (N-1, 0) and End(0, M-1) are empty
    - Can move only top and right
    - grid: N strings with m chars
            '0' meaning empty cell
            '1' meaning occupied
Idea:
    - We can reach any point by coming from left or bottom
    - Hence number of ways to reach a point is equal to sum of number of ways to reach left point + number of ways to reach right point
    - Mark all '1' cells as 0 ways
    - Also include one left column and one bottom row for handling corner cases
"""

EMPTY = -1 
def count_the_paths(grid):
    N, M = len(grid), len(grid[0])
    if N == 1 and M == 1: return 1

    cache = [[EMPTY for _ in range(M+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(1, M+1):
            if grid[i][j-1] == '1':
                cache[i][j] = 0 # No ways

    for j in range(M+1):
        cache[N][j] = 0

    for i in range(N+1):
        cache[i][0] = 0

    cache[N-1][1] = 1 # One way to reach itself

    for i in range(N-1, -1, -1):
        for j in range(1, M+1):
            if cache[i][j] == EMPTY:
                cache[i][j] = (cache[i][j-1] + cache[i+1][j]) % 1000003

    return cache[0][M]

grid = ["0100", "0010", "1000", "0000"]
print(count_the_paths(grid))

class NumMatrix:
    """
    Constraints:
    - Two diagonally opposite corners are given
    Goal:
    - Return sum
    Idea:
    - Store sum at top corner of all below it
    2 0 1
    1 0 1
    0 3 0
        
    8 5 2
    5 4 1 
    3 3 0

    """

    def cache(self, matrix):
        M, N = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(N+1)] for _ in range(M+1)]
        
        for r in range(1, M+1):
            for c in range(1, N+1):
                prefix[r][c] = prefix[r-1][c] +\
                        prefix[r][c-1] -\
                        prefix[r-1][c-1] +\
                        matrix[r-1][c-1]
        return prefix
        
        
    def __init__(self, matrix: List[List[int]]):
        self.prefix = self.cache(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.prefix[row2][col2] +\
            self.prefix[row1-1][col1-1] - \
            self.prefix[row2][col1-1] - \
            self.prefix[row1-1][col2]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


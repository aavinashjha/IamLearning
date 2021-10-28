class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Constraints:
        - n *n 2D matrix
        - rotate 90 degree clockwise
        - inplace
        - square
        
        Idea:
        0,0 --> 0,2 (N-1+r)%N = (3-1+0) % 3 = 2
        0,1--> 1, 2  =(3-1+1) % N
        0,2--> 2, 2 (N-1-r)
        
        Row will become?
        
        - 00 02 (N-1-r))  (N-r+1: )
        - 01 11 (3-1+1)
        - 02 22 (3-1+2)
        - 10 02
        Row will become column?
        
        (r, c) <--> (c, N-1-r)
        (1, 1) <--> (1, 3-1-1)
        (2, 1) <--> (1, 3-1-2) (1, 0)
        
        1 2
        3 4
        
        """
        def transpose():
            N = len(matrix)
            for r in range(N):           
                for c in range(r, N):
                    matrix[r][c], matrix[c][r] =\
                        matrix[c][r], matrix[r][c]
        
        def reflect():
            N = len(matrix)
            for r in range(N):
                for c in range(N//2):
                    matrix[r][c], matrix[r][N-c-1] =\
                        matrix[r][N-c-1], matrix[r][c]
        transpose()
        #print(matrix)
        reflect()
        return
        
        N = len(matrix)
        colLen = N
        for r in range(N):
            for c in range(colLen):
                
                matrix[r][c], matrix[c][N-r-1] = matrix[c][N-r-1], matrix[r][c]
            colLen -= 1

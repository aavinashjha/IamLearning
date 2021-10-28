class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(lr, lc, hr, hc, target):

            if lr > hr or lc > hc: return False
            if lr == hr and lc == hc and matrix[lr][lc] != target: return False
            #mr, mc = lr+(hr-lr)//2, lc+(hc-lc)//2
            mr, mc = (lr+hr)//2, (lc+hc)//2
            if matrix[mr][mc] == target:
                return True
            elif target < matrix[mr][mc]:
                return bs(lr, lc, hr, mc-1, target) or\
                        bs(lr, lc, mr-1, hc, target)
            else:
                return bs(lr, mc+1, hr, hc, target) or\
                        bs(mr+1, lc, hr, hc, target)
            
        
        
        M, N = len(matrix), len(matrix[0])
        return bs(0, 0, M-1, N-1, target)

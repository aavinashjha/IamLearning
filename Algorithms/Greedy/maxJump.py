class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Goal: minimum number of jumps
        Constraints:
        - Use minimum ladders
        - always reach end
        Idea:
        - select maximum reachability of a ladder
        2 3 1 1 4
        0 1 1 
        
        mj(i) = minimum jumps to reach index i
        mj(0) = 0
        usedMax = 2
        maxPossible = 2 4
        
        count = 1
        Each time usedMax is exhausted and we use new maxPossible, we increase count
        [2,3,1,1,4]
        2  
        """
        N = len(nums)
        if N == 1: return 0
        
        count = 1
        usedMax, maxPossible = nums[0], nums[0]
        
        for i in range(1, N):
            if usedMax < i:
                count += 1
                usedMax = maxPossible
                
            maxPossible = max(maxPossible, i+nums[i])
        return count    
        

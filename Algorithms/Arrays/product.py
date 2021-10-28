class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Constraint:
        - integer array nums
        - product of all other elements
        - Without using division operator
        - O(N)
        
        Goal:
        - Return answer array
        
        Idea:
        - 1 2 3 4
        - 24 12 8 6
        
        
        100
         10
        """
        N = len(nums)
        
        p = [1 if i == 0 else nums[i-1] for i in range(N)]
        p = [1] *N
        # Exclude product with the current element prefix
        for i in range(1, N):
            p[i] = nums[i-1]*p[i-1]
        
        # Exclude current element till suffix
        #s = [1]*N
        #for i in range(N-2, -1, -1):
        #    s[i] = nums[i+1]*s[i+1]
        #print(p)
        suffix = 1
        for i in range(N-1, -1, -1):
            #p[i] *= s[i]
            p[i] *= suffix
            suffix *= nums[i]
            
        
        return p
        
        prod = 1
        for e in nums:
            prod *= e
            
        ans = []
        
        for e in nums:
            ans.append(prod/e)
        
        return ans
        

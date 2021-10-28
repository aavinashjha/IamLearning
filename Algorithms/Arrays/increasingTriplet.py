class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Constraint:
        - i < j < k implies nums[i] < nums[j] < nums[k]
        
        Goal:
        - Triplet exists
        - Otherwise false
        
        Idea:
        - Sorting would be of less help as indices are important
        - [1, 2, 3, 4, 5]
        - Three loops O(N^3)
        
        
        Approach 2:
        - 5 4 3 2 1
        
        - 1 2 3 4 5
          4 3 2 1 0
          0 0 0 0 0
          
          
          n: 1 2 3 4 5
          i: 0 1 2 3 4
             4 3 2 1 0
             
             
          n: 2,1,5,0,4,6
          i: 0 1 2 3 4 5
          
          s: 0 1 2 4 5 6
          i: 3 1 0 4 2 5
          a: 2 2 2 1 1 0
          
          start with 1, if length is >= 3 return true
          
          
          we move over it to find if
          
          n: 20,100,10,12,5,13
          i:  0  1   2  3 4 5
          
          s: 5 10 12 13 20 100
          i: 4 2  3  5  0  1
          a: 3 3  2  2  2  1 
          
          n: 1 2 1 3
          i: 0 1 2 3
          
          s: 1 1 2 3
          i: 0 2 1 3
          a:     2 1
         
         n: 2 1 5 0 4 6
         m: 2 1 1 0 0 0
         x: 6 6 6 6 6 6
         
         1 2 1 3
         
        """
        min1, min2 = float('inf'), float('inf')
        for n in nums:
            if min1 < min2 < n:
                return True
            elif n < min1:
                min1 = n
            elif min1 < n < min2 :
                min2 = n
        return False
            
        
        
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if nums[i] < nums[j] and nums[j] < nums[k]: return True
        return False
        

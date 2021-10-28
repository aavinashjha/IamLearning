class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Constraints:
        - 0, 1, 2
        Goal:
        - inplace sort
        Idea:
        - Use counting sort as only 3 elements are there
        - O(N): Time
        - O(1): space
        
        0s..b1..1s..b2.undiscovered..b3...2s
        Invariant: before b0: 0s
                   between b0 and b1: 1s
                   between b1 and b2: undiscovered
                   after b2: 2s 
                   
        Every loop iteration try to reduce problem size by 1
        b0 is on 0, increment b0
        b2 is on 2: reduce b2
        b1 is on 1: increment b1
        
        2  0 2 1 1 0
        b0         b2
        b1
        increment b1 if 0 swap it with b0
        if 2 swap it with b1
        if b1 has 1 swap b0 and b2
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        N = len(nums)
        b0, b1, b2 = 0, 0, N-1
        
        while b1 <= b2:
            if nums[b1] == 0:
                swap(b0, b1)
                b1 += 1
                b0 += 1
            elif nums[b1] == 1:
                b1 += 1
            else:
                swap(b1, b2)
                b2 -= 1
        return
      
    
        c0, c1, c2 = 0, 0, 0
        for n in nums:
            if n == 0: c0 += 1
            elif n == 1: c1 += 1
   
        N = len(nums)
        for i in range(N):
            if i < c0:
                nums[i] = 0
            elif i >= c0 and i < c0+c1:
                nums[i] = 1
            else:
                nums[i] = 2
        

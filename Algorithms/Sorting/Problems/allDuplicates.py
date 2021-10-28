class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Constraint:
        - nums are in range [1, n]
        - Each integer appears once or twice
        Goal:
        - Return array of all the integers that appear twice            
        """
        sol = list()
        n = len(nums)
        i = 0
        
        while i < n: # n = 3
            val = nums[i]
            index = val-1
            if i == index or nums[i] == nums[index]:
                i += 1
            else:
                nums[i], nums[index] = nums[index], nums[i]
        
        for i in range(n):
            if i != nums[i] -1:
                sol.append(nums[i])
        return sol

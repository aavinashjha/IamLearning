import bisect

class Solution:
    def search(self, nums, target):
        """
        Constraints:
        - nums (array of integers)
        - already sorted [ascending order, smallest is the first element]
        - target [integer]
        Goal: search target in nums
              - if target exists return its index
              - otherwise return -1
              - O(logN)
        Idea:
        - Already sorted
        - Use binary search
        """
        index = bisect.bisect_left(nums, target)
        if index == len(nums) or nums[index] != target: return -1
        return index

nums = [1, 4, 5, 7, 9, 11]
target = 6
print(Solution().search(nums, target))


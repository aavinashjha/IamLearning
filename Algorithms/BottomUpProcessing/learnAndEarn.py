from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums) # Maximum number
        cache = [0] * (n+1)
        for i in nums:
            cache[i] += i
        
        # select non adjacent ones
        N = len(cache)
        pp, p = 0, 0
        for i in range(N):
            pp, p = p, max(p, cache[i]+pp)
        return p

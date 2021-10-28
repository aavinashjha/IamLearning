from functools import lru_cache
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Idea:
        - Subarray sum is sum of contiguous elements
        - If we maintain a cumulatve sum at each index
        - we can see if cs at i -cs at j == k
        - cs is 0 initially
        """
        N = len(nums)
        if N == 0: return 0
        
        cs = {0: 1}
        s = 0
        count = 0
        for i in range(N):
            s += nums[i]
            req = s-k # Required
            if req in cs:
                count += cs[req]
            cs[s] = 1+cs.get(s, 0)
        return count

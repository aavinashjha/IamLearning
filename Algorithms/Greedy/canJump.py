
#def canJump(self, nums):
#        t = list(accumulate([i + num for i, num in enumerate(nums)], max))
#        return all(i != t[i] for i in range(len(t) - 1))
from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Constraint:
        - At array's first index
        - value is maximum jump
        Goal:
        - Return tru if we can reach last index
        Idea:
        - we can jump 1..j
        - return true if any is possible
        j(i) = Jump possible from index i
        j(N-1) = True
        j(i) = any([j(i) for j in range(1, jump+1)])
        j(0) = ?
        """

        @lru_cache
        def jump1(i):
            if i >= N-1: return True
            return any([jump(i+j) for j in range(1, nums[i]+1)])

        def jump2(i):
            if i >= N-1: return True
            if i in cache: return False

            for j in range(1, nums[i]+1):
                if jump(i+j): return True

            cache.add(i)
            return False

        def jump():
            cache = [0] * N
            cache[N-1] = True

            for i in range(N-2, -1, -1):
                possible = False
                for j in range(i+1, i+nums[i]+1):
                    if cache[j]:
                        possible = True
                        break
                cache[i] = possible
            return cache


        N = len(nums)
        if N == 1: return True
        if nums[0] == 0: return False

        maximum = nums[0]
        for i in range(1, N):
            if i > maximum: return False # We cannot reach here
            maximum = max(maximum, i+nums[i])
            if maximum >= N-1: return True
        return False
        #cache = set()
        #ache = jump()
        #return cache[0]

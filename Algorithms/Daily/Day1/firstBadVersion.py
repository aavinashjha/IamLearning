# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
import bisect
class Solution:
    def __init__(self):
        self.versions = {1: "G", 2: "G", 3: "G", 4: "B", 5: "B"}

    def isBadVersion(self, version):
        return self.versions[version] == "B"

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Constraints:
        - Latest version fails the quality check
        - After this are also bad
        - n versions [1, 2, ..., n]
        - given bool isBadVersion(version)
        Goal:
        - find first bad one
        Idea:
        - After bad version all are bad
        - g1, g2, g3, ...., b1, b2, b3, ...
        - left most bad is to be found
        - API call would be minimized if we use binary search
        - if bad keep moving to the left
        - if good move to right
        - GGGGG G GGBB [Middle is good, move to right]
        -         GG B B [Move to left] - Middle or left could have leftmost
        """
        def search(l, r):

            if l > r: return l
            mid = (l+r)//2
             # Then left most bad could be this one or one of the left ones
            if self.isBadVersion(mid):
                return search(l, mid-1)
            return search(mid+1, r)

        return search(1, n)

print(Solution().firstBadVersion(5))

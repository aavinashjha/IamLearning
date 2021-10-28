class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Constraints:
        - intervals
        - not sorted
        
        Goal:
        - Return minimum number of intervals to be removed, to make non overlapping
        
        Idea:
        - [1,2] [1, 3] [2,3] [3,4]
        - Single point intersection at start or end can be ignored
        - sort on the basis of start and end
        """
        intervals.sort()
        N = len(intervals)
        if N <= 1: return 0
        ps, pe = intervals[0]
        count = 0
        print(intervals)
        for i in range(1, N):
            s, e = intervals[i]
            if pe > s:
                # Previous will remain same
                # As we are ignoring current one
                # Selection
                if pe > e:
                    ps, pe = s, e
                count += 1
            else:
                ps, pe = s, e
        return count

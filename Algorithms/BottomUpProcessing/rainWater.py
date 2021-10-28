class Stack:
    def __init__(self):
        self.s = list()
        
    def push(self, e):
        self.s.append(e)
    
    def pop(self):
        return self.s.pop()
    
    def empty(self):
        return len(self.s) == 0
    
    def top(self):
        return self.s[-1]
    
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Constraints:
        - Width of each bar is 1
        - n non-negative integers (0 or positive)
        Goal:
        - How much water it can trap
        Idea:
        - For storing water, boundaries should be higher than inside
        - Water stored is governed by 2 factors: height of bar
        - width between two bars
        - difference between boundaries and lesser hights inside
          store water
        - wait for first non zero boundary
        - look for lesser heights
        - diff between boundary and height is water stored
        - larger height make it boundary
        - First non-zero wall is boundary
        - If greater update boundary,
        - On finding greater
         
        - Select bars to be used as boundaries
        - Water between two bars
        - Remove bars smaller
        """
        """
        s = Stack() 
        N, i = len(height), 0
        sol = 0
        while i < N:
            while not s.empty() and height[s.top()] < height[i]:
                index = s.pop()
                sol += (i-index-1)*height[index]
            s.push(i)
            i += 1
        return sol
        """
        N = len(height)
        
        l, r = 1, N-2
        maxL, maxR = height[0], height[N-1]
        sol = 0
        while l <= r:
            if maxL < maxR: # Take the smaller one
                # We are taking smaller one here as
                # min(leftMax, rightMax) was done
                # and smaller is left so thats the bottleneck
                if maxL > height[l]:
                    sol += (maxL-height[l])
                else:
                    maxL = height[l]
                l += 1
            else:
                if maxR > height[r]:
                    sol += (maxR-height[r])
                else:
                    maxR = height[r]
                r -= 1
        return sol
        """
        N = len(height)
        leftMax, rightMax = [0] * N, [0] * N
        
        leftMax[0] = 0
        for i in range(1, N):
             leftMax[i] = max(leftMax[i-1], height[i-1])
        
        rightMax[N-1] = 0
        for i in range(N-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        sol = 0
        #print(leftMax, rightMax)
        for i in range(N):
            sol += max(0, (min(rightMax[i],leftMax[i])-height[i]))
        return sol
        """
        
                
        """
        def leftMax(i):
            # We are finding leftMax and rightMax again and againa hence Dynamic Programming can be used
            maximum = float('-inf')
            while i >= 0:
                maximum = max(maximum, height[i])
                i -= 1
            return maximum

        def rightMax(i):
            maximum = float('-inf')
            while i < N:
                maximum = max(maximum, height[i])
                i += 1
            return maximum
        
        N = len(height)
        sol = 0
        
        for i in range(N):
            sol += (min(leftMax(i), rightMax(i))-height[i])
        
        return sol
        """

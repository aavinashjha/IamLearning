https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems

from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Constraints:
        - Cooldown of 1 day
        Idea:
        - mp(start): maximum profit starting from this point
        1 2 3 0 2
        mp(0, -inf, 0)
        nohold = 0
        hold = -1
        noholdNew = 0
        
        mp(2, -1, 0), mp(1, -1, 0)
        
        hold=-1
        nohold=0
        noholdNew=2
        
        hold=-1
        nohold=0
        noholdNew = 1
        
        mp()
        
        Bottom up processing
        - [1, 2, 3, 0, 2]
        - each element consider or ignore
        - buy = 1, profit = 0
        - sell = 1, profit = -inf
            
        buy(1) --> sell(2)
        sell(1) --> buy(3)
        Transaction is when we start buying
        T[i][k][0]= Max profit on ith day with at most k transactions with no stocks at eod [Sold today or sold earlier]
        
        T[i][k][0] = max(T[i-1][k][1]+prices[i],
                        T[i-1][k][0])
                        
        
        T[i][k][1] = Max profit on ith day with atmost k transactions with 1 stock at eod [Bought today or resting today and carryoing bought stock from early day]
        
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0]-prices[i])
        
        T[i][0] = max(T[i-1][1]+prices[i], T[i-1][0])
        T[i][1] = max(T[i-2][0]-prices[i], T[i-1][1])
        
        T[-1][0] = 0
        T[-1][1] = -inf
        """
        cache = defaultdict(dict)
        cache[-1][0] = 0
        cache[-1][1] = float('-inf')
        cache[-2][0] = 0
        cache[-2][1] = float('-inf')
        N = len(prices)
        
        for i in range(N):
            cache[i][0] = max(cache[i-1][1]+prices[i],
                             cache[i-1][0])
            cache[i][1] = max(cache[i-2][0]-prices[i],
                              cache[i-1][1])
            
        return cache[N-1][0]
        
        def mp(i, ihold, inohold):
            if i >= N: return inohold
            if (i, ihold, inohold) in cache:
                return cache[(i, ihold, inohold)]
            
            hold = max(ihold, inohold-prices[i])
            nohold = max(inohold, ihold+prices[i])
            # We are selling in this transaction
            
            cache[(i+1, hold, inohold)] = mp(i+1, hold, inohold)
            cache[(i+2, hold, nohold)] = mp(i+2, hold, nohold)
            cache[(i, ihold, inohold)] = max(cache[i+1, hold, inohold],
                                            cache[i+2, hold, nohold])
            
            return cache[(i, ihold, inohold)]
            
        N = len(prices)
        cache = dict()
        return mp(0, float('-inf'), 0)
            

        
        
        

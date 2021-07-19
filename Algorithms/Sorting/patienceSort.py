"""
Constraints:
    - Cards are there, we have to minimize number of piles
    - Left most eligible pile
    - Merge of piles

How we ensure that piles are minimum?
- We place card greedily on left most pile
- That ensures we have large spectrum to keep piles minimum
10, 100, 5, ...

10  100
5
We placed 5 in first pile, as the second pile would only be formed if card is greater than the top most element of first pile
That ensures we are placing pile in pile having least values so that new pile on right is not underused
Hence piles are minimized

How is longest increasing subsequence is guaranteed?
- Single card on pile 1 makes a LIS of length 1
- Assume after placing the nth card, cardn into pilek, a subsequence of length k is created
- if cardn+1 > cardn, it is placed on right
- hence inreasing the length of subsequence
NOTE: The pointer links the new crad to top card of pile immediately left

All piles have decreasing cards
Hence number of piles is the length of longest increasing subsequence
A new pile is created only when it is not possible to put card on a pile because its larger than its top element

Example:
    10 5 8 3 9 4 12 11

    10  8  9  12
    5   4     11
    3

"""
from bisect import bisect_left
class Pile:
    def __init__(self):
        self.p = list()

    def __str__(self):
        return "->".join([str(i) for i in self.p])

    def add(self, e):
        self.p.append(e)

    def isEmpty(self):
        return len(self.p) == 0

    def top(self):
        if len(self.p) == 0:
            return
        return self.p[-1]

    def pop(self):
        self.p.pop()

class Piles:
    def __init__(self):
        self.ps = list()
        self.link = list()

    def __str__(self):
        return "\n".join([str(p) for p in self.ps])

    def findPile(self, e):
        """
        Element is to be added on that pile for which
        """
        t = [p.top() for p in self.ps]
        length = len(t)
        if not length: return

        index = bisect_left(t, e)
        if index != length:
            return index
        return

    def add(self, e):
        index = self.findPile(e)
        if index is not None:
            self.ps[index].add(e)
            return

        p = Pile()
        p.add(e)
        if self.ps:
            self.link.append((self.ps[-1].top(), e))
        self.ps.append(p)

    def links(self):
        return self.link

    def piles(self):
        return self.ps

def patienceSort(sequence):
    print('Input: ', sequence)
    N = len(sequence)
    if N == 0: return []
    ps = Piles()
    for i in range(N):
        ps.add(sequence[i])

    # Getting Longest Increasing Subsequence
    lis = list()
    for s, _ in ps.links():
        lis.append(s)
    lis.append(ps.links()[-1][1])

    sol = []
    print(ps)
    while True:
        minimum, mp = float('inf'), None
        for i, p in enumerate(ps.piles()):
            if (not p.isEmpty()) and (p.top() < minimum):
                mp = i
                minimum = p.top()

        if mp is None:
            break
        else:
            sol.append(minimum)
            ps.piles()[mp].pop()
    return lis, sol

seq = [3, 4, -1, 5, 8, 2, 3 ,12, 7, 9 ,10]
print(patienceSort(seq))





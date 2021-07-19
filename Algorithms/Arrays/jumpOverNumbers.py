"""
Constraints:
    - List of non negative numbers
    - We move forward or if 0 if return -1
    - Goal is to reach beyond even on reaching last index
    - Return number of jumps
Idea:
    - Iterate through the array
    - s = 0
    - Keep adding value to index till length is reached
    - Increase number of jumps
    - T: O(n), S: O(1)
Testcase:
    0 1 2 3 4 5 6 7 8 9 10 11
    3 4 1 2 5 6 9 0 1 2 3  1
    |     |   |            |    

"""
def jumpOverNumbers(a):
    N = len(a)
    p, jumps = 0, 0
    while p < N:
        if a[p] == 0: return -1
        p += a[p]
        jumps += 1
    return jumps

a = [3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]
print(jumpOverNumbers(a))



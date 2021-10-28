"""
Constraints:
    - list of movie lengths
    - Duration of flights
Goal:
    - Return a pair of 2 movies whose combined length is the highest
    - Less than or equal to flight length
    - If multiple return the pair of movie with longer longest duration
Idea:
    - sort movie lengths
    - select smallest and largest
    - and keep incrementing left if sum is less than flight length
    - if equal return it
    - if greater return previous one
"""

def select(m, d):
    N = len(m)

    m.sort()

    l, h = 0, N-1

    while l < h:
        if m[l] + m[h] == d:
            return (m[l], m[h])
        elif m[l] + m[h] < d:
            l += 1
        else:
            if m[h] > d or l == 0:
                r -= 1
            else:
                return (m[l-1], m[h])

m = [27,1,10,39,12,52,32,67,76]
d = 77
print(select(m, d))

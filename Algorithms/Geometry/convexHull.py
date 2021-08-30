"""
Convex Hull:
    - Choose leftmost point in convex hull
    - Consider one point outside convex hull, having mouth of crocodile
    - Eat the top most and the bottom most with its two jaws
    - Recurrence: T(N) = T(N-1) + O(N) = O(N^2)
    - h is number of points in convex hull

Orientation(P1, P2)
- P1 is clockwise or counter clock wise relative to P2

- Sorting reduced to convex hull
- Convex Hull as faster as Sorting (Convex hull is atleast O(lgN))
- Given numbers (n, n^2) plot it
- It would be a parabola
- Convex HULL will return those vertices
- And hence has sorted the numbers as well

Count Down Game:
    - Any number of times going to that number allowed : O(n^2) [Triangular number]
    - Only one cut: 2n = O(n)
"""

CW="clockwise"
CCW="counter-clockwise"
SAME="same"

def orientation(p1, p2, o):
    x1, y1 = p1
    x2, y2 = p2
    ox, oy = o
    """
    Slope: y1/x1 > y2/x2, p1 CCW w.r.t p2 [y1x2 > y2x1]
           y1/x1 < y2/x2, p1 CW w.r.t p2 [y1x2 < y2x1]

           (y1-oy)/(x1-ox) > (y2-oy)/(x2-ox)
    """
    if (y1-oy) * (x2-ox) > (y2-oy) * (x1-ox): return CCW
    elif (y1-oy) * (x2-ox) < (y2-oy) * (x1-ox): return CW
    else: return SAME

#print(orientation((5, 9), (3, 8), (4, 2)))

def grahamScan():
    """
    - Select lowest point : take left one if multiple break tie O(N)
    - Sort points in counter clock wise direction w.r.t lowest point O(NlgN)
    - if left turn it adds to convex hull
    - if right turn backup and see the new point with respect from earlier point
    - Scan Processing O(N)
    - Use stack
    """

def jarvis():
    """
    - lowest point
    - wrap around the points
    - take rightmost point at each point
    - if same angle choose closest point
    - O(nh) where h is number of points in convex hull
    """


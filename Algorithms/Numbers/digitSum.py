"""
Digit Sum:
    Constraints:
    - Works for -ve and +ve numbers
    - -2^63 to 2^63
    Idea:
    - Get unit digit and reduce number
"""

def digitSum(n):
    s = 0
    n = abs(n)
    while n:
        s += n % 10
        n = n // 10
    return s
print(digitSum(-10))
print(digitSum(1325132435356))

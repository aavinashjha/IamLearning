"""
Constraint:
    - N and D would not be in simple form if their gcd > 1
    - Base case would be if GCD is 1
Idea:
    - Till GCD of N and D is 1, keep on dividing N and D with GCD
    - Set result[0] = N
    - Set result[1] = D
Time Complexity:
    ?
GCD:
    gcd(9, 6)
    a, b = 9, 6
    a, b = b, a%b // a %b will be smaller than b
    a b
    9 6
    6 3
    3 0

    9 4
    4 1
    1 0

    9/6
    3
    3/2

    3 2
    2 1
    1 0

"""
def simplify_fraction(numerator, denominator, result):
    def gcd(a, b):
        if not b: return a
        return gcd(b, a%b)

    g = gcd(numerator, denominator)
    while g != 1:
        numerator //= g
        denominator //= g
        g = gcd(numerator, denominator)

    result[0] = numerator
    result[1] = denominator

result = [0, 0]
simplify_fraction(8, 1, result)
print(result)

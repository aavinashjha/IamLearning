"""
Constraint:
    - count factors
Idea:
    - One solution is to iterate over all the numbers and see if divisible and increment count
    - O(N)
"""
def count_numbers_factors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0: count += 1
    return count

print(count_numbers_factors(12))

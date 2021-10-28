"""
 S2     S1
[max[  min  ]max]
The middle part should be min sub array

S1+S2= S
if S1 is not min sub array, we could extend it to increase our max subarray
max sum ending at index
"""
def subarray(a):
    N = len(a)
    minimum, maximum = [None]*N, [None]*N
    total, maximum[0], minimum[0] = a[0], a[0], a[0]
    for i in range(1, N):
        total += a[i]
        maximum[i] = max(maximum[i-1]+a[i], a[i])
        minimum[i] = min(minimum[i-1]+a[i], a[i])

    return total, max(maximum), min(minimum)

total, maximum, minimum = subarray([3,-1,2,-1])
print(total, maximum, minimum)
print(max(maximum, total-minimum))

"""
numbers are in range 0..n
find missing number
Idea:
    - Array exhausted and u cannot set element to its correct place that is the number

9 6 4 2 3 5 7 0 1
1 6 4 2 3 5 7 0 9
6 1 4 2 3 5 7 0 9
7 1 4 2 3 5 6 0 9
0 1 4 2 3 5 6 7 9
0 1 3 2 4 5 6 7 9
0 1 2 3 4 5 6 7 9

"""
a = [9,6,4,2,3,5,7,0,1]

def missing(a):
    N, i = len(a), 0

    while i < N:
        val = a[i]
        index = val
        if i == val or val == N:
            i += 1
        else:
            a[i], a[index] = a[index], a[i]
    print(a)
    for i, v in enumerate(a):
        if i != v:
            return i
    return N
a=[1,0,3,2]
print(missing(a))

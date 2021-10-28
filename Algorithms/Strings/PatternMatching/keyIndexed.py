"""
Sort an array a[] of N integers between 0 and R-1
- Count frequencies of each letter using key as index
- Compute frequency cumulates which specify destinations
- Access cumulates using key as index to move items
- Copy back to original array

NOTE: Update count first in index+1 and not index

Time complexity:
- Key indexed counting uses ~11 N + 4R array accesses to sort N items0
  whose keys are integers between 0 and R-1
- Extra space N+R
It is stable, we move key in order we see it in input
"""
def frequency(a):
    # We know that each letter is between a to f (0-5)
    count = [0] * (R+1)

    for e in a:
        count[ord(e)-ord('a')+1] += 1
    return count

def cumulate(count):
    for i in range(R):
        count[i+1] += count[i]

def keyIndexCounting(a):
    N = len(a)
    aux = [None] * N

    print("Input: ", a)
    count = frequency(a)
    print("Frequency: ", count)
    cumulate(count)
    print("Cumulate: ", count)

    for i in range(N):
        index = ord(a[i])-ord('a')
        aux[count[index]] = a[i]
        count[index] += 1

    print(aux)


a = ['d', 'a', 'c', 'f', 'f', 'b', 'd', 'b', 'f', 'b', 'e', 'a']

R = 6
keyIndexCounting(a)

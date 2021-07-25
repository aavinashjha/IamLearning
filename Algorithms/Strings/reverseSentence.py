"""
Reverse Sentence:
    I/P: boy a is this
    O/P: this is a boy

Constraints:
    - Separated by spaces
Ideas:
    - One idea is to replace first word with last and in case of mismatch in number od characters shift other words
    - So we have to iterate through entire list: (n-1, 0), (n-2, 1), (n-3, 2)..
    - And then do a swap and in that process additional n shifts would be required
    - This becomes O(n^2) algorithm

    - Another idea could be just swap all the chars (n-1, 0), ...
    - And then reverse words
    - One pass char swap
    - Another pass swap words
    - Not nested but done in 2 passes O(n)
"""

def reverseSentence(array):
    def reverse(a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    reverse(array, 0, len(array)-1) # All characters reversed - Pass 1
    s = 0
    for i in range(len(array)):
        if array[i] == ' ': # word End
            reverse(array, s, i-1)
            s = i+1

    reverse(array, s, i) # Last word

a = "boy a is this"
a = [c for c in a]
reverseSentence(a)
print("".join(a))

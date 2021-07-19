"""
Constraints:
    - s is a string whose subsequences are to be generated
    - In a subsequence each char could be considered or not
    - If length of s is 1 only 2 subsequences are possible s and ""
    - For empty only 1 subsequence is possible
    - abc -> a, b, c
             ab, ac, bc
             abc

"""

def subsequences(soFar, rest):
    if rest == "":
        print(soFar)
        return
    subsequences(soFar+rest[0], rest[1:])
    subsequences(soFar, rest[1:])

s = "abc"
subsequences("", s)


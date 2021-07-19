"""
same characters at differnt position are considered as unique
Order is important
"""
def permutation(soFar, rest):
    if rest == "":
        print(soFar)
        return
    for i in range(len(rest)):
        permutation(soFar+rest[i], rest[:i] + rest[i+1:])

permutation("", "abc")
    

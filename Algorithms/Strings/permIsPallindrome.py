from collections import defaultdict
def permIsPallindrome(s):
    chars = defaultdict(int)
    for c in s:
        chars[c] += 1
    odd = False
    for _, v in chars.items():
        if v & 1:
            if odd: return False
            odd = True
    return True
print(permIsPallindrome('civic'))
print(permIsPallindrome('ciivc'))
print(permIsPallindrome('abc'))
print(permIsPallindrome('livci'))

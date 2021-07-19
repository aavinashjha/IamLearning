class Sol:
    def isPalindrome(self, s):
        if not s:
            return True

        i, j = 0, len(s) - 1

        while i < j:
            #print(i, j)
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                
                a, b = s[i].lower() if s[i].isalpha() else s[i],\
            s[j].lower() if s[j].isalpha() else s[j]
                #print(a, b)
                if a == b:
                    i += 1
                    j -= 1
                else:
                    return False

        return True
print(Sol().isPalindrome("mad am"))
print(Sol().isPalindrome("mad1am"))

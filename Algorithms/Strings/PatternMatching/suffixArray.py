class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        Constraints:
        - Longest possible length
        Goal:
        - duplicated substrings
        Idea:
        - make all suffixes possible and sort
        banana
        anana
        nana
        ana
        na
        a
        
        a
        ana
        anana
        banana
        nana
        na
        
        Check every next stringd and see max match
        """
        def prefix(w1, w2):
            M, N = len(w1), len(w2)
            i, j = -1, -1
            while i+1 < M and j+1 < N and w1[i+1] == w2[j+1]:
                i += 1
                j += 1
            return i+1
            
        suffix = []
        for i in range(len(s)):
            suffix.append(s[i:])
            
        suffix.sort()
        maxLen = 0
        word = ""
        N = len(suffix)
        for i in range(N-1):
            length = prefix(suffix[i], suffix[i+1])
            if length > maxLen:
                maxLen = length
                word = suffix[i][:length]
        return word
        

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        p, q = 0, 0
        
        while q < len(t):
            if t[q] == s[p]:
                p += 1
            q += 1
            if p == len(s):
                return True
        return False
        
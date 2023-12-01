class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        for i in range(len(t)):
            if t[i] == s[0]:
                return self.isSubsequence(s[1:], t[i+1:])
        return False
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        for i in range(m-1, n):
            if haystack[i] != needle[-1]:
                continue
            if haystack[i+1-m:i+1] != needle:
                continue
            else:
                return i+1-m
        return -1
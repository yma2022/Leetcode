class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        for i in range(0, n-m+1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i+m] != needle:
                continue
            else:
                return i
        return -1
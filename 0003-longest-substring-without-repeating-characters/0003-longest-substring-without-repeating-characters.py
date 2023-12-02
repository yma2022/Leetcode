class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        n = len(s)
        l, r = 0, 0
        res = 0
        while r < n:
            while r < n and s[r] not in s[l:r]:
                r += 1
            res = max(res, r-l)
            l += 1
            
        return res
        
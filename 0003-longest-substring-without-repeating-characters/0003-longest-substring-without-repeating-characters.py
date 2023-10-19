class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left, i = 0, 0
        res = 0
        while i < len(s):
            while s[i] in s[left:i]:                
                left += 1
            i += 1
            res = max(res, i - left)
        return res
        
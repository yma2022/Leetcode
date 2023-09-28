class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in mp:                
                i = max(mp[s[j]], i)
            res = max(j - i + 1, res)
            mp[s[j]] = j + 1
        return res
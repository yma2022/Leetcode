class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = dict()
        res = 0
        
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            res = max(res, j - i + 1)
            mp[s[j]] = j + 1
            
        return res
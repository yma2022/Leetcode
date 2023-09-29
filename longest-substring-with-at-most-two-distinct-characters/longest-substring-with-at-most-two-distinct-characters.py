class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = collections.defaultdict(int)
        n = len(s)
        j = 0
        
        for i in range(n):
            d[s[i]] += 1
            if len(d) > 2:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    del d[s[j]]
                j += 1
                
        return n - j
        
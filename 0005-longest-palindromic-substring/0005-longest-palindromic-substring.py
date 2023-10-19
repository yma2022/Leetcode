class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(s, left, right):
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ""
        for i in range(len(s)):
            s1 = expansion(s, i, i)
            s2 = expansion(s, i, i+1)
            ans = s1 if len(s1) > len(ans) else ans
            ans = s2 if len(s2) > len(ans) else ans
            
        return ans
            
        
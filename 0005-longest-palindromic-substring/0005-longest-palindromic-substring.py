class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expansion(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ""
        for i in range(len(s)):
            str1 = expansion(s, i, i)
            str2 = expansion(s, i, i+1)
            
            ans = str1 if len(str1) > len(ans) else ans
            ans = str2 if len(str2) > len(ans) else ans
            
        return ans
        
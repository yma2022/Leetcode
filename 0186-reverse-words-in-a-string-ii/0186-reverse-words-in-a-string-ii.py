class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            
        s.reverse()
        left = 0
        for i in range(len(s)):
            if i+1 < len(s) and s[i+1] == " " or i+1 == len(s):
                reverse(s, left, i)
            if s[i] == " " and s[i+1] != " ":
                left = i+1
                
        
        
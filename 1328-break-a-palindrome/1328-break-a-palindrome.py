class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        if n == 1:
            return ""
        p_list = list(palindrome)
        for i in range(n // 2):
            if p_list[i] != "a":
                p_list[i] = "a"
                return "".join(p_list)
            
        p_list[n - 1] = "b"
        return "".join(p_list)
        
        
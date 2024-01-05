class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        num = x
        while x:
            digit = x % 10
            x = x // 10
            rev = rev*10 + digit
        print(rev)   
        return rev == num
        
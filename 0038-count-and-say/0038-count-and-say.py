class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        digits = self.countAndSay(n-1)
        print(digits)
        res = ""
        count = 1
        curr = digits[0]
        for c in digits[1:]:
            if c != curr:
                res += str(count) + str(curr)
                curr = c
                count = 1
            else:
                count += 1
        if count and curr:
            res += str(count) + str(curr)
        return res

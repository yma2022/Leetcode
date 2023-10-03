class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        carry = 0
        res = ""
        diff = len(a) - len(b)
        for i in range(len(a) - 1, -1, -1):
            if i - diff >= 0:
                add = int(a[i]) + int(b[i - diff]) + carry
            else:
                add = int(a[i]) + carry
            carry = add // 2
            res = str(add % 2) + res
            # print(i, res)
        if carry:
            res = str(carry) + res
        return res
            
                
        
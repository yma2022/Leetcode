class Solution:
    # def myPow(self, x: float, n: int) -> float:
        # if x == 0.0:
        #     return 0.0
        # # res = 1
        # if n < 0:
        #     x = 1/x
        #     n = -n
        # while n:
        #     if n & 1:
        #         res *= x
        #     x *= x
        #     n //= 2
        # return res
    def binaryExp(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.binaryExp(x, -n)
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        else:
            return self.binaryExp(x * x, n // 2)
    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
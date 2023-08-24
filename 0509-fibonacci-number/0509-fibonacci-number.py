class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # dp = [0] * (2)
        # dp[0] = 0
        # dp[1] = 1
        # for i in range(2,n+1):
        #     sum = dp[0] + dp[1]
        #     dp[0] = dp[1]
        #     dp[1] = sum
        # return dp[1]
        d = {0:0,1:1}
        if n in d:
            return d[n]
        if n - 2 in d and n - 1 not in d:
            return self.fib(n-1) + d[n-2]
        if n - 1 in d and n - 2 not in d:
            return self.fib(n-1) + d[n-1]
        res = self.fib(n-1) + self.fib(n-2)
        d[n] = res
        return res
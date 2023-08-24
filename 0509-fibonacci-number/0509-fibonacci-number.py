class Solution:
    # def fib(self, n: int) -> int:
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
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (2)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            sum = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum
        return dp[1]
class Solution:
    d = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        # dp = [1] * (n + 1)        
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 2] + dp[i - 1]            
        # return dp[n]
        if n in self.d:
            return self.d[n]
        self.d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.d[n]
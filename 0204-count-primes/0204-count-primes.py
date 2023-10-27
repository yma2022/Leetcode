class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [True] * n
        dp[0] = False
        dp[1] = False
        
        for i in range(2, int(sqrt(n)) + 1):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)
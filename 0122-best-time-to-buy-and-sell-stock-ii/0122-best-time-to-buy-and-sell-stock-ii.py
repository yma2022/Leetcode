class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], dp[i-1] + (prices[i] - prices[i-1]))
        return dp[-1]
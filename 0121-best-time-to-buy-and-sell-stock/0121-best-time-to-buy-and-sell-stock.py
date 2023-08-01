class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # p_buy = p_sell = 0
        # max_profit = 0
        # for i in range(len(prices)):
        #     if prices[i] > prices[p_sell]:
        #         p_sell = i
        #         max_profit = max(prices[p_sell] - prices[p_buy], max_profit)
        #     elif prices[i] < prices[p_buy]:
        #         p_buy = i
        #         p_sell = i
        #     else:
        #         pass
        # return max_profit
        length = len(prices)
        dp0, dp1 = -prices[0], 0 #注意这里只维护两个常量，因为dp0的更新不受dp1的影响
        for i in range(1, length):
            dp1 = max(dp1, dp0 + prices[i])
            dp0 = max(dp0, -prices[i])
        return dp1